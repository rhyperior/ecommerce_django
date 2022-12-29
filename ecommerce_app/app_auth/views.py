from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def signup(request):
    if request.method=="POST":
        username = request.POST['email']
        email = username
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            return render(request,'auth/signup.html')
            
        try:
            if User.objects.get(username=email):

                messages.warning(request,"Email is already Taken")
                return render(request,'auth/signup.html')

        except Exception as identifier:
            pass

        
        myuser = User.objects.create_user(email, email, password)
        # myuser.first_name=first_name
        # myuser.last_name=last_name
        myuser.save()
        messages.info(request,"Signup SuccessFull! Please Login ")
        return redirect('/app_auth/login')

    return render(request,'auth/signup.html')

def handle_login(request):
    if request.method=="POST":

        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)
        print(myuser)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return render(request,'index.html')

        else:
            messages.error(request,"Something went wrong")
            return redirect('/app_auth/login')

    return render(request, 'auth/login.html')

def handle_logout(request):
    logout(request)
    messages.success(request, 'logged out!')
    return redirect('/app_auth/login')