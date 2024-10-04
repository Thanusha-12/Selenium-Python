###Handling AJAX calls in Selenium involves waiting for elements to load or change as a result of asynchronous requests.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
try:
    driver.get("https://example.com/ajax-page")
    trigger_button = driver.find_element(By.ID, "trigger-ajax-button")
    trigger_button.click()
    ajax_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ajax-result-button")))
    ajax_button.click()
    time.sleep(5)
finally:
    driver.quit()
