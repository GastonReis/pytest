from selenium.webdriver.common.by import By


class LoginPage():

    BASE_URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver
        driver.get(self.BASE_URL)

    def do_login(self, username, password):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def was_login_successful(self):
        return self.driver.current_url == "https://www.saucedemo.com/inventory.html"