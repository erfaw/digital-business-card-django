from django.db import models
from django.db.models import CharField, TextField, EmailField, URLField
from datetime import datetime


class OwnerInfoModel(models.Model): # TODO check end-to-end and modify if needed field constraints. i guess some of them need to be changed or need to has condition in html. 
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
    # TODO good to have an avatar field to get an image.
    # TODO good to have a field for Instagram, Telegram, GitHub, Docker Hub and so on.

    def __str__(self):
        return self.name


class Contact(models.Model):
    name= models.CharField(max_length= 200)
    phone= models.CharField(max_length= 100)
    message= models.TextField(blank= True)
    contact_date= models.DateTimeField(default= datetime.now, blank= True)

    def __str__(self):
        return self.name
