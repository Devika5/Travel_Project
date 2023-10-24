from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here
def register(request):
    if request.method =='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['pass1']
        password2 = request.POST['pass2']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username is already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,first_name= first_name, last_name=last_name, email=email, password=password)
                user.save();
                messages.info(request,"user created")
        else:
            messages.info(request, "Password not matched")
            return redirect('register')
        return redirect('login')
    return render(request, "register.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        passwor=request.POST['password']
        user=auth.authenticate(username=username,password=passwor)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid username or password")
            return redirect('login')

    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
