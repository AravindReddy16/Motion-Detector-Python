import cv2
import pywhatkit
import time

list=[]
cam=cv2.VideoCapture(0)
while cam.isOpened():
    ret,frame1=cam.read()
    ret,frame2=cam.read()
    diff = cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    null,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)
    contours,null=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour)<5000:
            continue
        x,y,w,h=cv2.boundingRect(contour)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        list.append('detected')
    if cv2.waitKey(10)==ord('q'):
        break
    elif len(list)==5:
        x=int(time.strftime('%H'))
        y=int(time.strftime('%M'))+1
        pywhatkit.sendwhatmsg('+918247664235','Motion Detected...',x,y)
        print('Message Sent...')
        break
    cv2.imshow('Aravind Cam',frame1)