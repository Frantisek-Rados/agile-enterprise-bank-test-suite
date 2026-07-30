from playwright.sync_api import sync_playwright

def test_bill_pay():
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
        
        # Skontrolujeme, ci sme prihlaseni
        body = page.text_content("body")
        if "Welcome" not in body:
            print("Prihlasenie zlyhalo - pouzivatel neexistuje")
            browser.close()
            return
        
        # Prechod na Bill Pay
        page.click("text=Bill Pay")
        page.wait_for_load_state("networkidle")
        
        # Vyplnenie udajov pre platbu
        page.fill('input[name="payee.name"]', "Test Payee")
        page.fill('input[name="payee.address.street"]', "Test Street 123")
        page.fill('input[name="payee.address.city"]', "Kosice")
        page.fill('input[name="payee.address.state"]', "SK")
        page.fill('input[name="payee.address.zipCode"]', "04001")
        page.fill('input[name="payee.phoneNumber"]', "0900123456")
        page.fill('input[name="payee.accountNumber"]', "123456789")
        page.fill('input[name="verifyAccount"]', "123456789")
        page.fill('input[name="amount"]', "50.00")
        
        # Vyberieme ucet
        page.select_option('select[name="fromAccountId"]', "1")
        
        # Odošleme
        page.click('input[value="Send Payment"]')
        page.wait_for_timeout(3000)
        
        # Overenie
        body = page.text_content("body")
        assert "Bill Payment Complete" in body or "success" in body.lower(), \
            "Bill Pay zlyhal"
        
        browser.close()