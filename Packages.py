from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://google.com')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'submit'))
)

from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)
actions.move_to_element(element).click().perform()

from selenium.webdriver.support.ui import Select

select_element = driver.find_element(By.ID, 'dropdown')
select = Select(select_element)
select.select_by_visible_text('Option 1')

driver.switch_to.frame('frame_name_or_id')




