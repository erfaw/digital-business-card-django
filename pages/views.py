from django.shortcuts import render

def index(request):
    """
    Render actual digital business card.
    """
    return render(request, "index.html")

def dashboard(request):
    """
    Render dashboard to manipulate details of card.
    """
    return render(request, "dashboard.html")
