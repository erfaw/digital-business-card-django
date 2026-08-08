from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from pages.models import BusinessCard
from .forms import LoginForm

def login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, 'You are Logged in')
                return redirect('index')
            else: 
                messages.error(request, "Invalid Credentials!", 'danger')
                return redirect('login')     
    else:
        login_form = LoginForm()
        context = {"form": login_form}
        return render(request, 'accounts/login.html', context) 

def register(request):
    if request.method == "POST": # TODO (HIGH) search for form validations, forms in django, best practices.
        full_name= request.POST['full_name']
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password'] # TODO (HIGH) add password validation
        password2= request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, "This email was taken already!", 'danger')
                return redirect('register')
            else: 
                if User.objects.filter(username=username).exists():
                    messages.error(request, "This username was taken already!", 'danger')
                    return redirect('register')
                else: 
                    new_user = User.objects.create_user(
                        username,
                        email,
                        password,
                        first_name= full_name,
                    )
                    new_user.save()
                    messages.success(request, "You are successfully registered! can login now.")
                    user_bc = BusinessCard.objects.create(user=new_user)
                    user_bc.save()
                    return redirect('login')
        else:
            messages.error(request, "Passwords doesn't match!", 'danger')
            return redirect('register')
    else: 
        return render(request, 'accounts/register.html') 

@login_required # type: ignore
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.info(request, 'User logged out.')
        return redirect('login')

# TODO (MID) make a way to user reset password. likely must send mail a passcode and with that authenticate then reset password.
