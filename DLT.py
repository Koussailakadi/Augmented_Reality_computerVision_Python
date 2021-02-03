import glob
from imagePoints import *

class DLT:
    def __init__(self,M,K=None):
        self.objImage=PointsImage()
        self.mtxH=[]
        self.M=M #points monde
        self.K=K

    def calculerDLT(self):
        self.mtxH,statut=cv2.findHomography(self.objImage.m,self.M)

    def virtuel(self):
        thresh=200
        images = glob.glob("videoFrame/*.jpg")
        i = 0
        for fname in images:
            self.objImage.getPointImeage(fname) #pour récupérer les poits images et points monde
            img = cv2.imread(fname)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            size = gray.shape[::-1]
            ret, corners = cv2.findChessboardCorners(gray, (6, 4), None)
            print(corners)
            # print(corners)
            # result is dilated for marking the corners, not important
            gray = np.float32(gray)
            dst = cv2.cornerHarris(gray, 2, 3, 0.04)

            # result is dilated for marking the corners, not important
            dst = cv2.dilate(dst, None)
            if ret:
                obj_points.append(objp)

                corners2 = cv2.cornerSubPix(gray, corners, (5, 5), (-1, -1), criteria)
                # print(corners2)
                if [corners2]:
                    img_points.append(corners2)
                else:
                    img_points.append(corners)

                cv2.drawChessboardCorners(img, (6, 4), corners, ret)
                i += 1;
                cv2.imwrite('videoFrameAR/conimg' + str(i) + '.jpg', img)
                cv2.waitKey(4000)

                data = {'x:': self.objImage.x, 'y': self.objImage.y, 'z': L[0]}
                print('poits images:\n', pd.DataFrame(data))

                dim = (600, 600)
                img[dst > 0.4 * dst.max()] = [0, 0, 255]  # [34, 153, 84]  points rouge

                resised = cv2.resize(img, dim)
                cv2.imshow('les bores en points rouges', resised)
                if cv2.waitKey(0) & 0xff == 'q':
                    cv2.destroyAllWindows()

            cv2.destroyAllWindows()
    def calib(self):
        CHECKERBOARD = (6, 9)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        objp = np.zeros((4 * 6, 3), np.float32)
        objp[:, :2] = np.mgrid[0:6, 0:4].T.reshape(-1, 2)  #

        obj_points = []  # point 3D
        img_points = []  # point 2D

        images = glob.glob("videoFrame/*.png")
        i = 0
        for fname in images:
            img = cv2.imread(fname)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            size = gray.shape[::-1]
            gray = np.float32(gray)
            dst = cv2.cornerHarris(gray, 2, 3, 0.04)

            # result is dilated for marking the corners, not important
            dst = cv2.dilate(dst, None)

            if ret:

                obj_points.append(objp)

                corners2 = cv2.cornerSubPix(gray, corners, (5, 5), (-1, -1), criteria)
                # print(corners2)
                if [corners2]:
                    img_points.append(corners2)
                else:
                    img_points.append(corners)

                cv2.drawChessboardCorners(img, (6, 4), corners, ret)
                i += 1;
                cv2.imwrite('videoFrameAR/img' + str(i) + '.jpg', img)
                cv2.waitKey(1000)

        cv2.destroyAllWindows()


M=[[0,0,1],[0,43,1],[40,0,1],[40,43,1]] #points monde
dlt=DLT(M)
dlt.calculerDLT()
print(dlt.mtxH)
a=np.matmul(dlt.mtxH,M)
print(a/a[2])
