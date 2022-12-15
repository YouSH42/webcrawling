from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://instagram.com')



# time.sleep(2)
# e = driver.find_element_by_css_selector('input[name="username"]').text
# print(e)