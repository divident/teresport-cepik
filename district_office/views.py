# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from .models import Car

class CarListView(generic.ListView):
  template_name = 'district_office/index.html'
  context_object_name = 'all_car_list'
  
  def get_queryset(self):
    return Car.objects.all()
    
class CarDetailView(generic.DetailView):
   model = Car
   template_name = 'district_office/detail.html'
   
   def get_queryset(self):
     return Car.objects.filter(pk=self.kwargs['pk'])
