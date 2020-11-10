from django.contrib import admin
from Regapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['No','Name','Age','Mob','Add']
admin.site.register(Student,StudentAdmin)
