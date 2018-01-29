# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin

from .models import PoliceStation, PoliceCar

admin.site.register(PoliceStation)
admin.site.register(PoliceCar)
