#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
import datetime


class Customerr(models.Model):

    newcus_name = models.CharField(max_length=128, default='name of client', verbose_name='Имя клиента')
    contact = models.CharField(max_length=128, default='Номер телефона')

    def __str__(self):
        return (str(self.newcus_name)+' '+str(self.contact))

class Operation(models.Model):
    operation_name = models.CharField(max_length=128, default='вид работы')
    price = models.FloatField(default='стоимость работы')

    def __str__(self):
        return (str(self.operation_name)+ ' '+str(self.price))

class Repaier(models.Model):
    # Убрал чтобы протестировать ушла ли ошибка создания таблиц
    CHOICE_REP = (
        ('Влад', 'Влад'),
        ('Андрей', 'Андрей')

        )
    repaier_name= models.CharField(max_length=128, choices=CHOICE_REP, default='Влад')


    def __str__(self):
        return (str(self.repaier_name))

class Device(models.Model):

    BRAND_CHOICES = (
        ('HP', 'HP'),
        ('Canon', 'Canon'),
        ('Kyocera','Kyocera'),
        ('Brother', 'Brother'),
        ('Samsung', 'Samsung'),
        ('KonicaMinolta', 'KonicaMinolta'),
        ('Другой', 'Другой')
)
    device_customer = models.ForeignKey(Customerr)
    brand = models.CharField(max_length=1000, choices=BRAND_CHOICES, default='H')
    br_model = models.CharField(max_length=128)
    serial_num = models.CharField(max_length=128)
    total_count = models.IntegerField()



    def __str__(self):
        return (str(self.device_customer)+ ' '+str(self.brand) + ' '+str(self.br_model)+ ' '+str(self.serial_num))

class PartCategory(models.Model):
    part_category_name = models.CharField(max_length=128, default=" ", verbose_name="Категория запчастей")

    def __str__(self):
        return (str(self.part_category_name))

class Part(models.Model):

    category_part = models.ForeignKey(PartCategory, default="", verbose_name="Категория запчасти")
    name_part = models.CharField(max_length=128, null=True, blank=True)
    part_number = models.CharField(max_length=128, null=True, blank=True)
    pcs_part = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return (str(self.category_part) + ' ' + str(self.name_part) + ' ' + str(self.part_number) + ' ' + str(self.pcs_part))


class Order(models.Model):
    order_customer = models.ForeignKey(Customerr, default="", verbose_name="Владелец")
    order_device = models.ForeignKey(Device, default="", verbose_name="Устройство")
    order_repaier = models.ForeignKey(Repaier, default="", verbose_name="Мастер")
    order_part = models.ManyToManyField(Part, default="НЕТ", verbose_name="Детали", null=True, blank=True)
    order_operation = models.ForeignKey(Operation, default="", verbose_name="Вид работ")
    date = models.DateField(default=datetime.date.today, verbose_name="Дата")
    count_now = models.IntegerField(default=0, verbose_name="Счетчик")

    def __str__(self):
        return (
        str(self.date) + ' ' + str(self.order_customer))


        #description = models.TextField(default='..Заметки')


