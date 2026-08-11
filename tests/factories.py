import factory
from factory.declarations import SubFactory
from pages.models import BusinessCard
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User


class BusinessCardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BusinessCard

    name = "test_name"
    user = SubFactory(UserFactory)
