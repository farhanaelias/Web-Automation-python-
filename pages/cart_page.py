
from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_badge = page.locator(".shopping_cart_badge") 
        self.add_to_cart_buttons = page.locator(".btn_inventory") 
        self.remove_buttons = page.locator(".cart_button")  
        self.cart_link = page.locator(".shopping_cart_link")  

    def add_product_to_cart(self, product_index: int):
        self.add_to_cart_buttons.nth(product_index).click()

    def remove_product_from_cart(self, product_index: int):
        self.cart_link.click()  
        self.remove_buttons.nth(product_index).click()

    def get_cart_badge_count(self):
        return self.cart_badge.inner_text()
