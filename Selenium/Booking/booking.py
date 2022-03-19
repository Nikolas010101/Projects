from selenium import webdriver
import os
import Booking.constants as const

class Booking(webdriver.Chrome):
    def __init__(self, driver_path = r'C:/SeleniumDrivers', teardown = False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += os.pathsep + driver_path
        super(Booking, self).__init__()
    
    def __exit__(self, *args):
        if self.teardown:
            self.quit()
    
    def land_first_page(self):
        self.get(const.BASE_URL)
        