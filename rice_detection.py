# -*- coding:utf-8 -*-
import cv2  
import numpy as np
import matplotlib.pyplot as plt 
    
img = cv2.imread("rice.png")  
#cv2.namedWindow("imagshow", 
#cv2.imshow('imagshow', img)    
 
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
 
dst = cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,101, 1)
 
#res ,dst = cv2.threshold(gray,0 ,255, cv2.THRESH_OTSU)
 
element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3, 3))
dst=cv2.morphologyEx(dst,cv2.MORPH_OPEN,element)  
dst,hierarchy = cv2.findContours(dst,cv2.EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)  
cv2.drawContours(dst,contours,-1,(120,0,0),2)  #绘制轮廓
 
count=0 
ares_avrg=0  
for cont in contours:
 
    ares = cv2.contourArea(cont)
 
    if ares<50:   
        continue
    count+=1    
    ares_avrg+=ares
 
    print("{}-blob:{}".format(count,ares),end="  ") 
 
    rect = cv2.boundingRect(cont) 
 
    print("x:{} y:{}".format(rect[0],rect[1]))
    x={format(rect[0])}
    y={format(rect[1])}
    print(x)
    print(y)
    ellipse = cv2.fitEllipse(cont)
    #cv2.rectangle(img,(0,0),(0,0),(0xff),2)
    cv2.ellipse(img,ellipse,(0xff),2)
 
    y=10 if rect[1]<10 else rect[1] 
 
    cv2.putText(img,str(count), (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1) 
 
print("米粒平均面积:{}".format(round(ares_avrg/ares,2))) 
 
cv2.namedWindow("imagshow", 2)   
cv2.imshow('imagshow', img)    
 
cv2.namedWindow("dst", 2)   
cv2.imshow("dst", dst)  
 
 
#plt.hist(gray.ravel(), 256, [0, 256]) 
#plt.show()
 
 
cv2.waitKey()
