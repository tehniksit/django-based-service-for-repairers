from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect
from landing.form import *

def parts(request):

    return render(request, 'landing/parts.html/', locals())




