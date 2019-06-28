from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')

driver.get('http://newtours.demoaut.com')

# validate the radiobutton
roundtrip_status = driver.find_element_by_css_selector('input[value=roundtrip]')
print ('Status of roundtrip radiobutton {}'.format(roundtrip_status.is_selected()))

oneway_status = driver.find_element_by_css_selector('input[value=oneway]')
print ('Status of oneway radiobutton before {}'.format(oneway_status.is_selected()))
driver.find_element_by_css_selector('input[value=oneway]').click()
oneway_status = driver.find_element_by_css_selector('input[value=oneway]')
print ('Status of oneway radiobutton after {}'.format(oneway_status.is_selected()))

driver.close()
driver.quit()