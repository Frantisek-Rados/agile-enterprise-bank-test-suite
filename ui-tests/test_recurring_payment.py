from playwright.sync_api import sync_playwright

def test_recurring_payment():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Prihlasenie s existujucim pouzivatelom
        page.goto("https://parabank.parasoft.com/parabank/index.htm")
        page.wait_for_load_state("networkidle")
        page.fill('input[name="username"]', "john_doe")
        page.fill('input[name="password"]', "Test123!")
        page.click('input[value="Log In"]')
        page.wait_for_load_state("networkidle")

        # Kontrola prihlasenia
        body = page.text_content("body")
        if "Welcome" not in body:
            print("Prihlasenie zlyhalo - pouzivatel neexistuje")
            browser.close()
            return

        # Bill Pay
        page.click("text=Bill Pay")
        page.wait_for_load_state("networkidle")

        # Vyplnenie
        page.fill('input[name="payee.name"]', "Monthly Rent")
        page.fill('input[name="payee.address.street"]', "Rent Street 1")
        page.fill('input[name="payee.address.city"]', "Kosice")
        page.fill('input[name="payee.address.state"]', "SK")
        page.fill('input[name="payee.address.zipCode"]', "04001")
        page.fill('input[name="payee.phoneNumber"]', "0900111222")
        page.fill('input[name="payee.accountNumber"]', "987654321")
        page.fill('input[name="verifyAccount"]', "987654321")
        page.fill('input[name="amount"]', "300.00")
        page.select_option('select[name="fromAccountId"]', "1")
        page.click('input[value="Send Payment"]')

        page.wait_for_timeout(3000)

        body = page.text_content("body")
        assert "Bill Payment Complete" in body or "success" in body.lower(), \
            "Pravidelna platba zlyhala"

        browser.close()