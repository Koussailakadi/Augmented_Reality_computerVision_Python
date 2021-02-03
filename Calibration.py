import cv2
import numpy as np
import glob

class Calibration:
    def __init__(self):
        self.mtx=None # matrice K intrinsèque
        self.rvecs=None # vecteur rotation
        self.tvecs=None # traslation vecteur
        self.dist = None # destortion values

    def calibrerCamera(self):
        # Defining the dimensions of checkerboard
        CHECKERBOARD = (6, 9)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        objp = np.zeros((4 * 6, 3), np.float32)
        objp[:, :2] = np.mgrid[0:6, 0:4].T.reshape(-1, 2)  #

        obj_points = []  # point 3D
        img_points = []  # point 2D

        images = glob.glob("images/*.png")
        i = 0
        for fname in images:
            img = cv2.imread(fname)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            size = gray.shape[::-1]
            ret, corners = cv2.findChessboardCorners(gray, (6, 4), None)
            # print(corners)

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
                cv2.imwrite('imagesAfterCalib/conimg' + str(i) + '.jpg', img)
                cv2.waitKey(4000)

        cv2.destroyAllWindows()

        # calibration
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, size, None, None)


        img = cv2.imread(images[2])
        h, w = img.shape[:2]
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

        #print("------------------use indistor-------------------")
        dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
        x, y, w, h = roi
        dst1 = dst[y:y + h, x:x + w]
        cv2.imwrite('imagesAfterCalib/calibresult3.jpg', dst1)


        # les résultat de calibration
        self.mtx = mtx
        self.rvecs = rvecs
        self.tvecs = tvecs
        self.dist = dist

    def CameraParam(self):
        print("-------------la matrice intrinsèque K---------------")
        print("K :\n", self.mtx)  # intrinsec matrix : K
        print("-------------distortion cofficients-----------------")
        print("dist:\n", self.dist)  # distortion cofficients = (k_1,k_2,p_1,p_2,k_3)
        print("----------------rotation vector---------------------")
        print("R:\n", self.rvecs)  # rotation vector
        print("---------------translation vector-------------------")
        print("tvecs:\n", self.tvecs)  # translation vector
        print("----------------------------------------------------")
