import pytest
from accounts.forms import RegisterForm

pytestmark = pytest.mark.django_db


class TestAccountsForms:
    test_data = {
        "full_name": "test testi",
        "username": "test_testi",
        "email": "test@gmail.com",
        "password": "123456789",
        "password2": "123456789",
    }

    def test_register_form_is_valid(self):
        td = self.test_data
        form = RegisterForm(td)
        assert form.is_valid()

    def test_register_form_full_name_field_min_length(self):
        MIN_LEN = 3
        td = self.test_data
        td["full_name"] = "s" * (MIN_LEN - 1)
        form = RegisterForm(td)
        with pytest.raises(AssertionError):
            assert form.is_valid()
