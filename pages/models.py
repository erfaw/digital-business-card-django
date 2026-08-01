from django.db import models
from django.db.models import CharField, TextField, EmailField, URLField, OneToOneField
from django.contrib.auth.models import User
from datetime import datetime


class BusinessCard(models.Model):
    name = CharField(max_length=50)
    role = CharField(max_length=100)
    description = TextField()
    logo_sub = CharField(max_length=50)
    tag_behind = CharField(max_length=100)
    email = EmailField()
    mobile_number = CharField(max_length=20)
    website = URLField(blank=True)
    website_preview = CharField(blank=True)
    linkedin = URLField(blank=True)
    linkedin_preview = CharField(blank=True)
    location = CharField(blank=True)
    response_time = CharField(blank=True)
    user = OneToOneField(User, on_delete=models.CASCADE, related_name="business_card")
    # TODO good to have an avatar field to get an image.
    # TODO good to have a field for Instagram, Telegram, GitHub, Docker Hub and so on.

    def __str__(self):
        return self.name


class Contact(models.Model):
    name= models.CharField(max_length= 200)
    mobile_number= models.CharField(max_length= 100)
    message= models.TextField(blank= True)
    contact_date= models.DateTimeField(default= datetime.now, blank= True)
    # TODO connect to user

    def __str__(self):
        return self.name
