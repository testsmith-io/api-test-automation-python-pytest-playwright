def test_should_return_access_token_on_successful_login(api_request):
    payload = {
        "email": "customer@practicesoftwaretesting.com",
        "password": "welcome01"
    }
    response = api_request.post("https://api.practicesoftwaretesting.com/users/login", data=payload)
    assert response.status == 200, f"Unexpected status code: {response.status}"
    response_body = response.json()
    assert "access_token" in response_body, "Response does not contain 'access_token'"
