from django.urls import re_path
from . import consumers


websocket_urlpatterns=[
    re_path(r'ws/chat/(?P<room_name>\w+)/$',consumers.ChatRoomConsumer.as_asgi()),
]

#w=match any word with any length +
#$=end of the path (doar de forma chat/room_name/optional_oriceNume)
