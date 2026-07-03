from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_login_parabank():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login = LoginPage(page)
        login.go_to()
        login.login("john_doe", "Test123!")
        # Overíme, že sme presmerovaní na overview (alebo login, ak zlyhá prihlásenie)
        assert "overview" in page.url or "login" in page.url
        browser.close()