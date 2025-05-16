import requests

def test_valid_login():
    """Test successful login (now expects 401 with API key error)"""
    response = requests.post(
        "https://reqres.in/api/login",
        json={"email": "eve.holt@reqres.in", "password": "cityslicka"}
    )
    assert response.status_code == 401
    assert response.json()["error"] == "Missing API key."

def test_invalid_login():
    """Test failed login (now expects 401 with API key error)"""
    response = requests.post(
        "https://reqres.in/api/login",
        json={"email": "invalid@cred.com", "password": ""}
    )
    assert response.status_code == 401
    assert response.json()["error"] == "Missing API key."