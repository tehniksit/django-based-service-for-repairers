# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 19:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerr',
            name='contact',
            field=models.CharField(default=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd\xd0\xb0', max_length=128),
        ),
        migrations.AlterField(
            model_name='customerr',
            name='newcus_name',
            field=models.CharField(default=b'name of client', max_length=128, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f \xd0\xba\xd0\xbb\xd0\xb8\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='device',
            name='brand',
            field=models.CharField(choices=[(b'HP', b'HP'), (b'Canon', b'Canon'), (b'Kyocera', b'Kyocera'), (b'Brother', b'Brother'), (b'Samsung', b'Samsung'), (b'KonicaMinolta', b'KonicaMinolta'), (b'\xd0\x94\xd1\x80\xd1\x83\xd0\xb3\xd0\xbe\xd0\xb9', b'\xd0\x94\xd1\x80\xd1\x83\xd0\xb3\xd0\xbe\xd0\xb9')], default=b'H', max_length=1000),
        ),
        migrations.AlterField(
            model_name='operation',
            name='operation_name',
            field=models.CharField(default=b'\xd0\xb2\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b', max_length=128),
        ),
        migrations.AlterField(
            model_name='operation',
            name='price',
            field=models.FloatField(default=b'\xd1\x81\xd1\x82\xd0\xbe\xd0\xb8\xd0\xbc\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='order',
            name='count_now',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\xa1\xd1\x87\xd0\xb5\xd1\x82\xd1\x87\xd0\xb8\xd0\xba'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_customer',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, to='landing.Customerr', verbose_name=b'\xd0\x92\xd0\xbb\xd0\xb0\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x86'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_device',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, to='landing.Device', verbose_name=b'\xd0\xa3\xd1\x81\xd1\x82\xd1\x80\xd0\xbe\xd0\xb9\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_operation',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, to='landing.Operation', verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_part',
            field=models.ManyToManyField(default=b'\xd0\x9d\xd0\x95\xd0\xa2', to='landing.Part', verbose_name=b'\xd0\x94\xd0\xb5\xd1\x82\xd0\xb0\xd0\xbb\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_repaier',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, to='landing.Repaier', verbose_name=b'\xd0\x9c\xd0\xb0\xd1\x81\xd1\x82\xd0\xb5\xd1\x80'),
        ),
        migrations.AlterField(
            model_name='part',
            name='category_part',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, to='landing.PartCategory', verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xbf\xd1\x87\xd0\xb0\xd1\x81\xd1\x82\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='partcategory',
            name='part_category_name',
            field=models.CharField(default=b' ', max_length=128, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xbf\xd1\x87\xd0\xb0\xd1\x81\xd1\x82\xd0\xb5\xd0\xb9'),
        ),
        migrations.AlterField(
            model_name='repaier',
            name='repaier_name',
            field=models.CharField(choices=[(b'\xd0\x92\xd0\xbb\xd0\xb0\xd0\xb4', b'\xd0\x92\xd0\xbb\xd0\xb0\xd0\xb4'), (b'\xd0\x90\xd0\xbd\xd0\xb4\xd1\x80\xd0\xb5\xd0\xb9', b'\xd0\x90\xd0\xbd\xd0\xb4\xd1\x80\xd0\xb5\xd0\xb9')], default=b'\xd0\x92\xd0\xbb\xd0\xb0\xd0\xb4', max_length=128),
        ),
    ]
