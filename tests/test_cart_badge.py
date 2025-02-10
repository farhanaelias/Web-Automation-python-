
import pytest
from pages.login_page import LoginPage
from pages.cart_page import CartPage

def test_cart_badge_count(page):
    login_page = LoginPage(page)
    cart_page = CartPage(page)

    # Step 1: Login
    login_page.navigate()
    login_page.login('standard_user', 'secret_sauce')

    # Step 2: Add products to the cart
    cart_page.add_product_to_cart(0)  # Add the first product to the cart
    cart_page.add_product_to_cart(1)  # Add the second product to the cart

    # Step 3: Verify the cart badge count
    badge_count = cart_page.get_cart_badge_count()
    assert badge_count == "2", f"Expected cart badge count to be '2', but got '{badge_count}'"

    # Step 4: Remove an item from the cart
    cart_page.remove_product_from_cart(0)  # Remove the first product

    # Step 5: Verify the cart badge count updates correctly
    badge_count = cart_page.get_cart_badge_count()
    assert badge_count == "1", f"Expected cart badge count to be '1', but got '{badge_count}'"
