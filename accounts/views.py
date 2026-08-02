from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from pages.models import BusinessCard

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, 'You are Logged in')
            return redirect('index')
        else: 
            messages.error(request, "Invalid Credentials!", 'danger')
            return redirect('login')
    else: 
        return render(request, 'accounts/login.html') 

def register(request):
    if request.method == "POST":
        full_name= request.POST['full_name']
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password'] # TODO add password validation
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

# def dashboard(request): # TODO append this functionality to our dashboard or make a button for it
# user = User.objects.get(pk= request.user.id)
# user_contacts = user.contacts.order_by('-contact_date')
# context = {
#     'contacts': user_contacts,
# }
# return render(request, 'accounts/dashboard.html', context)
