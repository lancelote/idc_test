from django.shortcuts import render, get_object_or_404
from .models import Patient, Document, RegAddress, ActAddress


def patient_list(request):
    patients = Patient.objects.order_by('id')
    return render(request, 'med_app/patient_list.html', {'patients': patients})


def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    document = Document.objects.get(patient_id=patient.id)
    reg_address = RegAddress.objects.get(patient_id=patient.id)
    act_address = ActAddress.objects.get(patient_id=patient.id)
    return render(request, 'med_app/patient_detail.html',
                  {'patient': patient,
                   'document': document,
                   'reg_address': reg_address,
                   'act_address': act_address})
