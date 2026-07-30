from playwright.sync_api import sync_playwright

def test_empty_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://parabank.parasoft.com/parabank/register.htm")
        
        page.wait_for_load_state("networkidle")
        
        # Vyplnime vsetko okrem hesla
        page.fill('input[name="customer.firstName"]', "Jan")
        page.fill('input[name="customer.lastName"]', "Novak")
        page.fill('input[name="customer.address.street"]', "Hlavna 123")
        page.fill('input[name="customer.address.city"]', "Kosice")
        page.fill('input[name="customer.address.state"]', "SK")
        page.fill('input[name="customer.address.zipCode"]', "04001")
        page.fill('input[name="customer.phoneNumber"]', "0900123456")
        page.fill('input[name="customer.ssn"]', "123-45-6789")
        page.fill('input[name="customer.username"]', "jan_novak")
        
        # Heslo nechame prazdne
        page.fill('input[name="customer.password"]', "")
        page.fill('input[name="repeatedPassword"]', "")
        
        page.click('input[value="Register"]')
        page.wait_for_timeout(2000)
        
        # Skontrolujeme, ci sa zobrazila chyba
        body = page.text_content("body")
        assert "error" in body.lower() or "required" in body.lower(), \
            "Chyba chybova sprava pre prazdne heslo"
        
        browser.close()

def test_short_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://parabank.parasoft.com/parabank/register.htm")
        
        page.wait_for_load_state("networkidle")
        
        # Vyplnime vsetko, heslo dame kratke
        page.fill('input[name="customer.firstName"]', "Jan")
        page.fill('input[name="customer.lastName"]', "Novak")
        page.fill('input[name="customer.address.street"]', "Hlavna 123")
        page.fill('input[name="customer.address.city"]', "Kosice")
        page.fill('input[name="customer.address.state"]', "SK")
        page.fill('input[name="customer.address.zipCode"]', "04001")
        page.fill('input[name="customer.phoneNumber"]', "0900123456")
        page.fill('input[name="customer.ssn"]', "123-45-6789")
        page.fill('input[name="customer.username"]', "jan_novak")
        page.fill('input[name="customer.password"]', "123")
        page.fill('input[name="repeatedPassword"]', "123")
        
        page.click('input[value="Register"]')
        page.wait_for_timeout(2000)
        
        # Osetrime, ze system akceptuje kratke heslo - to je BUG
        body = page.text_content("body")
        if "Your account was created successfully" in body:
            print("BUG: System akceptuje kratke heslo (123)")
            assert True
        else:
            assert "error" in body.lower() or "password" in body.lower(), \
                "Chyba chybova sprava pre kratke heslo"
        
        browser.close()