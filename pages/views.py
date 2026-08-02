from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from qrcode import QRCode, constants
from io import BytesIO
from pages.models import Contact


def index(request):
    """
    Render Home page as simple as it is.

    Returns:
        HttpResponse
    """
    return render(request, "pages/index.html")


def public_card(request, username):
    """
    Render actual digital business card in GET. Create a record for Contact() in POST.

    - GET :
        Get user by username from db then act on user.business_card. increase business_card.view_count by 1 each time.
    - POST :
        Get user by username from db then make a new Contact and attach to user. push a success message to render.

    Args:
        username(str): get automatically from url

    Returns:
        - GET: HttpResponse
        - POST: HttpResponseRedirect
    """

    if request.method == "POST": # TODO make a separate view and endpoint for making contacts.
        user = get_object_or_404(User, username=username)
        new_contact = Contact.objects.create(
            name=request.POST.get("name"),
            mobile_number=request.POST.get("mobile_number"),
            message=request.POST.get("message"),
            user=user,
        )
        new_contact.save()
        messages.success(request, "Thanks! We'll get back to you soon.")
        # TODO send mail and any kind of notification to owner here.
        return redirect("public_card", username=username)

    user = get_object_or_404(User, username=username)
    bc = user.business_card # type: ignore
    context = {"owner_card": bc} 
    bc.view_count += 1 
    bc.save()
    return render(request, "pages/public_card.html", context)


@login_required
def dashboard(request):
    """
    Render dashboard. decorate with login_required.
    
    - GET :
        Prepare form to manipulate details of card and make POST for modify it. form prepared by front-end.
    - POST :
        Modify record for user.business_card from data submitted.

    Returns:
        - GET: HttpResponse
        - POST: HttpResponseRedirect
    """
    if request.method == "POST":
        user_bc = request.user.business_card

        user_bc.name=request.POST.get("name") # TODO try to do it dynamic, with getattr and for loop
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
    return render(request, "pages/dashboard.html")

def qr(request, username):
    """
    Makes a QR Code with `qrcode`_ library based on public_card endpoint for username. buffer and send it as result.

    Args:
        username(str): get automatically from url

    Returns:
        HttpResponse

    .. _qrcode: https://pypi.org/project/qrcode/
    """

    url_to_card = request.build_absolute_uri(reverse("public_card", kwargs={"username": username}))

    qr_code = QRCode(version=1, error_correction=constants.ERROR_CORRECT_L,  border=2)
    qr_code.add_data(url_to_card)
    qr_code.make(fit=True)

    qr_code_image = qr_code.make_image(fill_color="white", back_color=(5, 17, 38))

    buffer = BytesIO()
    qr_code_image.save(buffer, "PNG")

    return HttpResponse(buffer.getvalue(), content_type="image/png")
