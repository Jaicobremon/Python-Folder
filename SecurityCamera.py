import cv2
import time
import random

startime = time.time()

def takeSnapShot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):

        ret,frame = videoCaptureObject.read()

        imageName = "img" + str(number) + ".png"

        cv2.imwrite(imageName,frame)

        startime = time.time()

        result = False
    
    return imageName
    print("Snapshot Taken.")

    videoCaptureObject.release()

    cv2.destroyAllWindows()

def main():
    while(True):
        if((time.time()-startime) >= 100):
            takeSnapShot()

main()