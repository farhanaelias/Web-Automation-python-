from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage

def test_logout(page):
    # Initialize the page objects
    login_page = LoginPage(page)
    logout_page = LogoutPage(page)

    # Step 1: Navigate to login page and log in with valid credentials
    login_page.navigate()
    login_page.login('standard_user', 'secret_sauce')

    # Step 2: Perform logout
    logout_page.logout()

    # Step 3: Verify that the user is redirected to the login page
    assert page.url == "https://www.saucedemo.com/"
    assert login_page.username_input.is_visible()  # Check if the username input is visible (indicating we're on the login page)
