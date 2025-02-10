# 🏆 Web Automation Testing with Playwright & Python

This project automates UI testing for the **SauceDemo** (https://www.saucedemo.com/) website using **Playwright and Python**. It verifies key functionalities such as login, sorting, adding to the cart, checkout, logout, and handling locked-out users. The automation follows the **Page Object Model (POM)** for better code organization and maintainability.

---

## 📌 **Project Features**
✅ Automated UI testing using **Playwright**  
✅ Implemented **Page Object Model (POM)** for cleaner code  
✅ Validations for **sorting products, cart badge, and checkout**  
✅ **Error handling & assertions** to ensure test reliability  
✅ **GitHub integration** for version control and collaboration  

---

## 🛠 **Tech Stack**
- **Programming Language:** Python 🐍  
- **Automation Tool:** Playwright 🎭  
- **Test Framework:** Pytest ⚡  
- **Version Control:** Git & GitHub  

---

## 📂 **Project Structure**

# Automation_task/

│── pages/ # Page Object Model (POM) for each webpage │ 

├── login_page.py # Login page interactions │ 

├── products_page.py # Products │ 

├── cart_page.py # Cart interactions │ 

├── checkout_page.py # Checkout process handling │ 

├── sorting_page.py # Sorting logic │ 

├── logout_page.py # Logout page │ 

# Test scripts for different functionalities │ 

├── test_login.py # Login test cases │ 

├── test_cart.py # Add to cart validation │ 

├── test_checkout.py # Checkout process validation │ 

├── test_sorting.py # Sorting products validation │ 

├── test_logout.py # Logout functionality test │ 

├── test_locked_out_user.py # Handling locked-out user case │ 

├── test_cart_badge.py # Cart badge count validation │


# Install Playwright Browsers
playwright install

# 🏃 Running the Tests
pytest tests/

# Run a Specific Test File
pytest tests/test_login.py (example for only login)

# Run Tests with Detailed Output
pytest -v --headed

# ✅ Test Cases Implemented

Login	-> Validates correct & incorrect login attempts

Add to Cart->	Checks if products can be added to the cart

Sorting	-> Ensures sorting works by price and name

Cart Badge->	Verifies cart badge updates correctly

Checkout->	Validates checkout process and order confirmation

Logout-> 	Ensures users can log out successfully

Locked-Out User->	Handles blocked user scenario gracefully



