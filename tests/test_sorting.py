
import pytest
from pages.login_page import LoginPage
from pages.sorting_page import SortingPage

def test_sorting_products(page):
    login_page = LoginPage(page)
    sorting_page = SortingPage(page)

    # Step 1: Login
    login_page.navigate()
    login_page.login('standard_user', 'secret_sauce')

    # Step 2: Verify sorting by Price (low to high)
    sorting_page.select_sort_option("Price (low to high)")
    prices = sorting_page.get_product_prices()
    assert prices == sorted(prices), "Prices are not sorted from low to high"

    # Step 3: Verify sorting by Price (high to low)
    sorting_page.select_sort_option("Price (high to low)")
    prices = sorting_page.get_product_prices()
    assert prices == sorted(prices, reverse=True), "Prices are not sorted from high to low"

    # Step 4: Verify sorting by Name (A to Z)
    sorting_page.select_sort_option("Name (A to Z)")
    names = sorting_page.get_product_names()
    assert names == sorted(names), "Names are not sorted from A to Z"

    # Step 5: Verify sorting by Name (Z to A)
    sorting_page.select_sort_option("Name (Z to A)")
    names = sorting_page.get_product_names()
    assert names == sorted(names, reverse=True), "Names are not sorted from Z to A"
