import pytest
from django.urls import reverse
from django.test import Client

pytestmark = pytest.mark.django_db


class TestRegisterView:
    def test_status_code(self):
        c = Client()
        response = c.get(reverse("register"))
        assert response.status_code == 200

    # TODO (HIGH) write test for all aspects of register
    # TODO (HIGH) test for login
    # TODO (HIGH) test for logout