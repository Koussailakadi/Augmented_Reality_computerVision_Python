import cv2
import numpy as np

#lire une video
class openCV:

    def LireVideo(self):
        cap = cv2.VideoCapture(0)
        cap.set(3, 640)
        cap.set(4, 480)
        cap.set(10, 200)

        while True:
            success, img = cap.read()
            # gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            imgCanny = cv2.Canny(img, 100, 100)
            cv2.imshow('Video', imgCanny)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print('fin')
                break

    def DrawImage(self,filename):
        img=cv2.imread(filename)
        cv2.line(img,(0,0),(img.shape[1],img.shape[0]),color=(0,255,0),thickness=3)
        resised=cv2.resize(img,(600,600))
        cv2.imshow('image',resised)
        cv2.waitKey(0)

    def poitdetection(self):
        img = cv2.imread('videoFrame/frame0.jpg')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        dst=cv2.cornerHarris(gray,2,3,0.04)
        dst=cv2.dilate(dst,None)
        img[dst>0.3*dst.max()]=[0,0,255]

        resized = cv2.resize(img, (500, 500))
        cv2.imshow('image', resized)
        cv2.waitKey(0)

image=openCV()
image.poitdetection()
