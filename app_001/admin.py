from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.
"""class UserModel(UserAdmin):
    pass
"""
class lst11(admin.ModelAdmin):
    list_display=("id","email")
admin.site.register(CustomUser,lst11)
admin.site.register(AdminHOD)
admin.site.register(Status)


admin.site.register(LeaveReportStudent)
admin.site.register(Courseregister)
admin.site.register(Staff)
admin.site.register(Addcourse)
class lst2(admin.ModelAdmin):
    list_display=("id","email","rollnumber","gender")
admin.site.register(Students,lst2)