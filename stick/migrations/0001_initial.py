# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-13 05:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('association', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('comment_content', models.TextField(verbose_name='评论内容')),
                ('comment_parent', models.IntegerField(null=True, verbose_name='评论对象')),
                ('comment_parise', models.IntegerField(default=0, verbose_name='点赞数')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('association', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='association.Association', verbose_name='社团账号评论')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Stick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(null=True, verbose_name='评论内容')),
                ('issue_date', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('praise', models.IntegerField(default=0, verbose_name='点赞数量')),
                ('association', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='association.Association', verbose_name='所属社团')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Student', verbose_name='发帖学生')),
            ],
            options={
                'db_table': 'stick',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='stick',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stick.Stick', verbose_name='评论帖子'),
        ),
        migrations.AddField(
            model_name='comment',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Student', verbose_name='学生账号评论'),
        ),
    ]