# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render


def home(request):
    data = {}
    return render(request, 'main/home.html', data)