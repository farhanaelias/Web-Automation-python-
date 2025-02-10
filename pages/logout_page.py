from playwright.sync_api import Page

class LogoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.hamburger_menu = page.locator("#react-burger-menu-btn")  
        self.logout_button = page.locator("#logout_sidebar_link")  

    def logout(self):
        self.hamburger_menu.click()  
        self.logout_button.click()   