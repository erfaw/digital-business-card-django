from django.db import models
from django.db.models import CharField, TextField, EmailField, URLField


class OwnerInfoModel(models.Model):
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

    def __str__(self):
        return self.name
