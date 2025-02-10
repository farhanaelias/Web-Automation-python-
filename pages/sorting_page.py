
from playwright.sync_api import Page

class SortingPage:
    def __init__(self, page: Page):
        self.page = page
        self.sort_dropdown = page.locator("select.product_sort_container[data-test='product-sort-container']") 
        self.products = page.locator(".inventory_item_price")  

    def select_sort_option(self, option: str):
        self.sort_dropdown.select_option(label=option)

    def get_product_prices(self):
        prices = self.products.all()
        return [float(price.inner_text().strip('$')) for price in prices]
    
    def get_product_names(self):
        product_names = self.page.locator(".inventory_item_name")
        return [name.inner_text() for name in product_names.all()]
