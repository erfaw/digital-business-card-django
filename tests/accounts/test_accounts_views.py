import pytest
from django.urls import reverse
from django.test import Client

pytestmark = pytest.mark.django_db


class TestAccountsViews:
    def test_register_view_status_code(self):
        c = Client()
        response = c.get(reverse("register"))
        assert response.status_code == 200
