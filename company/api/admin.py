from django.contrib import admin

# Register your models here.
from api.models import company,Employee

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','company')

admin.site.register(company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
