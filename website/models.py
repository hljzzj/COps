# _*_ coding: utf-8 _*_
from django.db import models
# from django.contrib.gis.db import models   # 空间数据
# from django.contrib.gis.db.models.manager import GeoManager # 空间数据

class DeviceStatus(models.Model):
    name = models.CharField(max_length=50,verbose_name='设备状态分类')
    def __unicode__(self):
        return self.name,self,id

class DeviceFault(models.Model):
    name = models.CharField(max_length=50,verbose_name='设备故障原因')
    def __unicode__(self):
        return self.name

class DeviceGroup(models.Model):
    name = models.CharField(max_length=50,verbose_name='设备分组')
    def __unicode__(self):
        return self.name

class DeviceRegion(models.Model):
    name = models.CharField(max_length=50,verbose_name='设备分区')
    def __unicode__(self):
        return self.name

class CameraDirection(models.Model):
    name = models.CharField(max_length=50,verbose_name='摄像头方向')
    def __unicode__(self):
        return self.name

class CameraType(models.Model):
    name = models.CharField(max_length=32,verbose_name='摄像头分类')
    def __unicode__(self):
        return self.name

class DeviceBrand(models.Model):
    name = models.CharField(max_length=32,verbose_name='设备品牌')
    def __unicode__(self):
        return self.name

class DeviceType(models.Model):
    brandid = models.ForeignKey(DeviceBrand,verbose_name='关联设备品牌ID')
    name = models.CharField(max_length=32,verbose_name='设备型号')
    def __unicode__(self):
        return self.name
class Telecom(models.Model):
    name = models.CharField(max_length=32,verbose_name='运营商')
    def __unicode__(self):
        return self.name

class NVRDevice(models.Model):
    name = models.CharField(max_length=32,verbose_name='录像机名称')
    ip = models.GenericIPAddressField(protocol='ipv4',verbose_name='录像机IP')
    username = models.CharField(max_length=32,verbose_name='录像机帐号')
    password = models.CharField(max_length=32,verbose_name='录像机密码')
    def __unicode__(self):
        return self.name

class PowerSupply(models.Model):
    name = models.CharField(max_length=32,verbose_name='供电方式')
    def __unicode__(self):
        return self.name

class PowerID(models.Model):
    name = models.CharField(max_length=50,verbose_name='供电标识')
    def __unicode__(self):
        return self.name

class NetworkDevice(models.Model):
    name = models.CharField(max_length=32,verbose_name='网络设备名称')
    ip = models.GenericIPAddressField(protocol='ipv4',verbose_name='网络设备IP')
    username = models.CharField(max_length=32,verbose_name='网络设备帐号')
    password = models.CharField(max_length=32,verbose_name='网络设备密码')

class ServerHostDevice(models.Model):
    name = models.CharField(max_length=32,verbose_name='服务器名称')
    ip = models.GenericIPAddressField(protocol='ipv4',verbose_name='服务器IP')
    username = models.CharField(max_length=32,verbose_name='服务器帐号')
    password = models.CharField(max_length=32,verbose_name='服务器密码')

class CameraDevice(models.Model):
    pid = models.CharField(max_length=32,verbose_name='摄像头编号',null=True)
    name = models.CharField(max_length=50,verbose_name='摄像头名称')
    groupid = models.ForeignKey(DeviceGroup,verbose_name='摄像头分组')
    regionid = models.ForeignKey(DeviceRegion,verbose_name='摄像头区域划分')
    ctypeid = models.ForeignKey(CameraType,verbose_name='摄像头类别')
    directionid = models.ForeignKey(CameraDirection,verbose_name='摄像头方向')
    ip = models.GenericIPAddressField(protocol='ipv4',verbose_name='摄像机IP')
    username = models.CharField(max_length=50,verbose_name='摄像头帐号',null=True)
    password = models.CharField(max_length=50,verbose_name='摄像头密码',null=True)
    gpslon = models.CharField(max_length=18,verbose_name='经度',null=True)
    gpswei = models.CharField(max_length=18,verbose_name='纬度',null=True)
    statusid = models.ForeignKey(DeviceStatus,verbose_name='设备状态',null=True)
    faultid = models.ForeignKey(DeviceFault,verbose_name='设备故障原因',null=True)
    brandid = models.ForeignKey(DeviceBrand, verbose_name='设备品牌')
    dtypeid = models.ForeignKey(DeviceType,verbose_name='设备型号')
    updatetime = models.DateTimeField(auto_now=True,verbose_name='主机更新时间',null=True)
    addtime = models.DateTimeField(auto_now_add=True,verbose_name='主机添加时间')
    telecomid = models.ForeignKey(Telecom,verbose_name='运营商')
    nvrdeviceid = models.ForeignKey(NVRDevice,verbose_name='后台存储设备',null=True)
    powersupplyid = models.ForeignKey(PowerSupply,verbose_name='供电方式',null=True)
    powerid = models.ForeignKey(PowerID,verbose_name='供电标识',null=True)

