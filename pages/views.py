from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from pages.models import Contact


def index(request):
    return render(request, "pages/index.html")


def public_card(request, username):
    """
    Render actual digital business card in GET. Create a record for Contact() in POST.
    """
    if request.method == "POST":
        new_contact = Contact.objects.create(
            name=request.POST.get("name"),
            mobile_number=request.POST.get("mobile_number"),
            message=request.POST.get("message"),
        )
        new_contact.save()
        messages.success(request, "Thanks! We'll get back to you soon.")
        # TODO send mail and any kind of notification to owner here.
        return redirect("public_card")

    user = get_object_or_404(User, username=username)
    context = {"owner": user.business_card} # type: ignore
    return render(request, "public_card.html", context)


# TODO make dashboard login required
def dashboard(request):
    """
    Render dashboard to manipulate details of card in GET. Create a record for BusinessCard() in POST.
    """
    # TODO render dashboard with previous data (modifiable)
    if request.method == "POST":
        user_bc = request.user.business_card

        user_bc.name=request.POST.get("name")
        user_bc.role=request.POST.get("role")
        user_bc.description=request.POST.get("description")
        user_bc.logo_sub=request.POST.get("logo_sub")
        user_bc.tag_behind=request.POST.get("tag_behind")
        user_bc.email=request.POST.get("email")
        user_bc.mobile_number=request.POST.get("mobile_number")
        user_bc.website=request.POST.get("website")
        user_bc.website_preview=request.POST.get("website_preview")
        user_bc.linkedin=request.POST.get("linkedin")
        user_bc.linkedin_preview=request.POST.get("linkedin_preview")
        user_bc.location=request.POST.get("location")
        user_bc.response_time=request.POST.get("response_time")

        user_bc.save()
        messages.success(request, "Your card fields updated successfully.")
        return redirect("dashboard")

    return render(request, "dashboard.html") # TODO render with existing data of logged in user
