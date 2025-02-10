import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout(page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    # Step 1: Login
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Step 2: Add products to the cart and navigate to the cart
    products_page.add_first_two_products_to_cart()
    products_page.go_to_cart()

    # Step 3: Proceed to checkout
    cart_page.proceed_to_checkout()

    # Step 4: Enter checkout information and complete checkout
    checkout_page.enter_checkout_info("John", "Doe", "12345")
    checkout_page.complete_checkout()

    # Step 5: Verify successful checkout
    assert checkout_page.get_confirmation_message().lower() == "thank you for your order!".lower()
