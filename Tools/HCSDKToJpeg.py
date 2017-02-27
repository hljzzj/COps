# _*_ coding:utf-8 _*_
import ctypes,sys,os,time
from ctypes import *
from datetime import datetime
import MySQLdb as mdb
import Queue

####################################################
### 加载海康SDK动态链接库                        ###
####################################################
HC = cdll.LoadLibrary('lib/libhcnetsdk.so')
####################################################
### 设置数据类型                                   ###
####################################################
BOOL = ctypes.c_bool
INT = ctypes.c_int
LONG = ctypes.c_long
BYTE = ctypes.c_ubyte
WORD = ctypes.c_ushort
CHARP = ctypes.c_char_p
VOIDP = ctypes.c_void_p
HWND = ctypes.c_uint

init = HC.NET_DVR_Init()
if init == 1 :
    print datetime.now(),u"SDK初始化成功"
setconnecttime = HC.NET_DVR_SetConnectTime(600,3)   # 设置连接超时时间与重连次数
getLastError = HC.NET_DVR_GetLastError()    # 返回错误etErrorMsg = HC.NET_DVR_GetErrorMsg()  # 设置连接超时时间与重连次数
print getLastError
#deviceinfoV40 = HC.NET_DVR_DEVICEINFO_V40()
bUseAsynLogin = 0
sDeviceAddress = "46.105.5.20"
wPort = 8000
sUserName = "admin"
sPassword = "66782011"
loginInfo = sDeviceAddress,wPort,sUserName,sPassword
print loginInfo
lUserID = HC.NET_DVR_Login_V40(sDeviceAddress,wPort,sUserName,sPassword)
print lUserID
if lUserID < 0:
    print "登陆失败，错误代码：%d" % getLastError
    HC.NET_DVR_Cleanup()
lChannel = "1"
sPicFileName = "../static/CToJpeg/image%s.jpg" % sDeviceAddress
print "当前图片输出名字：%s" % sPicFileName
wPicSize ="0xff-Auto"
wPicQuality = "0"
lpJpegPara = wPicSize,wPicQuality
#HC.NET_DVR_CaptureJPEGPicture(lUserID,lChannel,*sPicFileName)
ver = HC.NET_DVR_GetSDKVersion()
print getLastError
print ver


logout = HC.NET_DVR_Logout(lUserID)
#name__ == "__main__":
    #startCapture16("46.105.5.63",8000,"admin","66782011",0.0066)
LONG
if __name__ == '__main__':
    cap = cap
