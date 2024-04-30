from django.contrib import admin
from user.models import (PhoneNumbers, Role, Profile, UserManagement, ResetPassword)
# Register your models here.

admin.site.register(PhoneNumbers)
admin.site.register(Role)
admin.site.register(Profile)
admin.site.register(UserManagement)
admin.site.register(ResetPassword)