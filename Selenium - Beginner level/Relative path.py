# # Find an element by its ID
# element = driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
#
# # Find an element with a partial match in the placeholder attribute
# element = driver.find_element_by_xpath("//input[contains(@placeholder, 'Search')]")
#
# # Find an element whose name starts with 'field'
# element = driver.find_element_by_xpath("//input[starts-with(@name, 'field')]")
#
# # Find a button within a specific form
# element = driver.find_element_by_xpath("//form[@id='search']//button")
#
# # Find a label that follows a specific input
# element = driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']/following-sibling::label")
#
# # Find the parent of an input element
# element = driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']/parent::*")
#
# # Find an input element with specific class and placeholder
# element = driver.find_element_by_xpath("//input[@class='nav-input' and @placeholder='Search Amazon.in']")


### Example ####
driver.get("https://www.amazon.in")
# Use relative XPath to find the search box and enter a query
search_box = driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
search_box.send_keys("Laptops")
# Find the search button and click it
search_button = driver.find_element_by_xpath("//input[@value='Go']")
search_button.click()
driver.quit()
