import factory
from pages.models import BusinessCard


class BusinessCardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BusinessCard

    name = "test_name"
