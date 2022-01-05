from django.urls import path

from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('chatroom/message/', views.addNewMessage, name='message'),  #endpoint pt adaugare mesaj nou in tabel
    path('chatroom/welcomeRoom/', views.Welcomeroom, name='welcomeRoom'),
    path('chatroom/<str:room_name>/', views.room, name='room') 
]
