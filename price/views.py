from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect
from price.form import *
from django.forms import modelform_factory

def price(request):

    query = request.GET.get("dev_model")
    if query:
        query_1 = Relations.objects.all()
        query_1 = query_1.filter(

            Q(dev_model__id__icontains=query)
        )


    form_class = RelationsForm(Relations)
    if request.method == "POST":
        form = RelationsForm(request.POST, instance=Relations())

        if form.is_valid():

                return redirect('price')
    else:
        form = RelationsForm(instance=Relations())
    for f in form.fields:
        form.fields[f].widget.attrs['class'] = 'form-control'
    return render(request, 'landing/price.html/', locals(), {'form': form, })







