from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("u/<str:username>/", views.public_card, name="public_card"),
    path("u/<str:username>/qr/", views.qr, name="qr"),
]

