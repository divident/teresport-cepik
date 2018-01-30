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


class PoliceCarDetailView(generic.DetailView):
    model = PoliceCar
    template_name = 'police_office/detail.html'

    def get_queryset(self):
        return PoliceCar.objects.filter(pk=self.kwargs['pk'])

@method_decorator(login_required, name='dispatch')
class PoliceCarAdd(CreateView):
    model = PoliceCar
    fields=['vin','station_assigned','reg_no','model','mark','production_year',
	'engine_number','engine_capacity','engine_power','special_treatment',]
    success_url = '/police/'

class PoliceCarUpdateView(UpdateView):
    model = PoliceCar
    fields = ['vin', 'station_assigned', 'reg_no', 'model', 'mark', 'production_year',
              'engine_number', 'engine_capacity', 'engine_power', 'special_treatment', ]
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return "/police/"






