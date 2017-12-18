# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Person, Car, InsuranceCompany, Policy, HealthExamination, TechnicalExamination

admin.site.register(Person)
admin.site.register(Car)
admin.site.register(InsuranceCompany)
admin.site.register(Policy)
admin.site.register(HealthExamination)
admin.site.register(TechnicalExamination)
