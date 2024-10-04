from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self._username = None
        self._password = None
        self._submit_button = None
    @property
    def username(self):
        if not self._username:
            self._username = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "username"))
            )
        return self._username
    @property
    def password(self):
        if not self._password:
            self._password = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "password"))
            )
        return self._password
    @property
    def submit_button(self):
        if not self._submit_button:
            self._submit_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "submit")))
        return self._submit_button
    def login(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.submit_button.click()
driver = webdriver.Chrome()
driver.get("file:///path/to/your/local/file.html")
login_page = LoginPage(driver)
login_page.login("my_username", "my_password")
driver.quit()
