import pytest
from django.test import Client


pytestmark = pytest.mark.django_db


class TestPagesViews:
    def test_index_view_status_code(self):
        client = Client()
        response = client.get("/")
        assert response.status_code == 200

    def test_index_view_template_name(self):
        client = Client()
        response = client.get("/")
        assert "pages/index.html" in [t.name for t in response.templates]

    def test_public_card_view_new_contact_on_post(self, user_factory, business_card_factory):
        user = user_factory()
        bc = business_card_factory(user=user)
        client = Client()
        params = {
            "name": "test-name",
            "mobile_number": 20*"1",
            "message": "test_message"
        }
        response = client.post(f"/u/{user.username}/", params)
        assert response.status_code == 302
        response = client.post(f"/u/{user.username}/", params, follow=True)
        assert response.status_code == 200

    def test_dashboard_view_login_required(self):
        c = Client()
        response = c.get("/dashboard/")
        assert response.status_code == 302
        assert response.url == "/accounts/login/?next=/dashboard/" # type: ignore
