'''
Brave broswer installed in /usr/bin/brave-browser
Chromedriver installed in /usr/local/bin (chromedriver is globally accessible)

This script automates the login process for a practice test website using Selenium with the Brave browser.
It performs the following steps:
1. Opens the login page.
2. Locates the username and password fields and fills them in.
3. Clicks the login button.
4. Waits for the page to load and captures a screenshot of the result.
5. Optionally verifies the successful login by checking for a specific message.
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Configuring Chrome options for Brave browser
options = Options()
options.binary_location = "/usr/bin/brave-browser"

# Initializing driver (since chromedriver is globally available, no need to specify path)
driver = webdriver.Chrome(options=options)

try:
    # Step 1: Open the login page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()

    # Step 2: Locate and fill in username and password
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys("student")
    password_input.send_keys("Password123")

    # Step 3: Click the login button
    login_button = driver.find_element(By.ID, "submit")
    login_button.click()

    # Step 4: Wait and capture screenshot
    time.sleep(2)  # Give it time to load after login
    driver.save_screenshot("login_result.png")
    print("Screenshot saved as login_result.png")

    # Step 5 (Optional): Verify successful login
    success_message = driver.find_element(By.TAG_NAME, "h1").text
    assert "Logged In Successfully" in success_message
    print("Login successful and verified.")

finally:
    # Step 6: Closing the browser
    driver.close()
