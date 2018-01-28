# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)
SPECIAL_treatment_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'Yes'),
    )
class Person(models.Model):
    class Meta:
        verbose_name_plural = 'People'
    pesel = models.CharField(max_length=11, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    street_address = models.CharField(max_length=30)
    local_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
    
class Company(models.Model):
    class Meta:
        verbose_name_plural = 'Companies'

    nip = models.IntegerField(primary_key=True, validators=[MaxValueValidator(9999999999),MinValueValidator(000000000)])
    regon = models.IntegerField(validators=[MaxValueValidator(999999999),MinValueValidator(000000000)])
    company_name = models.CharField(max_length=50)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    street_address = models.CharField(max_length=30)
    local_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return '%s %s' % (self.nip, self.company_name)
class Car(models.Model):
    vin = models.CharField(max_length=17, primary_key=True)
    owner = models.ForeignKey(Company, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=8)
    model = models.CharField(max_length=50)
    mark = models.CharField(max_length=50)
    production_year = models.DateField()
    engine_number = models.CharField(max_length=20)
    engine_capacity = models.IntegerField()
    engine_power = models.IntegerField()
    last_tech_exam = models.DateField()
    special_treatment = models.CharField(max_length=1, choices=SPECIAL_treatment_CHOICES)

    """
  Make possible to display all fields of car, using for loop.
  """

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


class InsuranceCompany(models.Model):
    class Meta:
        verbose_name_plural = 'Inscurance Companies'

    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street_addres = models.CharField(max_length=30)
    local_number = models.CharField(max_length=10, blank=True)


class Policy(models.Model):
    class Meta:
        verbose_name_plural = 'Policies'

    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
                                    
class TechnicalExamination(models.Model):
    class Meta:
        verbose_name_plural = 'Technical Examinations'

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    technician_person = models.CharField(max_length=70, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

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
      return str(self.person)
