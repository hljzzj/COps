# _*_ coding:utf-8 _*_
import sys
import cv2

def CToJpeg(i):
    cap = cv2.VideoCapture("rtsp://%u:%p@%i/stream2" % i["username"],i["passwd"],i["cameraip"])

    #判断是否正常开启
    print cap.isOpened()

    frameNum = 1
    while(cap.isOpened()):
        ret,frame = cap.read()
        print frameNum
        frameNum = frameNum + 1
        cv2.imshow("frame",frame)
    #每10帧存储一张图片
        if frameNum%10 == 1:
            cv2.imwrite("image"+str(frameNum)+".jpg",frame)
        if cv2.waitKey(1) == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    i = {'username':'admin','passwd':'66782011','cameraip':'46.105.7.45'}
    print i
    CToJpeg(i)

