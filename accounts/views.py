from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from pages.models import BusinessCard
from .forms import LoginForm, RegisterForm

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
            context = {"form": login_form}
            return render(request, 'accounts/login.html', context)
    else:
        login_form = LoginForm()
        context = {"form": login_form}
        return render(request, 'accounts/login.html', context) 

def register(request):
    if request.method == "POST":

        token = request.POST["g-recaptcha-response"]

        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            full_name= register_form.cleaned_data['full_name']
            username= register_form.cleaned_data['username']
            email= register_form.cleaned_data['email']
            password= register_form.cleaned_data['password'] # Note: validations are inside RegisterForm()

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
            context = {"form": register_form}
            return render(request, "accounts/register.html", context)
    else:
        register_form = RegisterForm()
        context = {"form": register_form}
        return render(request, "accounts/register.html", context)

@login_required # type: ignore
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.info(request, 'User logged out.')
        return redirect('login')

# TODO (MID) make a way to user reset password. likely must send mail a passcode and with that authenticate then reset password.
