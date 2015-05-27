# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('city', models.CharField(default='Тула', max_length=20)),
                ('street', models.CharField(max_length=20)),
                ('house', models.IntegerField()),
                ('apartment', models.IntegerField()),
                ('postal_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('doc_name', models.CharField(default='Паспорт', choices=[('Паспорт', 'Паспорт')], max_length=20)),
                ('serial', models.IntegerField()),
                ('number', models.IntegerField()),
                ('date_of_issue', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('family_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('patronymic_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(choices=[('М', 'мужской'), ('Ж', 'женский')], max_length=1)),
                ('phone_number', models.CharField(validators=[django.core.validators.RegexValidator(message="Требуемый формат номера: '+999999999'", regex='^\\+?1?\\d{9,15}$')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ActAddress',
            fields=[
                ('address_ptr', models.OneToOneField(to='med_app.Address', primary_key=True, parent_link=True, serialize=False, auto_created=True)),
            ],
            bases=('med_app.address',),
        ),
        migrations.CreateModel(
            name='RegAddress',
            fields=[
                ('address_ptr', models.OneToOneField(to='med_app.Address', primary_key=True, parent_link=True, serialize=False, auto_created=True)),
            ],
            bases=('med_app.address',),
        ),
        migrations.AddField(
            model_name='document',
            name='patient',
            field=models.ForeignKey(to='med_app.Patient'),
        ),
        migrations.AddField(
            model_name='address',
            name='patient',
            field=models.ForeignKey(to='med_app.Patient'),
        ),
    ]
