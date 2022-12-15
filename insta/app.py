from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://instagram.com')

time.sleep(2)
e = driver.find_element_by_css_selector('input[name="username"]')
e.send_keys('enddl402')
e = driver.find_element_by_css_selector('input[name="password"]')
e.send_keys('2022exer@@')
e.send_keys(Keys.ENTER)

time.sleep(5)
driver.get('https://www.instagram.com/explore/tags/%EA%B7%A4/?next=%2F')
time.sleep(5)
e = driver.find_element_by_css_selector('._aagw').click()

imgi = driver.find_elements_by_css_selector('.x13vifvy')[1].get_attribute('src')
urllib.request.urlretrieve(imgi, '1.jpg')



# time.sleep(2)
# e = driver.find_element_by_css_selector('input[name="username"]').text
# print(e)