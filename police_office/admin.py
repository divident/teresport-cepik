# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin

from .models import Person, Company, Car, InsuranceCompany, Policy, TechnicalExamination

admin.site.register(Person)
admin.site.register(Company)
admin.site.register(Car)
admin.site.register(InsuranceCompany)
admin.site.register(Policy)
admin.site.register(TechnicalExamination)
