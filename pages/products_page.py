from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.add_to_cart_buttons = page.locator(".btn_inventory")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.sort_dropdown = page.locator(".product_sort_container")

    def is_on_products_page(self):
        return self.title.inner_text() == "Products"

    def add_first_two_products_to_cart(self):
        self.add_to_cart_buttons.nth(0).click()
        self.add_to_cart_buttons.nth(1).click()

    def go_to_cart(self):
        self.cart_icon.click()

    def sort_products(self, option):
        self.sort_dropdown.select_option(option)
