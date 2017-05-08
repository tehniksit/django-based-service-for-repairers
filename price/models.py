#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

class DeviceCategory(models.Model):
    name_cat = models.CharField(default='', verbose_name='Имя категории', max_length=128)

    def __str__(self):
        return (str(self.name_cat))

    # mono_pr14 = models.CharField(max_length=128, default='Монохромный принтер до 14стр', verbose_name='МоноПрДо14')
    # mono_pr35 = models.CharField(max_length=128, default='Монохромный принтер до 35стр', verbose_name='МоноПрДо35')
    # mono_pr36 = models.CharField(max_length=128, default='Монохромный принтер от 36стр', verbose_name='МоноПрОт36')
    #
    # color_pr14 = models.CharField(max_length=128, default='Цветной принтер до 14стр', verbose_name='ЦветПр14')
    # color_pr30 = models.CharField(max_length=128, default='Цветной принтер до 30стр', verbose_name='ЦветПрДо30')
    # color_pr31 = models.CharField(max_length=128, default='Цветной принтер от 31стр', verbose_name='ЦветПрОт31')
    #
    # copir14 = models.CharField(max_length=128, default='Копир монохромный до 14стр', verbose_name='КопирДо35')
    # copir35 = models.CharField(max_length=128, default='Копир монохромный до 35стр', verbose_name='КопирДо36')
    # copir36 = models.CharField(max_length=128, default='Копир монохромный от 36стр', verbose_name='КопирОт35')
    # copirA3 = models.CharField(max_length=128, default='Копир монохромный A3', verbose_name='КопирA3')
    #
    # mfu_mono14 = models.CharField(max_length=128, default='МФУ монохромное до 14стр', verbose_name='МФУмоноДо14')
    # mfu_mono35 = models.CharField(max_length=128, default='МФУ монохромное до 35стр', verbose_name='МФУмоноДо35')
    # mfu_mono36 = models.CharField(max_length=128, default='МФУ монохромное от 36стр', verbose_name='МФУмоноОт36')
    # mfu_mono50 = models.CharField(max_length=128, default='МФУ монохромное от 50стр', verbose_name='МФУмоноОт50')
    # mfu_monoA3 = models.CharField(max_length=128, default='МФУ монохромное А3', verbose_name='МФУмоноА3')
    #
    # mfu_color14 = models.CharField(max_length=128, default='МФУ цветное до 14стр', verbose_name='МФУцветДо14')
    # mfu_color30 = models.CharField(max_length=128, default='МФУ цветное до 35стр', verbose_name='МФУцветДо30')
    # mfu_color31 = models.CharField(max_length=128, default='МФУ цветное от 36стр', verbose_name='МФУцветОт31')
    # mfu_colorA3 = models.CharField(max_length=128, default='МФУ цветное А3', verbose_name='МФУцветА3')

class TypeOfWork(models.Model):
    device_category = models.ForeignKey(DeviceCategory)
    diagnostika = models.IntegerField(default=0,verbose_name='Диагностика')
    profilaktika = models.IntegerField(default=0, verbose_name='Профилактика')
    teh_obs = models.IntegerField(default=0, verbose_name='Техническое обслуживание')
    rem_0kat= models.IntegerField(default=0, verbose_name='Ремонт узла 0-й категории сложности')
    rem_1kat = models.IntegerField(default=0, verbose_name='Ремонт узла 1-й категории сложности')
    rem_2kat = models.IntegerField(default=0, verbose_name='Ремонт узла 2-й категории сложности')
    rem_3kat = models.IntegerField(default=0, verbose_name='Ремонт узла 3-й категории сложности')

    def __str__(self):
        return (str(self.device_category))


class Device(models.Model):

    category = models.ForeignKey(TypeOfWork, verbose_name='Категория')
    name_dev = models.CharField(default='', verbose_name='Наименование', max_length=128)


    def __str__(self):
        return (str(self.name_dev))

class Relations(models.Model):
    dev_model = models.ForeignKey(Device, verbose_name='Устройство', primary_key=True)

    def __str__(self):
        return (str(self.dev_model))
