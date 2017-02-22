# _*_ coding:utf-8 _*_
import sys
import numpy as np
import cv2
import MySQLdb as mdb
import datetime,time
import Queue


if __name__=='__main__':
    while True:
        queue = Queue.Queue()
        try:
            conn = mdb.connect('46.105.2.169', 'COps', 'Dzga@110', 'COps');
            cur = conn.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT cameraip,username,password FROM website_cameradevice WHERE statusid_id = '1'")
            rows = cur.fetchall()
            #print rows
            cur.close()
        except:
            print "连接出错"
            info = sys.exc_info()
            print info[0], ":", info[1]
        print "程序开始运行%s" % datetime.datetime.now()
        for row in rows:
            print row
            cap = cv2.VideoCapture("rtsp://{0[username]}:{0[password]}@{0[cameraip]}:554/h264/ch1/main/av_stream".format(row))
            print u"连接中"
            # 判断是否正常开启
            print cap.isOpened()

            frameNum = 1
            while (cap.isOpened()):
                ret, frame = cap.read()
                #print frameNum
                frameNum = frameNum + 1
                # 每10帧存储一张图片
                if frameNum % 10 == 1:
                    cv2.imwrite("../static/CToJpeg/image{0[cameraip]}.jpg".format(row),frame,[int(cv2.IMWRITE_JPEG_QUALITY), 95])
                    print "取图完成"
                    break
            cap.release()
            time.sleep(1)
        print "程序结束运行%s" % datetime.datetime.now()
        time.sleep(3600)



