from django.contrib import admin
from .models import Doctor, Patient


# admin.site.register(Person)
admin.site.register(Doctor)
admin.site.register(Patient)