from django.contrib import admin
from .models import AlumniInfo,StaffInfo,StudentInfo,chat
# Register your models here.
admin.site.register(AlumniInfo)
admin.site.register(StaffInfo)
admin.site.register(StudentInfo)
admin.site.register(chat)
