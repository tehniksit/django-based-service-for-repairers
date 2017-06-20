#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse

from landing.form import *
from django.db.models import Q
from django.forms import modelform_factory


def landing(request, sort_id):
    if sort_id == '1':
        sort1 = Order.objects.all().order_by('-date')
    elif sort_id == '2':
        sort1 = Order.objects.all().order_by('order_repaier__repaier_name')
    elif sort_id == '3':
        sort1 = Order.objects.all().order_by('order_customer__newcus_name')
    else:
        sort1 = Order.objects.all()

    query = request.GET.get("q")
    if query:
        sort1 = sort1.filter(

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


