from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("u/public_card", views.public_card, name="public_card"), # TODO make it dynamic to Card.slug
]

