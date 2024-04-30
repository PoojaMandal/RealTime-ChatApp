# from django.test import TestCase

# # Create your tests here.
# class Message(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
#     message = models.CharField(max_length=1200)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     is_read = models.BooleanField(default=False)

#     def __str__(self):
#         return self.message

#     class Meta:
#         ordering = ('timestamp',)


#   https://github.com/ajmaln/DRF-Chat/blob/master/chat/models.py 
# https://github.com/ajmaln/DRF-Chat/tree/master/templates
#https://github.com/topics/django-chat-app

# class Messages(models.Model):

#     description = models.TextField()
#     sender_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sender')
#     receiver_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='receiver')
#     time = models.TimeField(auto_now_add=True)
#     seen = models.BooleanField(default=False)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"To: {self.receiver_name} From: {self.sender_name}"

#     class Meta:
#         ordering = ('timestamp',)



# class Friends(models.Model):

#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     friend = models.IntegerField()

#     def __str__(self):
#         return f"{self.friend}"


# class UserProfile(models.Model):

#     name = models.CharField(max_length=25)
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=20, unique=True)

#     def __str__(self):
#         return f"{self.name}"