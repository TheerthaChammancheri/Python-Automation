from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')

# Find the total number of Inputboxes
inputboxes = driver.find_elements(By.CLASS_NAME, 'text_field')
print (len(inputboxes))

# Provide value into textbox
display_status = driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
print (display_status)
driver.find_element(By.ID, 'RESULT_TextField-1').send_keys('Testing')

enable_status = driver.find_element(By.ID, 'RESULT_TextField-2').is_enabled()
print (enable_status)
driver.find_element(By.ID, 'RESULT_TextField-2').send_keys('Testing')

driver.find_element_by_id('RESULT_TextField-3').send_keys('9807654123')