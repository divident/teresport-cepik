# Generated by Django 2.0.1 on 2018-01-28 14:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('vin', models.CharField(max_length=17, primary_key=True, serialize=False)),
                ('reg_no', models.CharField(max_length=8)),
                ('model', models.CharField(max_length=50)),
                ('mark', models.CharField(max_length=50)),
                ('production_year', models.DateField()),
                ('engine_number', models.CharField(max_length=20)),
                ('engine_capacity', models.IntegerField()),
                ('engine_power', models.IntegerField()),
                ('last_tech_exam', models.DateField()),
                ('special_treatment', models.CharField(choices=[('Y', 'Yes'), ('N', 'Yes')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('nip', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(0)])),
                ('regon', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999999), django.core.validators.MinValueValidator(0)])),
                ('company_name', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=50)),
                ('street_address', models.CharField(max_length=30)),
                ('local_number', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='InsuranceCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street_addres', models.CharField(max_length=30)),
                ('local_number', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Inscurance Companies',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('pesel', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('birth_date', models.DateField()),
                ('birth_place', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=50)),
                ('street_address', models.CharField(max_length=30)),
                ('local_number', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('insurance_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='police_office.InsuranceCompany')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='police_office.Person')),
            ],
            options={
                'verbose_name_plural': 'Policies',
            },
        ),
        migrations.CreateModel(
            name='TechnicalExamination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technician_person', models.CharField(blank=True, max_length=70)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='police_office.Person')),
            ],
            options={
                'verbose_name_plural': 'Technical Examinations',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='police_office.Person'),
        ),
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='police_office.Company'),
        ),
    ]
