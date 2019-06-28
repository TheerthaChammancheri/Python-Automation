from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')

driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
driver.maximize_window()

# Scroll the page by 0 to 1000 pixel
driver.execute_script("window.scrollBy(0, 1000)", "")
time.sleep(2)

# Scroll the page untill the element is found
flag = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img')
driver.execute_script("arguments[0].scrollIntoView();",flag)
time.sleep(4)

# Scroll the page to the end of the page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(4)

driver.quit()