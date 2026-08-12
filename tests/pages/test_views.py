import pytest
from django.test import Client
from django.urls import reverse


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

    def test_dashboard_view_modify_card_on_post(self, user_factory, business_card_factory):
        user = user_factory(password="12345678")
        card = business_card_factory(user=user)

        c = Client()
        c.force_login(user)
        params = {}
        for f in card._meta.fields:
            if not f.name in ["id", "view_count", "user"]:
                field_name = f.name
                field_value = f"modify-test-{field_name}"
                params[field_name] = field_value

        response = c.post(reverse("dashboard"), params)
        assert response.status_code == 302

        card.refresh_from_db()
        for f in card._meta.fields:
            if not f.name in ["id", "view_count", "user"]:
                assert getattr(card, f.name).startswith("modify-test")

    # TODO (HIGH) test changing record in post request at dashboard
    # TODO (HIGH) build test qr and contact view