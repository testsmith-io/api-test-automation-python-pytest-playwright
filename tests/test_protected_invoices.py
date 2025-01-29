import pytest

@pytest.fixture
def login(api_request):
    payload = {
        "email": "customer@practicesoftwaretesting.com",
        "password": "welcome01"
    }
    response = api_request.post("https://api.practicesoftwaretesting.com/users/login", data=payload)
    assert response.status == 200, f"Unexpected status code: {response.status}"
    return response.json().get("access_token")

def test_should_retrieve_invoices_with_valid_token(api_request, login):
    token = login
    headers = {"Authorization": f"Bearer {token}"}
    response = api_request.get("https://api.practicesoftwaretesting.com/invoices", headers=headers)
    assert response.status == 200, f"Unexpected status code: {response.status}"
    data = response.json().get("data", [])
    assert len(data) >= 15, f"Expected at least 15 invoices, but got {len(data)}"
