from encodings import search_function
from django.contrib import admin
from app.models import Patient


# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'age', 'gender', 'created']
    list_filter = ['gender']
    search_fields = ['name', 'phone', 'email', 'age']
    list_per_page = 10


admin.site.register(Patient, PatientAdmin)
