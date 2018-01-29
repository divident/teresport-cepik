# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models

SPECIAL_treatment_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No'),
    )

class PoliceStation(models.Model):
  postal_code = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  street_address = models.CharField(max_length=50)
  
class PoliceCar(models.Model):
    vin = models.CharField(max_length=17, primary_key=True)
    station_assigned = models.ForeignKey(PoliceStation, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=8)
    model = models.CharField(max_length=50)
    mark = models.CharField(max_length=50)
    production_year = models.DateField()
    engine_number = models.CharField(max_length=20)
    engine_capacity = models.IntegerField()
    engine_power = models.IntegerField()
    special_treatment = models.CharField(max_length=1, choices=SPECIAL_treatment_CHOICES)


    def get_fields(self):
        pairs = []
        for field in self._meta.fields:
            name = field.name
            try:
                pairs.append((name, getattr(self, "get_%s_display" % name)()))
            except AttributeError:
                pairs.append((name, getattr(self, name)))
        return pairs

    def __str__(self):
        return '%s' % (self.vin)


                                    
