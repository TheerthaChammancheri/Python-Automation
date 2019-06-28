from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
driver.maximize_window()
x=driver.find_element_by_xpath('//*[@id="RESULT_RadioButton-7"]')
driver.execute_script("arguments[0].scrollIntoView();",x)
drpdwn=Select(x)
drpdwn.select_by_index(1)
# drpdwn.select_by_visible_text('Evening')
opts=drpdwn.options
for o in opts:
    print o.text
time.sleep(5)
driver.close()
driver.quit()