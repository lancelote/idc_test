from django.shortcuts import render
from .models import Patient


def patient_list(request):
    patients = Patient.objects.order_by('id')
    return render(request, 'med_app/patient_list.html', {'patients': patients})
