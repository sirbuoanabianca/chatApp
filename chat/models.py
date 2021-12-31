from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    name = models.TextField(unique=True ,max_length=25)
    creation_date = models.DateTimeField(auto_now_add=True)

    # echivalent cu .toString()
    def __str__(self):
        return self.name

class ChatHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chatRoom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    

class Message(models.Model):
    author     = models.ForeignKey(User, on_delete=models.CASCADE)
    chatRoom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
    timeStamp = models.DateTimeField(auto_now_add=True)