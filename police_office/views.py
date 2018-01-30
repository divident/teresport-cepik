# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from reportlab.pdfgen import canvas
from .models import PoliceCar

class PoliceCarListView(generic.ListView):
  template_name = 'police_office/index.html'
  context_object_name = 'all_police_cars_list'
  
  def get_queryset(self):
    return PoliceCar.objects.all()

@method_decorator(login_required, name='dispatch')
class PoliceCarDetailView(generic.DetailView):
    model = PoliceCar
    template_name = 'police_office/detail.html'

    def get_queryset(self):
        return PoliceCar.objects.filter(pk=self.kwargs['pk'])




