from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = self.page.locator("input[data-test='firstName']")
        self.last_name_input = self.page.locator("input[data-test='lastName']")
        self.postal_code_input = self.page.locator("input[data-test='postalCode']")
        self.continue_button = self.page.locator("input[data-test='continue']")
        self.finish_button = self.page.locator("button[data-test='finish']")
    
    def enter_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        """Fills out the checkout information and clicks continue."""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    def complete_checkout(self):
        """Click the finish button to complete checkout."""
        self.finish_button.click()

    def get_confirmation_message(self):
        """Retrieve the confirmation message after checkout."""
        return self.page.locator(".complete-header").inner_text()
