#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from landing.form import *
from django.contrib import auth
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "правильную" страницу

        return redirect('/landing/')
    else:
        print('error')
        # Отображение страницы с ошибкой
        #
    return render(request, 'landing/index.html', locals())
