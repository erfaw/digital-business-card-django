import pytest
from accounts.forms import RegisterForm

pytestmark = pytest.mark.django_db


class TestAccountsForms:
    def test_register_form_is_valid(self, login_form):
        test_data = {
            "full_name": "test testi",
            "username": "test_testi",
            "email": "test@gmail.com",
            "password": "123456789",
            "password2": "123456789",
        }
        form = RegisterForm(test_data)
        assert form.is_valid()
