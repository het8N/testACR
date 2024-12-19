from django.contrib import admin

# Register your models here.
from .models import Company, Building, Employee
admin.site.register(Company)
admin.site.register(Building)
admin.site.register(Employee)
