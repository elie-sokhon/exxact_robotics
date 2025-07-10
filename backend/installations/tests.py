import pytest
from django.urls import reverse
from installations.models import Installation

@pytest.mark.django_db
def test_installation_list(client):
    url = reverse("installation-list")
    response = client.get(url)
    assert response.status_code == 200
