# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Car, Person, HealthExamination, TechnicalExamination
import datetime
import string
import random

"""
Generate random character string of given size
"""


def char_generator(str_size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(str_size))


def rand_date():
    return timezone.now() - datetime.timedelta(days=(random.randint(0, 31) + 365 * random.randint(18, 30)))


def create_person():
    return Person.objects.create(
        pesel=char_generator(Person._meta.get_field('pesel').max_length, string.digits),
        first_name=char_generator(Person._meta.get_field('first_name').max_length, string.ascii_uppercase),
        last_name=char_generator(Person._meta.get_field('last_name').max_length, string.ascii_uppercase),
        gender='M',
        birth_date=rand_date(),
        birth_place=char_generator(Person._meta.get_field('birth_place').max_length, string.ascii_uppercase),
        postal_code=char_generator(Person._meta.get_field('postal_code').max_length, string.ascii_uppercase),
        city=char_generator(Person._meta.get_field('city').max_length, string.ascii_uppercase),
        street_address=char_generator(Person._meta.get_field('street_address').max_length, string.ascii_uppercase),
        local_number=char_generator(Person._meta.get_field('local_number').max_length, string.digits),
    )


def create_car():
    return Car.objects.create(
        vin=char_generator(Car._meta.get_field('vin').max_length),
        owner=create_person(),
        reg_no=char_generator(Car._meta.get_field('reg_no').max_length),
        model=char_generator(Car._meta.get_field('model').max_length),
        mark=char_generator(Car._meta.get_field('mark').max_length),
        production_year=rand_date(),
        engine_number=char_generator(Car._meta.get_field('engine_number').max_length, string.digits),
        engine_capacity=random.randint(1000, 2000),
        engine_power=random.randint(100, 300),
        last_tech_exam=rand_date(),
		car_status = Normal;
    )

def create_health_examination():
    return HealthExamination.objects.create(
      doctor=char_generator(HealthExamination._meta.get_field('doctor').max_length, string.ascii_uppercase),
      person=create_person(),
      start_date = rand_date(),
      end_date = rand_date(),
    )

def create_technical_examination():
    return TechnicalExamination.objects.create(
      doctor=char_generator(TechnicalExamination._meta.get_field('technician').max_length, string.ascii_uppercase),
      person=create_person(),
      start_date = rand_date(),
      end_date = rand_date(),
    )

class CarListViewTest(TestCase):
    def test_no_car(self):
        """
    If no cars exist, an appropriate message is displayed.
    """
        response = self.client.get(reverse('district_office:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No cars are available.")
        self.assertQuerysetEqual(response.context['all_car_list'], [])

    def test_car_exist(self):
        """
    If cars exist in databse, they are display
    """
        car = create_car()
        response = self.client.get(reverse('district_office:index'))
        self.assertQuerysetEqual(
            response.context['all_car_list'],
            ['<Car: ' + str(car) + '>']
        )


class CarDetailViewTests(TestCase):
    def test_car_dont_exist(self):
        """
    If car which given vin number does't exist in databse detail
    view returns a 404 not found
    """

        vin = char_generator(Car._meta.get_field('vin').max_length - 1)

        url = reverse('district_office:detail', args=(vin,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_car_exist(self):
        """
    If car exist, detail view of it will be display
    """
        car = create_car()
        url = reverse('district_office:detail', args=(car.vin,))
        response = self.client.get(url)
        self.assertContains(response, car.vin)

class HealthExaminationViewTest(TestCase):
  def test_no_health_examination(self):
    """
        If no health examinations exist, an appropriate message is displayed.
        """
    response = self.client.get(reverse('district_office:health'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "No health examinations are available.")
    self.assertQuerysetEqual(response.context['all_health_examination_list'], [])

  def test_health_examination_exist(self):
    """
    If health examinations exist in databse, they are display
    """
    health_examination = create_health_examination()
    response = self.client.get(reverse('district_office:health'))
    self.assertQuerysetEqual(
      response.context['all_health_examination_list'],
      ['<HealthExamination: ' + str(health_examination) + '>']
    )

    class TechnicalExaminationViewTest(TestCase):
        def test_no_technical_examination(self):
            """
                If no technical examinations exist, an appropriate message is displayed.
                """
            response = self.client.get(reverse('district_office:technical'))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "No technical examinations are available.")
            self.assertQuerysetEqual(response.context['all_technical_examination_list'], [])

        def test_technical_examination_exist(self):
            """
            If technical examinations exist in databse, they are display
            """
            technical_examination = create_technical_examination()
            response = self.client.get(reverse('district_office:technical'))
            self.assertQuerysetEqual(
                response.context['all_technical_examination_list'],
                ['<technicalExamination: ' + str(technical_examination) + '>']
            )
