from django.contrib import admin
from models import CameraDevice
# Register your models here.
admin.site.register(CameraDevice)
from .ImportExcel import import_user
class CDImportFileAdmin(admin.ModelAdmin):
    list_display = ('file','name')
    list_filter = ['name']
    def save_model(CameraDevice,self, request, obj, form, change):
        re = super(CDImportFileAdmin,self).save_model(request,obj,form,change)
        import_user(self,request,obj,change)
        return re
