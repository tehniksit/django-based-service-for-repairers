#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect
from landing.form import *

from django.forms import modelform_factory


def landing(request):

    query_1 = Order.objects.all()
    query = request.GET.get("q")
    if query:
        query_1 = query_1.filter(

            Q(order_device__serial_num__icontains=query) |
            Q(order_device__brand__icontains=query) |
            Q(order_device__br_model__icontains=query) |
             Q(order_customer__newcus_name__icontains=query) |
             Q(order_repaier__repaier_name__icontains=query)
        )

    form_class = modelform_factory(Order, exclude=[])
    if request.method == "POST":

        form = form_class(request.POST, instance=Order())
        if form.is_valid():
            form.save()
            return redirect('landing')
    else:
        form = form_class(instance=Order())
    for f in form.fields:
        form.fields[f].widget.attrs['class'] = 'form-control'
    return render(request, 'landing/landing.html/', locals(), {'form': form, })


