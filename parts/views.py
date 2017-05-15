from django.db.models import Q
from django.shortcuts import render, redirect
from landing.form import *
from django.forms import modelform_factory

def parts(request):
    query_1 = Part.objects.all()
    query = request.GET.get("q")
    if query:
        query_1 = query_1.filter(
            Q(category_part__part_category_name__icontains=query) |
            Q(name_part__icontains=query) |
            Q(part_number__icontains=query) |
            Q(pcs_part__icontains=query)
        )

    form_class = modelform_factory(Part, exclude=[])
    if request.method == "POST":

        form = form_class(request.POST, instance=Part())
        if form.is_valid():
            form.save()
            return redirect('parts')
    else:
        form = form_class(instance=Part())
    for f in form.fields:
        form.fields[f].widget.attrs['class'] = 'form-control'
    return render(request, 'landing/parts.html/', locals(), {'form': form, })




