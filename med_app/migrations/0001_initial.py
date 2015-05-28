# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('city', models.CharField(max_length=20, default='Тула')),
                ('street', models.CharField(max_length=20)),
                ('house', models.IntegerField()),
                ('apartment', models.IntegerField()),
                ('postal_code', models.IntegerField(default=300000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('doc_name', models.CharField(choices=[('Паспорт', 'Паспорт')], max_length=20, default='Паспорт')),
                ('serial', models.IntegerField()),
                ('number', models.IntegerField()),
                ('date_of_issue', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('family_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('patronymic_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(choices=[('М', 'мужской'), ('Ж', 'женский')], max_length=1)),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Требуемый формат номера: '+999999999'")])),
            ],
        ),
        migrations.CreateModel(
            name='RegAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('city', models.CharField(max_length=20, default='Тула')),
                ('street', models.CharField(max_length=20)),
                ('house', models.IntegerField()),
                ('apartment', models.IntegerField()),
                ('postal_code', models.IntegerField(default=300000)),
                ('patient', models.ForeignKey(to='med_app.Patient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='document',
            name='patient',
            field=models.ForeignKey(to='med_app.Patient'),
        ),
        migrations.AddField(
            model_name='actaddress',
            name='patient',
            field=models.ForeignKey(to='med_app.Patient'),
        ),
    ]
