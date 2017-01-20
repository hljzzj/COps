# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceDayRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', null=True)),
                ('deviceid', models.ForeignKey(verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87ID', to='website.CameraDevice')),
                ('statusid', models.ForeignKey(verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81ID', to='website.DeviceStatus')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceTimeRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', null=True)),
                ('devideid', models.ForeignKey(verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87ID', to='website.CameraDevice')),
                ('statusid', models.ForeignKey(verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81ID', to='website.DeviceStatus')),
            ],
        ),
    ]
