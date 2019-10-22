# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-13 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0003_auto_20190413_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='associationstudent',
            name='remark',
            field=models.CharField(max_length=500, null=True, verbose_name='成员备注'),
        ),
        migrations.AlterField(
            model_name='associationstudent',
            name='apply_to_ass',
            field=models.IntegerField(choices=[(1, '待回复'), (2, '已加入'), (3, '已拒绝')], default=1, verbose_name='入团请求状态'),
        ),
        migrations.AlterField(
            model_name='associationstudent',
            name='apply_to_stu',
            field=models.IntegerField(choices=[(1, '待回复'), (2, '已加入'), (3, '已拒绝')], default=1, verbose_name='邀请请求状态'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='permission',
            field=models.IntegerField(choices=[(1, '公开'), (2, '私密')], verbose_name='权限'),
        ),
    ]