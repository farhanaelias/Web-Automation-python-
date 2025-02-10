from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_add_to_cart(page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    assert products_page.is_on_products_page()

    products_page.add_first_two_products_to_cart()
    products_page.go_to_cart()

    assert "/cart.html" in page.url
