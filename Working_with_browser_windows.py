from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')

driver.get('http://demo.automationtesting.in/Windows.html')

driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

# get the current window handle
print (driver.current_window_handle)

# return all the handle values opened
all_handle = driver.window_handles
for handle in all_handle:
    driver.switch_to_window(handle)
    time.sleep(2)
    print (driver.title)
    if driver.title == "Access Blocked":
        driver.close()
        break

time.sleep(2)
driver.quit()