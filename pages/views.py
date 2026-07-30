from django.shortcuts import render, redirect
from pages.models import OwnerInfoModel, Contact


def index(request):
    return render(request, "pages/index.html")


def public_card(request):
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
        # TODO send mail and any kind of notification to owner here.
        return redirect("index") # TODO investigate in html for a message to show with query params

    all_records = OwnerInfoModel.objects.all().order_by("id")
    last_record = all_records.last() # TODO get record of loggen in user.
    context = {"owner": last_record}
    return render(request, "public_card.html", context=context)


def dashboard(request):
    """
    Render dashboard to manipulate details of card in GET. Create a record for OwnerInfoModel() in POST.
    """
    # TODO render dashboard with previous data (modifiable)
    # TODO use `reuquest.POST.get()` instead
    if request.method == "POST":
        new_owner = OwnerInfoModel.objects.create(
            name=request.POST["name"],
            role=request.POST["role"],
            description=request.POST["description"],
            logo_sub=request.POST["logo_sub"],
            tag_behind=request.POST["tag_behind"],
            email=request.POST["email"],
            mobile_number=request.POST["mobile_number"],
            website=request.POST["website"],
            website_preview=request.POST["website_preview"],
            linkedin=request.POST["linkedin"],
            linkedin_preview=request.POST["linkedin_preview"],
            location=request.POST["location"],
            response_time=request.POST["response_time"],
        )
        new_owner.save()
        return redirect("index")

    return render(request, "dashboard.html")
