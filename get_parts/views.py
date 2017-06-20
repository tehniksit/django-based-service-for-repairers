#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse

from landing.form import *
from django.db.models import Q
from django.forms import modelform_factory

def get_parts(request, part_id ):
    part1 = Order.objects.all()


    if part_id:
        part1 = part1.filter(

            Q(id=part_id)
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

    context = {
        'form': form,


        'part1': part1,

        'part_id': part_id,


    }
    return render(request, 'landing/get_part.html/', context )