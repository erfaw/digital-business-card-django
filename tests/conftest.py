from pytest_factoryboy import register
from .factories import BusinessCardFactory, UserFactory, ContactFactory


register(BusinessCardFactory)
register(UserFactory)
register(ContactFactory)
