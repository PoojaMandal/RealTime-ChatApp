from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    attachment = models.FileField(upload_to="messagefiles/", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # is_read = models.BooleanField(default=False)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)


    # def __str__(self):
    #     return f"To: {self.receiver_name} From: {self.sender_name}"


class Friends(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend = models.IntegerField()

    def __str__(self):
        return f"{self.friend}"
    
    

# from django.db import models
# from django.conf import settings


# # Create your models here.

# class Conversation(models.Model):
#     initiator = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="convo_starter"
#     )
#     receiver = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="convo_participant"
#     )
#     start_time = models.DateTimeField(auto_now_add=True)


# class Message(models.Model):
#     sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
#                               null=True, related_name='message_sender')
#     text = models.CharField(max_length=200, blank=True)
#     attachment = models.FileField(upload_to="messagefiles/", null=True, blank=True)
#     conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE,)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ('-timestamp',)
    