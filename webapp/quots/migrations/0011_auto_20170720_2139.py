# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quots', '0010_auto_20170718_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='in',
            name='pic1',
            field=models.ImageField(max_length=200, upload_to='', verbose_name='사진1'),
        ),
        migrations.AlterField(
            model_name='in',
            name='pic2',
            field=models.ImageField(max_length=200, upload_to='', verbose_name='사진2'),
        ),
        migrations.AlterField(
            model_name='in',
            name='pic3',
            field=models.ImageField(max_length=200, upload_to='', verbose_name='사진3'),
        ),
        migrations.AlterField(
            model_name='in',
            name='pic4',
            field=models.ImageField(max_length=200, upload_to='', verbose_name='사진4'),
        ),
        migrations.AlterField(
            model_name='in',
            name='pic5',
            field=models.ImageField(max_length=200, upload_to='', verbose_name='사진5'),
        ),
        migrations.AlterField(
            model_name='in',
            name='pic6',
            field=models.ImageField(max_length=200, upload_to='', verbose_name='사진6'),
        ),
        migrations.AlterField(
            model_name='out',
            name='pic1',
            field=models.ImageField(max_length=200, upload_to='', verbose_name='사진1'),
        ),
        migrations.AlterField(
            model_name='out',
            name='pic2',
            field=models.ImageField(max_length=200, upload_to='', verbose_name='사진2'),
        ),
        migrations.AlterField(
            model_name='out',
            name='pic3',
            field=models.ImageField(max_length=200, upload_to='', verbose_name='사진3'),
        ),
        migrations.AlterField(
            model_name='out',
            name='pic4',
            field=models.ImageField(max_length=200, upload_to='', verbose_name='사진4'),
        ),
        migrations.AlterField(
            model_name='out',
            name='pic5',
            field=models.ImageField(max_length=200, upload_to='', verbose_name='사진5'),
        ),
        migrations.AlterField(
            model_name='out',
            name='pic6',
            field=models.ImageField(max_length=200, upload_to='', verbose_name='사진6'),
        ),
    ]
