from select import select
from selenium import webdriver
import os
import Booking.constants as const

class Booking(webdriver.Chrome):
    def __init__(self, driver_path = r'C:/SeleniumDrivers', teardown = False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += os.pathsep + driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
    
    def __exit__(self, *args):
        if self.teardown:
            self.quit()
    
    def land_first_page(self):
        self.get(const.BASE_URL)
    
    def change_currency(self, currency = 'BRL'):
        currency_button = self.find_element_by_css_selector('button[data-modal-aria-label = "Selecione sua moeda"]')
        currency_button.click()
        selected_currency_element = self.find_element_by_css_selector(f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        selected_currency_element.click()
        
    def select_destination(self, destination):
        search_field = self.find_element_by_id('ss')
        search_field.clear()
        search_field.send_keys(destination)
        first_result = self.find_element_by_css_selector('li[data-i="0"]')
        first_result.click()
        
    def select_date(self, checkin, checkout):
        checkin_element = self.find_element_by_css_selector(f'td[data-date="{checkin}"')
        checkin_element.click()
        checkout_element = self.find_element_by_css_selector(f'td[data-date="{checkout}"')
        checkout_element.click()