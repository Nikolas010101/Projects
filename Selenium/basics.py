import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(r'C:/SeleniumDrivers/chromedriver.exe')
driver.implicitly_wait(30)
driver.get('url qualquer')
# espera x segundos até encontrar o elemento ou realizar a ação
elemento = driver.find_element_by_id('id da tag')
elemento.click()

div_qualquer = driver.find_element_by_class_name('classe da div')
print(div_qualquer.text)

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'classe que estou procurando'),# provavelmente poderia ter usado div_qualquer como argumento
        'texto esperado'
    )
)