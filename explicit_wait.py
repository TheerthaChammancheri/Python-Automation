from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')

driver.maximize_window()

driver.get('https://www.expedia.com/')
driver.find_element(By.ID, "tab-hotel-tab-hp").click()

driver.find_element(By.ID, "flight-origin-hp-flight").send_keys('SFO')
driver.find_element(By.ID, "flight-destination-hp-flight").send_keys('NYC')

driver.find_element(By.ID, "flight-departing-hp-flight").click()
driver.find_element(By.ID, 'flight-departing-hp-flight').send_keys('12/10/2019')

driver.find_element(By.ID, "flight-departing-hp-flight").click()
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys('15/10/2019')

driver.find_element(By.XPATH, "//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()

# Explicit Wait time
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable(By.XPATH, "//*[@id='stopFilter_stops-0']"))
element.click()

driver.close()
driver.quit()