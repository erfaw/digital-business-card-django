from django.test import Client


class TestPagesViews:
    def test_index_view_status_code(self):
        client = Client()
        response = client.get("/")
        assert response.status_code == 200

    def test_index_view_template_name(self):
        client = Client()
        response = client.get("/")
        assert "pages/index.html" in [t.name for t in response.templates]
