import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += os.pathsep + r'C:/SeleniumDrivers'
driver = webdriver.Chrome()
driver.implicitly_wait(5)

# poderiam ser formulários
coisa1 = driver.find_element_by_id('id coisa1')
coisa2 = driver.find_element_by_id('id coisa2')
coisa3 = driver.find_element_by_id('id coisa3')

coisa1.send_keys(278318908290389)
coisa2.send_keys(1123435545)
coisa3.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)