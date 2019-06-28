from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')

driver.get('https://seleniumhq.github.io/selenium/docs/api/java/index.html')

# Click the link on first frame
driver.switch_to_frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
driver.switch_to_default_content()
time.sleep(3)

# Click the link on second frame
driver.switch_to_frame("packageFrame")
driver.find_element(By.LINK_TEXT, "WebDriver").click()
driver.switch_to_default_content()
time.sleep(3)

# Click the link on third frame
driver.switch_to_frame("classFrame")
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]/a").click()
time.sleep(3)

driver.close()
driver.quit()