from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')
driver.maximize_window()

driver.get('https://testautomationpractice.blogspot.com')
driver.switch_to_frame(0)
driver.implicitly_wait(10)

flag = driver.find_element_by_id('RESULT_FileUpload-11')
driver.execute_script("arguments[0].scroolIntoView;", flag)
time.sleep(2)

driver.find_element_by_id('RESULT_FileUpload-11').send_keys('E://Subash//Python//SeleniumAutomation//Resources//Chrome_Error.jpg')
time.sleep(5)

driver.quit()