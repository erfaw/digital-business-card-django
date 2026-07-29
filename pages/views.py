from django.shortcuts import render, redirect
from pages.models import OwnerInfoModel

def index(request):
    """
    Render actual digital business card.
    """
    return render(request, "index.html")

def dashboard(request):
    """
    Render dashboard to manipulate details of card.
    """
    if request.method == "POST":
        new_owner = OwnerInfoModel.objects.create(
            name=request.POST['name'],
            role=request.POST['role'],
            description=request.POST['description'],
            logo_sub=request.POST['logo_sub'],
            tag_behind=request.POST['tag_behind'],
            email=request.POST['email'],
            mobile_number=request.POST['mobile_number'],
            website=request.POST['website'],
            website_preview=request.POST['website_preview'],
            linkedin=request.POST['linkedin'],
            linkedin_preview=request.POST['linkedin_preview'],
            location=request.POST['location'],
            response_time=request.POST['response_time'],
        )
        new_owner.save()
        return redirect('index')

    return render(request, "dashboard.html")
