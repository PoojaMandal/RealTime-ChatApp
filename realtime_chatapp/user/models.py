from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
# Create your models here.


class PhoneNumbers(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField("Phone Number", max_length=500)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return "%s - %s - %s" % (self.user.first_name, self.phone, self.is_active)
    

class Role(TimeStampedModel):
    name = models.CharField(max_length=200)
    shortcode = models.CharField(max_length=200)

    def __str__(self):
        return "%s - %s" % (self.name, self.shortcode)    
    
    
class Profile(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone_verified = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    profile_complete = models.BooleanField(default=False)

    def __str__(self):
        return "%s - %s - %s" % (self.user, self.role, self.is_active)    
    
    
class UserManagement(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    logged_in = models.BooleanField(default=True)
    logged_in_time = models.DateTimeField()
    expiry_time = models.DateTimeField()
    device_ip = models.TextField(null=True, blank=True)
    device_token = models.TextField(null=True, blank=True)
    device_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return "%s" % (self.user)    
    
    

class ResetPassword(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=200)

    def __str__(self):
        return "%s - %s" % (self.user, self.otp)    