import pytest
from django.core.exceptions import ValidationError


pytestmark = pytest.mark.django_db


class TestBusinessCardModel:
    def test_dunder_str(self, business_card_factory):
        unit = business_card_factory()
        assert unit.__str__() == unit.name

    def test_name_field_maximum_length(self, business_card_factory):
        MAX_LENGTH = 50
        obj = business_card_factory(
            name=(MAX_LENGTH+1)*'a'
        )
        with pytest.raises(ValidationError):
            obj.full_clean()
        

