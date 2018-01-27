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
from .models import Car

class CarListView(generic.ListView):
  template_name = 'police_office/index.html'
  context_object_name = 'all_car_list'
  
  def get_queryset(self):
    return Car.objects.all()
    
class CarDetailView(generic.DetailView):
   model = Car
   template_name = 'police_office/detail.html'
   
   def get_queryset(self):
     return Car.objects.filter(pk=self.kwargs['pk'])
