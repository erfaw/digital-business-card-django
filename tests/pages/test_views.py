from django.test import Client


class TestPagesViews:
    def test_index_view_status_code(self):
        client = Client()
        response = client.get("/")
        assert response.status_code == 200
