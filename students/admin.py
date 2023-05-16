from django.contrib import admin
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ("f_name", "l_name", "birth_date",)
admin.site.register(Student, StudentAdmin)