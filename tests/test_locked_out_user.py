from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_locked_out_user(page):
    login_page = LoginPage(page)

    # Step 1: Navigate to login page
    login_page.navigate()

    # Step 2: Log in with locked-out user credentials
    login_page.login('locked_out_user', 'secret_sauce')

    # Step 3: Verify that the locked-out user error message is displayed
    error_message = login_page.get_error_message()
    assert error_message == "Sorry, this user has been locked out."
