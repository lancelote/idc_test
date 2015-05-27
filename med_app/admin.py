from django.contrib import admin
from .models import Patient, Document, RegAddress, ActAddress

admin.site.register((Patient, Document, RegAddress, ActAddress))
