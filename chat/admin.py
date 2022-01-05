from django.contrib import admin
from .models import Message, ChatRoom, ChatHistory, BannedUser

#pentru a putea accesa tabelele din admin
admin.site.register(Message)
admin.site.register(ChatRoom)
admin.site.register(ChatHistory)
admin.site.register(BannedUser)