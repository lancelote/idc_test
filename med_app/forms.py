from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Patient, Document, RegAddress, ActAddress


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = (
            'family_name',
            'first_name',
            'patronymic_name',
            'date_of_birth',
            'sex',
            'phone_number',
        )
        labels = {
            'family_name': _('Фамилия'),
            'first_name': _('Имя'),
            'patronymic_name': _('Отчество'),
            'date_of_birth': _('Дата рождения'),
            'sex': _('Пол'),
            'phone_number': _('Номер телефона'),
        }


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = (
            'doc_name',
            'serial',
            'number',
            'date_of_issue',
        )
        labels = {
            'doc_name': _('Документ'),
            'serial': _('Серия'),
            'number': _('Номер'),
            'date_of_issue': _('Дата выдачи'),
        }


class RegAddressForm(forms.ModelForm):

    class Meta:
        model = RegAddress
        fields = (
            'city',
            'street',
            'house',
            'apartment',
            'postal_code',
        )
        labels = {
            'city': _('Город'),
            'street': _('Улица'),
            'house': _('Дом'),
            'apartment': _('Квартира'),
            'postal_code': _('Почтовый индекс'),
        }


class ActAddressForm(forms.ModelForm):

    class Meta:
        model = ActAddress
        fields = (
            'city',
            'street',
            'house',
            'apartment',
            'postal_code',
        )
        labels = {
            'city': _('Город'),
            'street': _('Улица'),
            'house': _('Дом'),
            'apartment': _('Квартира'),
            'postal_code': _('Почтовый индекс'),
        }
