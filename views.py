# -*- coding: utf-8 -*-
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from zokiguide.decorators import render_to

@render_to('main/home.html')
def home(request):
	data = {}
	return data

