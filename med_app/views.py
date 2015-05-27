from django.shortcuts import render


def patient_list(request):
    return render(request, 'med_app/patient_list.html', {})
