# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 18:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('district_office', '0003_auto_20171110_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthExamination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(max_length=70)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='district_office.Person')),
            ],
            options={
                'verbose_name_plural': 'Health Examinations',
            },
        ),
    ]
