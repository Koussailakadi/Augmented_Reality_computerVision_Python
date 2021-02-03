import cv2
import numpy as np
import pandas as pd
class PointsImage:
    def __init__(self):
        self.x=[]
        self.y=[]
        self.dst=None
        self.m=[[],[],[],[]]

    def getPointImeage(self,filename):
        thresh = 200  # maximum de poits à détecter

        img = cv2.imread(filename)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        gray = np.float32(gray)
        dst = cv2.cornerHarris(gray, 2, 3, 0.04)

        # result is dilated for marking the corners, not important
        dst = cv2.dilate(dst, None)

        # -------
        dst_norm = np.empty(dst.shape, dtype=np.float32)
        cv2.normalize(dst, dst_norm, alpha=100, beta=255, norm_type=cv2.NORM_MINMAX)
        #dst_norm_scaled = cv2.convertScaleAbs(dst_norm)
        dst_norm_scaled = cv2.convertScaleAbs(dst_norm)
        for i in range(dst_norm.shape[0]):
            for j in range(dst_norm.shape[1]):
                if int(dst_norm[i, j]) > thresh:
                    cv2.circle(dst_norm_scaled, (j, i), 5, (0), 2)
                    self.x.append(i)
                    self.y.append(j)

        L=(np.ones((1, len(self.x)))).tolist()
        data={'x:':self.x,'y':self.y,'z':L[0]}
        print('poits images:\n',pd.DataFrame(data))
        self.dst=dst
        #for i in range(3):
        #    self.m[i][0] = self.x[i]
        #    self.m[i][1] = self.y[i]
        #    self.m[i][2] = 1
        # --------------

        # Threshold for an optimal value, it may vary depending on the image.
        dim = (600, 600)
        img[dst > 0.4 * dst.max()] = [0, 0, 255]  # [34, 153, 84]  points rouge

        resised = cv2.resize(img, dim)
        cv2.imshow('les bores en points rouges', resised)
        if cv2.waitKey(0) & 0xff == 27:
            cv2.destroyAllWindows()

    def getPointExemple(self):
        thresh = 200  # maximum de poits à détecter

        filename = 'images/image_29.png'
        img = cv2.imread(filename)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        gray = np.float32(gray)
        dst = cv2.cornerHarris(gray, 2, 3, 0.04)

        # result is dilated for marking the corners, not important
        dst = cv2.dilate(dst, None)

        # -------
        dst_norm = np.empty(dst.shape, dtype=np.float32)
        cv2.normalize(dst, dst_norm, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
        dst_norm_scaled = cv2.convertScaleAbs(dst_norm)
        for i in range(dst_norm.shape[0]):
            for j in range(dst_norm.shape[1]):
                if int(dst_norm[i, j]) > thresh:
                    cv2.circle(dst_norm_scaled, (j, i), 5, (0), 2)
                    self.x.append(i)
                    self.y.append(j)
        L=(np.ones((1, len(self.x)))).tolist()
        data={'x:':self.x,'y':self.y,'z':L[0]}
        print('poits images:\n',pd.DataFrame(data))
        self.dst=dst

        # --------------

        # Threshold for an optimal value, it may vary depending on the image.
        dim = (600, 600)
        img[dst > 0.01 * dst.max()] = [0, 0, 255]  # [34, 153, 84]  points rouge

        resised = cv2.resize(img, dim)
        cv2.imshow('les bores en points rouges', resised)
        if cv2.waitKey(0) & 0xff == 27:
            cv2.destroyAllWindows()



#obj=PointsImage()
#obj.getPointImeage('videoFrame/frame1.jpg')

