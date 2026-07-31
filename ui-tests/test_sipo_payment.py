from playwright.sync_api import sync_playwright

def test_sipo_payment():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Prihlasenie
        page.goto("https://parabank.parasoft.com/parabank/index.htm")
        page.wait_for_load_state("networkidle")
        page.fill('input[name="username"]', "john_doe")
        page.fill('input[name="password"]', "Test123!")
        page.click('input[value="Log In"]')
        page.wait_for_load_state("networkidle")

        # Kontrola prihlasenia
        body = page.text_content("body")
        if "Welcome" not in body:
            print("Prihlasenie zlyhalo")
            browser.close()
            return

        # 1. Platba prvej faktury
        page.click("text=Bill Pay")
        page.wait_for_load_state("networkidle")

        page.fill('input[name="payee.name"]', "Electricity")
        page.fill('input[name="payee.address.street"]', "Elm Street 1")
        page.fill('input[name="payee.address.city"]', "Kosice")
        page.fill('input[name="payee.address.state"]', "SK")
        page.fill('input[name="payee.address.zipCode"]', "04001")
        page.fill('input[name="payee.phoneNumber"]', "0900111223")
        page.fill('input[name="payee.accountNumber"]', "111222333")
        page.fill('input[name="verifyAccount"]', "111222333")
        page.fill('input[name="amount"]', "45.00")
        page.select_option('select[name="fromAccountId"]', "1")
        page.click('input[value="Send Payment"]')
        page.wait_for_timeout(2000)

        # 2. Platba druhej faktury
        page.click("text=Bill Pay")
        page.wait_for_load_state("networkidle")

        page.fill('input[name="payee.name"]', "Gas")
        page.fill('input[name="payee.address.street"]', "Gas Street 2")
        page.fill('input[name="payee.address.city"]', "Kosice")
        page.fill('input[name="payee.address.state"]', "SK")
        page.fill('input[name="payee.address.zipCode"]', "04001")
        page.fill('input[name="payee.phoneNumber"]', "0900111224")
        page.fill('input[name="payee.accountNumber"]', "444555666")
        page.fill('input[name="verifyAccount"]', "444555666")
        page.fill('input[name="amount"]', "60.00")
        page.select_option('select[name="fromAccountId"]', "1")
        page.click('input[value="Send Payment"]')
        page.wait_for_timeout(2000)

        # Overenie
        body = page.text_content("body")
        assert "Bill Payment Complete" in body or "success" in body.lower(), \
            "SIPO platba zlyhala"

        browser.close()