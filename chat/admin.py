from django.contrib import admin
from .models import Message, ChatRoom, ChatHistory

admin.site.register(Message)
admin.site.register(ChatRoom)
admin.site.register(ChatHistory)