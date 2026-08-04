from playwright.sync_api import sync_playwright

def test_sql_injection_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://parabank.parasoft.com/parabank/index.htm")
        page.wait_for_load_state("networkidle")

        # SQL injection do pola username
        page.fill('input[name="username"]', "' OR '1'='1")
        page.fill('input[name="password"]', "' OR '1'='1")
        page.click('input[value="Log In"]')
        page.wait_for_timeout(2000)

        # Skontrolujeme, ci sme neboli prihlaseni
        url = page.url
        body = page.text_content("body")

        # Ak sme na inej stranke, moze to znamenat SQL injection
        if "overview" in url or "Welcome" in body:
            print("BUG: SQL injection funguje – prihlasenie bez spravnych udajov")
            # Test prejde, ale zaznamename BUG
            assert False, "SQL injection je mozna – bezpecnostna chyba"
        else:
            assert True

        browser.close()

def test_xss_in_registration():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://parabank.parasoft.com/parabank/register.htm")
        page.wait_for_load_state("networkidle")

        # XSS vklad do pola First Name
        xss_payload = "<script>alert('XSS')</script>"
        page.fill('input[name="customer.firstName"]', xss_payload)
        page.fill('input[name="customer.lastName"]', "Test")
        page.fill('input[name="customer.address.street"]', "Test 123")
        page.fill('input[name="customer.address.city"]', "Kosice")
        page.fill('input[name="customer.address.state"]', "SK")
        page.fill('input[name="customer.address.zipCode"]', "04001")
        page.fill('input[name="customer.phoneNumber"]', "0900123456")
        page.fill('input[name="customer.ssn"]', "123-45-6789")
        page.fill('input[name="customer.username"]', "xss_test")
        page.fill('input[name="customer.password"]', "Test123!")
        page.fill('input[name="repeatedPassword"]', "Test123!")
        page.click('input[value="Register"]')
        page.wait_for_timeout(2000)

        # Skontrolujeme, ci sa script spustil (napr. ci sa zobrazil alert)
        # Playwright nezachytava JS dialogy automaticky, ale mozeme skontrolovat HTML
        body = page.text_content("body")
        if "<script>" in body or "alert" in body:
            print("BUG: XSS je mozny – script sa vlozil do stranky")
            assert False, "XSS je mozny – bezpecnostna chyba"
        else:
            assert True

        browser.close()