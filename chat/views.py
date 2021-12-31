import json
from django.contrib.auth import authenticate, login, logout
# from django.http import response
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import CreateUserForm
from .models import ChatHistory, ChatRoom, Message


# @login_required(login_url='login') #decorator for restricting the access if the user is not logged in
def index(request):
    return render(request, 'index.html', {})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('roomDebug')
        else:
            messages.info(request, 'USERNAME OR PASSWORD INCORRECT')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    form = CreateUserForm()
    context = {'form': form}

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('login')

    return render(request, 'register.html', context)


# decorator for restricting the access if the user is not logged in
@login_required(login_url='login')
def roomDeb(request):
    return render(request, 'chatroom.html', {
        'room_name': "camerista"
    })


# decorator for restricting the access if the user is not logged in
@login_required(login_url='login')
def room(request, room_name):

    # User->foreign key pt ChatHistory
    # toate chatHistory care il contin pe acest user
    history = request.user.chathistory_set.all()
    context = {'chathistory': history, 'room_name': room_name}
    (currChatroom, created) = ChatRoom.objects.all().get_or_create(name=room_name)

    if not request.user.chathistory_set.filter(chatRoom__name=room_name).exists():
        ChatHistory(user=request.user, chatRoom=currChatroom).save()

    return render(request, 'chatroom.html', context)


@login_required(login_url='login')
def addNewMessage(request):
    # adauga mesajul in tabela Message
    if request.method == 'POST':
        data = json.loads(request.body) #zice ca json ar fi gol
        roomName = data.get('room-name')
        message = data.get('content')
    

        # roomName = request.POST.get('room-name')
        # mess = request.POST.get('content')

        user = request.user
        room = ChatRoom.objects.all().filter(name=roomName)
        if room.exists():
            Message(author=user, ChatRoom=room, content=message).save()
