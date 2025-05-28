from selenium.webdriver.common.by import By
from locators.appointment import Locator

class Appointment:
    def __init__(self, setup):
        self.setup = setup

    def cek_judulMakeAppointment(self):
        judulMakeAppointment = self.setup.find_element(By.XPATH, Locator.cek_judulMakeAppointment).is_displayed()
        assert judulMakeAppointment == True
