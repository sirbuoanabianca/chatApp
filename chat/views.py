from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import CreateUserForm

# Create your views here. 

def index(request):
    return render(request, 'index.html', {})

def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('roomDebug')
        else:
            messages.info(request,'USERNAME OR PASSWORD INCORRECT')
            

    context ={}
    return render(request,'login.html', context)


def registerPage(request):
    form = CreateUserForm() 
    context ={'form':form}

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('login')

    return render(request,'register.html', context)

def roomDeb(request):
    return render(request,'chatroom.html',{
        'room_name':"camerista"
        })   

def room(request,room_name):
    return render(request,'chatroom.html',{
        'room_name':room_name
        })    
   