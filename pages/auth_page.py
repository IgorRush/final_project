from .base_page import BasePage
from .locators import AuthLocators, RegLocators, PassRecoveryLocators
from selenium.webdriver.common.by import By

class AuthPage(BasePage):

  def enter_data(self, locator, text):
    input_field = self.find_element(locator)
    input_field.click()
    input_field.send_keys(text)
    return input_field

  def click_enter_btn(self):
    return self.find_element(AuthLocators.BTN_ENTER).click()

  def click_reg_btn(self):
    return self.find_element(RegLocators.REG_BTN).click()  

  def click_continue_btn(self):
    return self.find_element(PassRecoveryLocators.PASS_BTN).click() 

  def click_link(self, locator):
    return self.find_element(locator).click()



