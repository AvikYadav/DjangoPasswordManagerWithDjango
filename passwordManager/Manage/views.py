import random
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User
from .models import passwords
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
# Create your views here.
AllPasswords = list()
def create(request):
    if request.method == "POST":
        user = request.POST["user"]
        password = request.POST["password"]
        email = request.POST["email"]
        first = request.POST["first"]
        last = request.POST["last"]
        user = User.objects.create_user(username=user,password=password,email=email,first_name = first,last_name=last)
        user.save()
        print("user created")
        return HttpResponse("sucessfull")
    return render(request,"createuser.html")


def home(request):
    if request.method == "POST":
        user = request.POST["user"]
        password = request.POST['password']
        user = auth.authenticate(username=user, password=password)
        if user is not None:
            auth.login(request,user)
            global user1
            user1 = request.POST["user"]
            print("login successful")
            return HttpResponse("sucessfull")
        else:
            messages.info(request,"incorrect credentials")
            return redirect("login")
    return render(request,"welcom.html")


def retrive(request):
    password = passwords.objects.all()
    passList = []
    for passwd in password:
        if passwd.user == user1:
            print(passwd.service,passwd.password,passwd.user)
            passwds = passwd.service+" : "+ passwd.password
            passList.append(passwds)
    return render(request,"retrive.html",{"data":passList,"the_title":"here are your passwords"})

def takecommand(request):
    if request.method == "POST":
        command = request.POST['command']
        if command == "r":
            redirect("retrive")
        if command == "g":
            return render(request,"generate.html")
    return render(request,"takeCommand.html")
def GenerateProcess(request):
    if request.method =="POST":
        service = request.POST['command']
        lenthPassword = len(passwords.objects.all())
        print(lenthPassword)
        generate = passwords.create(user =user1,service = service,password = generatePassword())
        generate.save()
        print(passwords.objects.all())
        return HttpResponse("sucess")
    return render(request,"generate.html")
def generatePassword() -> "password":
    password = ""
    for i in range(10):
        PasswordUnit = random.choice(chars)
        password = password+PasswordUnit
    return password
def store(request):
    if request.method =="POST":
        service = request.POST['command']
        passwd = request.POST['passwd']
        store = passwords.create(user=user1, service=service, password=passwd)
        store.save()
    return render(request,"store.html")
def delete(request):
    if request.method =="POST":
        service = request.POST['command']
        dele = passwords.objects.get(user=user1,service=service)
        dele.delete()
        return HttpResponse("delete Successful")
    return render(request,"delete.html")