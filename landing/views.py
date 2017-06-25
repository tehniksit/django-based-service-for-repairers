#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, InvalidPage
from landing.form import *
from django.db.models import Q
from django.forms import modelform_factory


def landing(request, sort_id ):

    try:
        page_num = request.GET["page"]
    except KeyError:
        page_num = 1

    if sort_id =='1':
        sort1 = Order.objects.all().order_by('-date','-id')
    elif sort_id =='2':
        sort1 = Order.objects.all().order_by('order_repaier__repaier_name')
    elif sort_id =='3':
        sort1 = Order.objects.all().order_by('order_customer__newcus_name')
    else:
        sort1 = Order.objects.all()

    paginator = Paginator(sort1, 8)

    current_page = int(page_num)


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


        form = form_class(request.POST,  instance=Order() )
        if form.is_valid():
            form.save()

            return redirect('/landing/1/')
    else:
        form = form_class(instance=Order())

    if query is None or query =='':
        try:
            sort1 = paginator.page(page_num)
        except InvalidPage:
            sort1 = paginator.page(1)

    for f in form.fields:
        form.fields[f].widget.attrs['class'] = 'form-control'




    return render(request, 'landing/landing.html/', locals(), {'form': form, })

