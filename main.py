from Calibration import *
from DLT import *

def main():
    #camera=Calibration()
    #camera.calibrerCamera()
    #camera.CameraParam()
    K=[]
    #K=camera.mtx
    #cordonnee=PointsImage()
    #cordonnee.getPointExemple()
    #poits monde:
    M=np.array([[0,0,1],[0,43,1],[40,0,1],[40,43,1]])
    dlt=DLT(M=M,K=K)
    dlt.virtuel()
    dlt.calculerDLT()
    








if __name__=='__main__':
    main()
