def test_should_retrieve_at_least_two_brands(api_request):
    response = api_request.get("https://api.practicesoftwaretesting.com/brands")
    assert response.status == 200, f"Unexpected status code: {response.status}"
    data = response.json()
    assert len(data) >= 2, f"Expected at least 2 brands, but got {len(data)}"
