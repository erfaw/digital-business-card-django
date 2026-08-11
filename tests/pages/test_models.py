import pytest


pytestmark = pytest.mark.django_db


class TestBusinessCardModel:
    def test_dunder_str(self, business_card_factory):
        unit = business_card_factory()
        assert unit.__str__() == "test_name"