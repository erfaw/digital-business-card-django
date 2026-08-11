import factory
from factory.declarations import SubFactory, Sequence
from pages.models import BusinessCard, Contact
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = Sequence(lambda n: f"test-{n}-user")


class BusinessCardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BusinessCard

    name = Sequence(lambda n: f"test{n} test{n}i")
    role = "test_role"
    logo_sub = "test_logo_sub"
    description = "test_description"
    tag_behind = "test_tag_behind"
    mobile_number = "+989000000000"
    email = Sequence(lambda n: f"test_{n}_user@gmail.com")
    user = SubFactory(UserFactory)


class ContactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=Contact

    name = Sequence(lambda n: f"test_name_{n}")
    mobile_number = Sequence(lambda n: f"test_mobile_number_{n}")
    user = SubFactory(UserFactory)
