from django.contrib import admin

from .models import *

# Register your models here.


admin.site.register(Recipe)

admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)
