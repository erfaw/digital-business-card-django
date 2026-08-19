import pytest
from django.urls import reverse
from django.test import Client

pytestmark = pytest.mark.django_db


class TestRegisterView:
    def test_get_request_status_code(self):
        c = Client()
        response = c.get(reverse("register"))
        assert response.status_code == 200

    def test_user_registration_on_post(self, user_factory, business_card_factory):
        user_class = user_factory().__class__
        business_card_class = business_card_factory().__class__
        c = Client()
        params = {
            "full_name": "test testi",
            "username": "test_testi",
            "email": "test@gmail.com",
            "password": "1"*8,
            "password2": "1"*8, # TODO (MID) add token to test_user_registration_on_post() and figure out failure.
        }
        response = c.post(
            reverse("register"), 
            params,
        )
        assert response.status_code == 302
        assert (
            user_class.objects
            .filter(username=params["username"])
            .exists()
        )
        assert (
            user_class.objects
            .filter(username=params["username"])
            .exists()
        )
        made_user = user_class.objects.get(username=params["username"])
        assert not made_user == None
        made_user.refresh_from_db()
        assert isinstance(
            made_user.business_card,
            business_card_class
        ) 


class TestLoginView:
    def test_get_request_status_code(self):
        c = Client()
        response = c.get(reverse("login"))
        assert response.status_code == 200

    def test_user_login_on_post(self, user_factory):
        paswrd="1"*8
        user = user_factory(
            username="test_username_for_login",
            password=paswrd
        )

        c = Client()
        params = {
            "username": user.username,
            "password": paswrd,
        }
        response = c.post(
            reverse("login"), 
            params,
        )
        assert response.status_code == 302
        assert response.wsgi_request.user.is_authenticated
        assert response.wsgi_request.user == user

    def test_invalid_credentials(self):
        c = Client()
        params = {
            "username": "invalid_credentials",
            "password": "invalid-credentials",
        }
        response = c.post(
            reverse("login"),
            params,
        )
        assert response.status_code == 302
        assert response.url == reverse("login") # type: ignore
        assert not response.wsgi_request.user.is_authenticated


def test_logout_view_login_required():
    c = Client()
    response = c.post(reverse("logout"))
    assert response.status_code == 302
    assert response.url == f"{reverse("login")}?next={reverse("logout")}" # type: ignore
