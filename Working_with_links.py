from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')

driver.get('http://newtours.demoaut.com/')

all_links = driver.find_elements(By.TAG_NAME, "a")

# count the number of links
print (len(all_links))

# extract each link and each
for link in all_links:
    print (link.text)
    if link.text == "REGISTER":
        driver.find_element(By.LINK_TEXT, link.text).click()
        break

time.sleep(3)

driver.close()
driver.quit()