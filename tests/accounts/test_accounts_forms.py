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
        td = self.test_data.copy()
        form = RegisterForm(td)
        assert form.is_valid()

    def test_register_form_full_name_field_min_length(self):
        MIN_LEN = 3
        td = self.test_data.copy()
        td["full_name"] = "s" * (MIN_LEN - 1)
        form = RegisterForm(td)
        assert not form.is_valid()

    def test_register_form_full_name_field_max_length(self):
        MAX_LEN = 200
        td = self.test_data.copy()
        td["full_name"] = "s" * (MAX_LEN + 1)
        form = RegisterForm(td)
        assert not form.is_valid()

    def test_register_form_username_field_min_length(self):
        MIN_LEN = 4
        td = self.test_data.copy()
        td["username"] = "s" * (MIN_LEN - 1)
        form = RegisterForm(td)
        assert not form.is_valid()

    def test_register_form_username_field_max_length(self):
        MAX_LEN = 150
        td = self.test_data.copy()
        td["username"] = "s" * (MAX_LEN + 1)
        form = RegisterForm(td)
        assert not form.is_valid()

    def test_register_form_full_name_required(self):
        td = self.test_data.copy()
        del td["full_name"]
        form = RegisterForm(td)
        assert not form.is_valid()

    def test_register_form_username_required(self):
        td = self.test_data.copy()
        del td["username"]
        form = RegisterForm(td)
        assert not form.is_valid()

    def test_register_form_email_required(self):
        td = self.test_data.copy()
        del td["email"]
        form = RegisterForm(td)
        assert not form.is_valid()

    def test_register_form_password_required(self):
        td = self.test_data.copy()
        del td["password"]
        form = RegisterForm(td)
        assert not form.is_valid()

    def test_register_form_password2_required(self):
        td = self.test_data.copy()
        del td["password2"]
        form = RegisterForm(td)
        assert not form.is_valid()

    def test_register_form_password_and_password2_being_equal(self):
        td = self.test_data.copy()
        td["password"] = "1"*8
        td["password"] = "1"*9
        form = RegisterForm(td)
        assert not form.is_valid()

    def test_register_form_username_validation(self, user_factory):
        user = user_factory(username="something")
        td = self.test_data.copy()
        td["username"] = user.username
        form = RegisterForm(td)
        assert not form.is_valid()

    def test_register_form_email_validation(self, user_factory):
        user = user_factory(email="something@gmail.com")
        td = self.test_data.copy()
        td["email"] = user.email
        form = RegisterForm(td)
        assert not form.is_valid()
