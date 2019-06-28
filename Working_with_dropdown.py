from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')

drp = Select(driver.find_element_by_id('RESULT_RadioButton-7'))

# select by value
#drp.select_by_value('Radio-2')

# select by visible text
#drp.select_by_visible_text('Morning')
time.sleep(5)

#select by index
drp.select_by_index(1)
time.sleep(2)

# Count number of option
print (len(drp.options))

# Capture all the options
all_options = drp.options
for option in all_options:
    print(option.text)

driver.close()
driver.quit()