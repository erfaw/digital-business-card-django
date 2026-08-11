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
        
    def test_role_field_maximum_length(self, business_card_factory):
        MAX_LENGTH = 100
        obj = business_card_factory(
            role=(MAX_LENGTH+1)*'a'
        )
        with pytest.raises(ValidationError):
            obj.full_clean()

    def test_logo_field_maximum_length(self, business_card_factory):
        MAX_LENGTH = 50
        obj = business_card_factory(
            logo_sub=(MAX_LENGTH+1)*'a'
        )
        with pytest.raises(ValidationError):
            obj.full_clean()

    def test_tag_behind_field_maximum_length(self, business_card_factory):
        MAX_LENGTH = 100
        obj = business_card_factory(
            tag_behind=(MAX_LENGTH+1)*'a'
        )
        with pytest.raises(ValidationError):
            obj.full_clean()

    def test_email_field_validation(self, business_card_factory):
        obj = business_card_factory(email="not-email-string")
        with pytest.raises(ValidationError):
            obj.full_clean()

    def test_mobile_number_field_maximum_length(self, business_card_factory):
        MAX_LENGTH = 20
        obj = business_card_factory(
            mobile_number=(MAX_LENGTH+1)*'1'
        )
        with pytest.raises(ValidationError):
            obj.full_clean()

    def test_website_field_blank_true(self, business_card_factory):
        obj = business_card_factory()
        obj.full_clean()
        assert obj.website == ""

    def test_website_preview_field_blank_true(self, business_card_factory):
        obj = business_card_factory()
        obj.full_clean()
        assert obj.website_preview == ""

    def test_website_field_url_validation(self, business_card_factory):
        obj = business_card_factory(
            website="not-url-string-123"
        )
        with pytest.raises(ValidationError):
            obj.full_clean()

    def test_linkedin_field_url_validation(self, business_card_factory):
        obj = business_card_factory(
            website="not-url-string-123"
        )
        with pytest.raises(ValidationError):
            obj.full_clean()
