from django.urls import path

from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('chatroom/camerista/', views.roomDeb, name='roomDebug'),
    path('chatroom/<str:room_name>/', views.room, name='room')   
]
