import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class WindApp:
    def __init__(self):
        self.service_obj = Service()
        self.driver = webdriver.Chrome(service=self.service_obj)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def login(self, username, password):
        self.driver.get("https://devwinde1webapp1dev.azurewebsites.net/Account/SignIn?ReturnUrl=%2F")
        self.driver.find_element(By.ID, "Username").send_keys(username)
        self.driver.find_element(By.ID, "Password").send_keys(password)
        self.driver.find_element(By.CLASS_NAME, "btnOrange").click()

    def fill_windspeeds_page(self, address, asce_edition, risk_category, building_height, unit_height=None,
                             unit_size="56", wind_speed="150"):
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="address"]').send_keys(address)

        asce_select = Select(self.driver.find_element(By.XPATH, '//*[@id="asceEdition"]'))
        asce_select.select_by_visible_text(asce_edition)

        risk_select = Select(self.driver.find_element(By.XPATH, '//*[@id="riskCategory"]'))
        risk_select.select_by_visible_text(risk_category)

        if building_height > 60 and unit_height:
            self.driver.find_element(By.ID, "unitHeight").send_keys(unit_height)
        else:
            self.driver.execute_script("arguments[0].value = arguments[1];",
                                       self.driver.find_element(By.ID, "buildingHeight"), building_height)

        self.driver.find_element(By.ID, "unitSize").send_keys(unit_size)
        checkbox = self.driver.find_element(By.ID, "IsManualcheck")
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.driver.find_element(By.ID, "manualWindSpeed").send_keys(wind_speed)
        self.driver.find_element(By.XPATH, '//*[@id="savebtn"]').click()

    def navigate_to_home(self):
        home_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'nav-link') and contains(text(), 'Home')]"))
        )
        home_button.click()

    def close(self):
        self.driver.quit()

    def switch_to_iframe(self, iframe_id):
        self.driver.switch_to.frame(iframe_id)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()


@pytest.fixture
def wind_app():
    app = WindApp()
    yield app
    app.close()


def test_login_and_fill_windspeeds(wind_app):
    wind_app.login("thanusha.kataprolu@clientek.com", "Cognine@12")
    wind_app.fill_windspeeds_page("Miami, FL, USA", "ASCE 7-10", "II", 60, unit_height="35")
    wind_app.navigate_to_home()

    # Example of switching to an iframe if needed (replace 'iframe_id' with the actual ID)
    # wind_app.switch_to_iframe('iframe_id')

    # Further tests can be added here
    time.sleep(5)  # Add appropriate waits for elements to be present


if __name__ == "__main__":
    pytest.main()
