import time
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launching the application
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://devwinde1webapp1dev.azurewebsites.net/Account/SignIn?ReturnUrl=%2F")
driver.implicitly_wait(3)

#########LOGIN###################
email_input = driver.find_element(By.ID, "Username")
# email_input.clear()# Clear any pre-filled text (if any)
email_input.send_keys("thanusha.kataprolu@clientek.com", Keys.RETURN)
driver.implicitly_wait(5)
password_input = driver.find_element(By.ID,"Password")
password_input.send_keys("Cognine@12",Keys.RETURN)
time.sleep(3)

###################PROJECTS PAGE#############
try:
    # Wait for the element with visible text to be clickable
    div_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Projects')]"))
    )
    # Click the element
    div_element.click()
finally:
    time.sleep(3)

#########CLICK ON CREATE NEW PROJECT BUTTON###################
create_project_button = driver.find_element(By.CLASS_NAME, "btnOrange")
driver.execute_script("arguments[0].click();", create_project_button)
time.sleep(3)

###########CREATING PROJECT############
project_name_input = driver.find_element(By.ID,"projectName")
# project_name_input.clear()# Clear any pre-filled text (if any)
project_name_input.send_keys("Winde test 1")
address_input = driver.find_element(By.ID,"address")
#address_input.clear()# Clear any pre-filled text (if any)
address= driver.find_element(By.XPATH, '//*[@id="address"]')
address.send_keys('23 Main St, Hilton Head Island, SC, USA')
# city_input = driver.find_element(By.ID,"city")
# city_name = "New York"
# city_input.send_keys(city_name)
# state_input = driver.find_element(By.ID,"state")
# state_name = "California"
# state_input.send_keys(state_name)
# zip_code_input = driver.find_element(By.ID,"zipCode")
# zip_code = "90001 "  # Replace with the actual zip code
# zip_code_input.send_keys(zip_code)
select_element = driver.find_element(By.ID,"asceEdition")
# Create a Select object using the select element
select = Select(select_element)
select.select_by_visible_text("ASCE 7-22")
# select.select_by_value("3")# We can select the value also
height_input = driver.find_element(By.ID,"buildingHeight")
building_height = "20"
height_input.send_keys(building_height)
select_element = driver.find_element(By.ID,"riskCategory")
select = Select(select_element)
select.select_by_visible_text("III")
select_element = driver.find_element(By.ID,"exposureCategory")
select = Select(select_element)
select.select_by_visible_text("C")
driver.find_element(By.XPATH, '//*[@id="savebtn"]').click()
time.sleep(8)

########ADDING UNITS####################
description_input = driver.find_element(By.ID, "description_2")
description_input.send_keys("Sample description")
unit_size_input = driver.find_element(By.ID, "unitSize_2")
unit_size_input.send_keys("65")
# unit_height_input = driver.find_element(By.ID, "unitHeight_2")
# unit_height_input.send_keys("18")
time.sleep(3)
# save_button = driver.find_element(By.ID, "savebtn")
# driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
# save_button.click()
try:
    calculate_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@onclick='calculateData()']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", calculate_button)
    calculate_button.click()
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.XPATH, "//button[@onclick='calculateData()']")))
    print("Calculation successfully completed.")
    projects_button = driver.find_element(By.ID, 'navProjectBtn').find_element(By.CSS_SELECTOR, 'a.nav-link')
    projects_button.click()
finally:
    time.sleep(3)