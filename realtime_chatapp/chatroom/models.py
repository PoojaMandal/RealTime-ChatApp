from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class ChatRoom(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,on_delete=models.CASCADE)
    identifier = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    participants = models.ManyToManyField(User, related_name='chat_rooms')

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.username


# class ChatRoom(models.Model):
#     identifier = models.CharField(max_length=100, unique=True)
#     name = models.CharField(max_length=255)
#     participants = models.ManyToManyField('User', related_name='chat_rooms')

#     def __str__(self):
#         return self.name




# from django.conf import settings
# from django.contrib.auth.models import User
# from django.db import models

# class ChatRoom(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
#     identifier = models.CharField(max_length=100, unique=True)
#     name = models.CharField(max_length=255)
#     participants = models.ManyToManyField(User, related_name='chat_rooms')

#     def __str__(self): 
#         return self.name
