from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect
from landing.form import *
from django.forms import modelform_factory
from django.http import HttpResponse

def device(request):


    query_1 = Device.objects.all()
    query = request.GET.get("q")
    if query:
        query_1 = query_1.filter(
            Q(device_customer__newcus_name__icontains=query) |
            Q(brand__icontains=query) |
            Q(br_model__icontains=query) |
            Q(serial_num__icontains=query)
        )


    form_class = modelform_factory(Device, exclude=[])
    if request.method == "POST":

        form = form_class(request.POST, instance=Device())
        if form.is_valid():
            form.save()
            return redirect('device')
    else:
        form = form_class(instance=Device())
    for f in form.fields:
        form.fields[f].widget.attrs['class'] = 'form-control'
    return render(request, 'landing/device.html/', locals(), {'form': form, })



