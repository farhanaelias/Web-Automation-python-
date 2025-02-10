import pytest
from pages.login_page import LoginPage

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("wrong_user", "secret_sauce")
    assert "Username and password do not match" in login_page.get_error_message()
