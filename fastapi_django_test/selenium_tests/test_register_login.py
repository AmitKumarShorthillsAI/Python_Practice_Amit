import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

class TestUserRegistrationLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setup Brave Browser options
        options = Options()
        options.binary_location = "/usr/bin/brave-browser"

        # Initialize driver
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.maximize_window()
        cls.base_url = "http://127.0.0.1:9000"

    def test_register_valid_user(self):
        try:
            self.driver.get(f"{self.base_url}/register/")
            time.sleep(1)

            self.driver.find_element(By.NAME, "username").send_keys("testuser1")
            self.driver.find_element(By.NAME, "password").send_keys("Test@1234")
            self.driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

            time.sleep(2)
            print("Valid registration test passed.")
        except Exception as e:
            print(f"Valid registration test failed: {e}")
            self.fail("Valid registration test failed.")

    def test_register_invalid_user(self):
        try:
            self.driver.get(f"{self.base_url}/register/")
            time.sleep(1)

            self.driver.find_element(By.NAME, "username").send_keys("a")  # Too short username
            self.driver.find_element(By.NAME, "password").send_keys("123")  # Weak password
            self.driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

            time.sleep(2)
            print("Invalid registration test completed (should show error).")
        except Exception as e:
            print(f"Invalid registration test failed: {e}")
            self.fail("Invalid registration test failed.")

    def test_login_valid_user(self):
        try:
            self.driver.get(f"{self.base_url}/login/")
            time.sleep(1)

            self.driver.find_element(By.NAME, "username").send_keys("testuser1")
            self.driver.find_element(By.NAME, "password").send_keys("Test@1234")
            self.driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

            time.sleep(2)
            print("Valid login test passed.")
        except Exception as e:
            print(f"Valid login test failed: {e}")
            self.fail("Valid login test failed.")

    def test_login_invalid_user(self):
        try:
            self.driver.get(f"{self.base_url}/login/")
            time.sleep(1)

            self.driver.find_element(By.NAME, "username").send_keys("wronguser")
            self.driver.find_element(By.NAME, "password").send_keys("WrongPass123")
            self.driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

            time.sleep(2)
            print("Invalid login test completed (should show error).")
        except Exception as e:
            print(f"Invalid login test failed: {e}")
            self.fail("Invalid login test failed.")

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()

if __name__ == "__main__":
    unittest.main()
