from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time
import pyautogui  # Used for handling file upload dialogs

# Load credentials from .env
load_dotenv()
EMAIL = os.getenv("HACKERRANK_EMAIL")
PASSWORD = os.getenv("HACKERRANK_PASSWORD")

# Load solution from file
with open("solve_me_first_solution.cpp", "r") as f:
    solution_code = f.read()

# Configure Chrome to use Brave
options = Options()
options.binary_location = "/usr/bin/brave-browser"
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

try:
    print("Logging in...")
    driver.get("https://www.hackerrank.com/auth/login")
    driver.maximize_window()
    
    # Wait until the email input is available and send the username
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    email_input.send_keys(EMAIL)

    # Wait until the password input is available and send the password
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password_input.send_keys(PASSWORD)

    # Find and click the login button using data-analytics attribute (most reliable)
    login_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/form/div[3]/button"
    )))
    login_button.click()

    # Wait for login to complete and navigate to the problem page
    problem_url = "https://www.hackerrank.com/challenges/solve-me-first/problem"
    time.sleep(4)
    print("Navigating to problem page...")
    driver.get(problem_url)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for the editor to load
    print("Pasting solution...")
    time.sleep(3)
    editor = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "view-lines")))

    # Inject code into editor using JS
    driver.execute_script(f"monaco.editor.getModels()[0].setValue(`{solution_code}`)")
    print("Code pasted successfully.")
    time.sleep(3)

    print("Running test cases...")
    run_code_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[4]/div/div/div/div/div[3]/div/section/div/div/div/div[1]/section[2]/div[1]/div/div[2]/div/div[1]/div[2]/button[2]")
    ))
    run_code_btn.click()

    print("Logging out...")
    time.sleep(5)
    
    profile_icon = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[contains(@class, 'profile-menu')]")
    ))
    profile_icon.click()

    logout_button = wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "logout-button")
    ))
    logout_button.click()
    print("Logged out successfully.")
    time.sleep(5)


except Exception as e:
    print("Error occurred:", e)

finally:
    print("Closing browser...")
    time.sleep(5)
    driver.close()
