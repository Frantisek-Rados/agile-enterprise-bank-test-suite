from playwright.sync_api import sync_playwright
import time

def test_registration_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://parabank.parasoft.com/parabank/register.htm")
        
        page.wait_for_load_state("networkidle")
        
        unique_username = f"jan_{int(time.time())}"
        
        page.fill('input[name="customer.firstName"]', "Jan")
        page.fill('input[name="customer.lastName"]', "Novak")
        page.fill('input[name="customer.address.street"]', "Hlavna 123")
        page.fill('input[name="customer.address.city"]', "Kosice")
        page.fill('input[name="customer.address.state"]', "SK")
        page.fill('input[name="customer.address.zipCode"]', "04001")
        page.fill('input[name="customer.phoneNumber"]', "0900123456")
        page.fill('input[name="customer.ssn"]', "123-45-6789")
        page.fill('input[name="customer.username"]', unique_username)
        page.fill('input[name="customer.password"]', "Test123!")
        page.fill('input[name="repeatedPassword"]', "Test123!")
        
        page.click('input[value="Register"]')
        
        page.wait_for_timeout(3000)
        
        # Skontrolujeme obsah stranky
        body_text = page.text_content("body")
        assert "Your account was created successfully" in body_text, \
            "Registracia zlyhala – chyba sprava 'Your account was created successfully'"
        
        browser.close()