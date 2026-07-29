from playwright.sync_api import sync_playwright

def test_mobile_view():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 375, "height": 812})
        page = context.new_page()
        page.goto("https://parabank.parasoft.com/parabank/index.htm")
        
        body_text = page.text_content("body")
        assert len(body_text) > 100, "Stránka je prázdna alebo sa nenačítala"
        page.screenshot(path="mobile_view.png")
        browser.close()

def test_tablet_view():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 768, "height": 1024})
        page = context.new_page()
        page.goto("https://parabank.parasoft.com/parabank/index.htm")
        
        body_text = page.text_content("body")
        assert len(body_text) > 100, "Stránka je prázdna alebo sa nenačítala"
        page.screenshot(path="tablet_view.png")
        browser.close()

def test_desktop_view():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()
        page.goto("https://parabank.parasoft.com/parabank/index.htm")
        
        body_text = page.text_content("body")
        assert len(body_text) > 100, "Stránka je prázdna alebo sa nenačítala"
        page.screenshot(path="desktop_view.png")
        browser.close()

def test_buttons_visible():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://parabank.parasoft.com/parabank/index.htm")
        
        # Skúsime nájsť tlačidlo podľa typu
        assert page.is_visible('input[type="submit"]'), "Tlačidlo Log In nebolo nájdené"
        browser.close()

def test_footer_present():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://parabank.parasoft.com/parabank/index.htm")
        
        content = page.text_content("body")
        assert "Parasoft" in content or "Copyright" in content, \
            "Chýba pätička alebo copyright"
        browser.close()