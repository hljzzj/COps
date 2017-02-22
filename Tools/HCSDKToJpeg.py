# _*_ coding:utf-8 _*_
import ctypes,sys,os,time
from ctypes import *
from datetime import datetime
import MySQLdb as mdb
import Queue

####################################################
### 加载海康SDK动态链接库                           ###
####################################################
HC = ctypes.cdll.LoadLibrary('./HCNetSDK.so')
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
print init
#if __name__ == "__main__":
    #startCapture16("46.105.5.63",8000,"admin","66782011",0.0066)
