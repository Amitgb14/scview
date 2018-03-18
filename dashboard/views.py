# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required(login_url="/login/")
def dashboard(request):

    return render(request, "dashboard.html")

