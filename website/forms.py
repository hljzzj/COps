# _*_ coding:utf-8 _*_

from django import forms
from django.forms import ModelForm
from models import *
class AddCameraForm(ModelForm):
    class Meta:
        model = CameraDevice
        fields = '__all__'
class AddCameraDeviceForm(forms.Form):
    pid = forms.CharField(required=False,label='编号') # required=False允许为空
    name = forms.CharField(label='名称')
    group_list = DeviceGroup.objects.all()
    # print group_list
    group = forms.ModelChoiceField(queryset=DeviceGroup.objects.all(),required=True,label=u'分组')
    region = forms.ModelChoiceField(queryset=DeviceRegion.objects.all(),required=True,label=u'摄像头所在区域')
    direction = forms.ModelChoiceField(queryset=CameraDirection.objects.all(),required=True,label=u'方向')
    ctype = forms.ModelChoiceField(queryset=CameraType.objects.all(),required=True,label=u'摄像头类别')
    brand = forms.ModelChoiceField(queryset=DeviceBrand.objects.all(),required=True,label=u'品牌')
    dtype = forms.ModelChoiceField(queryset=DeviceType.objects.all(),required=True,label=u'型号')
    ip = forms.GenericIPAddressField(protocol='ipv4',label=u'IP:')
    username = forms.CharField(required=False,label=u'帐号', widget=forms.TextInput(attrs={'class':'sp'}))
    password = forms.CharField(required=False,label=u'密码')
    gpslon = forms.CharField(required=False,label=u'经度')
    gpswei = forms.CharField(required=False,label=u'伟度')
    telecom = forms.ModelChoiceField(queryset=Telecom.objects.all(),required=True,label=u'运营商')
    nvrdevice = forms.ModelChoiceField(queryset=NVRDevice.objects.all(),required=True,label=u'后端设备')
    powersupply = forms.ModelChoiceField(queryset=PowerSupply.objects.all(),required=True,label=u'供电方式')
    powerid = forms.CharField(required=False,label=u'供电标识')
class UpdateCameraDeviceForm(forms.Form):
    class Meta:
        model = CameraDevice

class AddDeviceStatusForm(forms.Form):
    devicestatus = forms.CharField()
class AddDeviceGroupForm(forms.Form):
    devicegroup = forms.CharField()
class AddDeviceRegionForm(forms.Form):
    deviceregion = forms.CharField()
class AddCameraDirectionForm(forms.Form):
    cameradirection = forms.CharField()
class AddCameraTypeForm(forms.Form):
    cameratype = forms.CharField()
class AddDeviceBrandForm(forms.Form):
    devicebrand = forms.CharField()
class AddDeviceTypeForm(forms.Form):
    devicetype = forms.CharField()