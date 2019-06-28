from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')

driver.get('http://newtours.demoaut.com')

# Get the status of textbox (username and password)
user_textbox = driver.find_element_by_name('userName')
print (user_textbox.is_displayed())
print (user_textbox.is_enabled())

if user_textbox.is_displayed() and user_textbox.is_enabled():
    driver.find_element_by_name('userName').send_keys('mercury')

password_textbox = driver.find_element_by_name('password')
print ('status of username textbox {}'.format(password_textbox.is_displayed()))
print ('status od password texttbox {}'.format(password_textbox.is_enabled()))

if password_textbox.is_displayed() and password_textbox.is_enabled():
    driver.find_element_by_name('password').send_keys('mercury')

# click on sign in button
driver.find_element_by_name('login').click()

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