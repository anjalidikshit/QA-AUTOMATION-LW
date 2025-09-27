from playwright.sync_api import sync_playwright

def test_login_automation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)  # headless=False shows the browser
        page = browser.new_page()

        # Go to the login page
        page.goto("https://www.lathamalumni.com/login/login.aspx")

        page.wait_for_selector('xpath=//*[@id="LoginBox_LoginEmailAddress"]', timeout=5000)

        # Fill email using XPath
        page.fill('xpath=//*[@id="LoginBox_LoginEmailAddress"]', "testuser")

        # Fill password (still using name selector or XPath)
        page.fill('input[name="LoginBox$LoginPassword"]', "password123")


        # Click the login button 
        page.click('input[type="submit"]')

        try:
            # Wait for some post-login element (adjust based on what appears after login)
            page.wait_for_selector("text=Dashboard", timeout=5000)
            print("✅ Login successful!")
        except:
            print("❌ Login failed or Dashboard not found.")

        browser.close()

