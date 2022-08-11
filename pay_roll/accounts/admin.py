from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Pay1,Create_Business,Data_Range2,Data_Range1,Period_Number

admin.site.register(User, UserAdmin)
admin.site.register(Pay1)
admin.site.register(Create_Business)
admin.site.register(Data_Range2)
admin.site.register(Data_Range1)
admin.site.register(Period_Number)
