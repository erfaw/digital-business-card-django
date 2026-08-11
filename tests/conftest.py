from pytest_factoryboy import register
from .factories import BusinessCardFactory, UserFactory


register(BusinessCardFactory)
register(UserFactory)
