from playwright.sync_api import sync_playwright

def test_transfer_funds():
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
            print("Prihlasenie zlyhalo - pouzivatel john_doe neexistuje")
            print("Skus pouzit ine meno")
            browser.close()
            return
        
        # Transfer Funds
        page.click("text=Transfer Funds")
        page.wait_for_load_state("networkidle")
        
        # Vyberieme ucet
        page.select_option('select[name="fromAccountId"]', "1")
        page.select_option('select[name="toAccountId"]', "2")
        page.fill('input[name="amount"]', "10.00")
        page.click('input[value="Transfer"]')
        
        page.wait_for_timeout(3000)
        
        body = page.text_content("body")
        assert "Transfer Complete" in body or "success" in body.lower(), \
            "Transfer zlyhal"
        
        browser.close()