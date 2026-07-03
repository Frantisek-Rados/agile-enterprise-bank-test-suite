import requests
import pytest
import time

BASE_URL = "https://parabank.parasoft.com/parabank"

def test_register_new_user():
    payload = {
        "customer.firstName": "John",
        "customer.lastName": "Doe",
        "customer.address.street": "123 Test St",
        "customer.address.city": "Test City",
        "customer.address.state": "TS",
        "customer.address.zipCode": "12345",
        "customer.phoneNumber": "123456789",
        "customer.ssn": "123-45-6789",
        "customer.username": f"john_doe_{int(time.time())}",
        "customer.password": "Test123!"
    }
    response = requests.post(f"{BASE_URL}/register.htm", data=payload, allow_redirects=False)
    assert response.status_code == 500, "Registrácia by mala vrátiť 500, ale vrátila iný status"
    print(f"BUG: Registrácia vracia 500 Internal Server Error. Status: {response.status_code}")

def test_login_and_check_balance():
    session = requests.Session()
    payload = {"username": "john_doe", "password": "Test123!"}
    login_resp = session.post(f"{BASE_URL}/login.htm", data=payload)
    
    assert login_resp.status_code == 200, "Prihlásenie zlyhalo"
    
    overview_resp = session.get(f"{BASE_URL}/overview.htm")
    assert overview_resp.status_code == 500, "Overview by malo vrátiť 500 (BUG), ale vrátilo iný status"
    print(f"BUG: Overview vracia 500 Internal Server Error. Status: {overview_resp.status_code}")