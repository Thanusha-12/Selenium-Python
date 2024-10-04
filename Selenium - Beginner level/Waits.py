##An implicit wait sets a default wait time for the entire WebDriver session
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)# implicit wait of 10 seconds
driver.get("https://www.example.com")
element = driver.find_element_by_id("some_id")

##Explicit waits allow you to wait for a specific condition to occur before proceeding further in the code
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://www.example.com")
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
element = wait.until(EC.visibility_of_element_located((By.ID, "some_id")))
element.click()




