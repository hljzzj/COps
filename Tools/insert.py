# _*_ coding:utf-8 _*_
import os,sys
import threading
import Queue
import MySQLdb as mdb
import datetime,time
import xlrd


#print "通：%s" % ip["hostIP"]
conn = mdb.connect('113.59.61.225', 'VOAM', 'Dzga@110', 'VOAM');
print conn
cur = conn.cursor(mdb.cursors.DictCursor);
cur.execute("INSERT INTO website_devicegroup(ciso) VALUES ('海康')");
conn.commit()

