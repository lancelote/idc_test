from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Patient, Document, RegAddress, ActAddress
from .forms import PatientForm, DocumentForm, RegAddressForm, ActAddressForm


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


@login_required
def patient_new(request):
    if request.method == "POST":
        patient_form = PatientForm(request.POST)
        document_form = DocumentForm(request.POST)
        reg_address_form = RegAddressForm(request.POST, prefix='reg')
        act_address_form = ActAddressForm(request.POST, prefix='act')

        if all((
            patient_form.is_valid(),
            document_form.is_valid(),
            reg_address_form.is_valid(),
            act_address_form.is_valid(),
        )):
            patient = patient_form.save(commit=False)
            patient.save()

            document = document_form.save(commit=False)
            document.patient = patient
            document.save()

            reg_address = reg_address_form.save(commit=False)
            reg_address.patient = patient
            reg_address.save()

            act_address = act_address_form.save(commit=False)
            act_address.patient = patient
            act_address.save()

            return redirect('med_app.views.patient_detail', pk=patient.pk)
    else:
        patient_form = PatientForm()
        document_form = DocumentForm()
        reg_address_form = RegAddressForm(prefix='reg')
        act_address_form = ActAddressForm(prefix='act')
    return render(request, 'med_app/patient_edit.html',
                  {'patient_form': patient_form,
                   'document_form': document_form,
                   'reg_address_form': reg_address_form,
                   'act_address_form': act_address_form})


@login_required
def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    document = Document.objects.get(patient_id=patient.id)
    reg_address = RegAddress.objects.get(patient_id=patient.id)
    act_address = ActAddress.objects.get(patient_id=patient.id)

    if request.method == "POST":
        patient_form = PatientForm(request.POST, instance=patient)
        document_form = DocumentForm(request.POST, instance=document)
        reg_address_form = RegAddressForm(request.POST, prefix='reg',
                                          instance=reg_address)
        act_address_form = ActAddressForm(request.POST, prefix='act',
                                          instance=act_address)

        if all((
            patient_form.is_valid(),
            document_form.is_valid(),
            reg_address_form.is_valid(),
            act_address_form.is_valid(),
        )):
            patient = patient_form.save(commit=False)
            patient.save()

            document = document_form.save(commit=False)
            document.patient = patient
            document.save()

            reg_address = reg_address_form.save(commit=False)
            reg_address.patient = patient
            reg_address.save()

            act_address = act_address_form.save(commit=False)
            act_address.patient = patient
            act_address.save()

            return redirect('med_app.views.patient_detail', pk=patient.pk)
    else:
        patient_form = PatientForm(instance=patient)
        document_form = DocumentForm(instance=document)
        reg_address_form = RegAddressForm(prefix='reg', instance=reg_address)
        act_address_form = ActAddressForm(prefix='act', instance=act_address)
    return render(request, 'med_app/patient_edit.html',
                  {'patient_form': patient_form,
                   'document_form': document_form,
                   'reg_address_form': reg_address_form,
                   'act_address_form': act_address_form})


@login_required
def patient_remove(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('med_app.views.patient_list')
