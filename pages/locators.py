from selenium.webdriver.common.by import By

class AuthLocators:
  AUTH_TITLE = (By.TAG_NAME, 'h1')
  AUTH_LOGIN = (By.ID, 'username')
  AUTH_PASS = (By.ID,'password')
  BTN_ENTER = (By.ID, "kc-login")
  LOGIN_PLACEHOLDER = (By.XPATH, '//div[contains(@class, "tabs-input-container__login")]//span[@class="rt-input__placeholder"]')
  TAB_PHONE = (By.ID, 't-btn-tab-phone')
  TAB_MAIL = (By.ID, "t-btn-tab-mail")
  TAB_LOGIN = (By.ID, "t-btn-tab-login")
  TAB_PERS_ACCOUNT = (By.ID, "t-btn-tab-ls")
  LINK_FORGOT_PASS = (By.ID, "forgot_password")
  LINK_REGISTRATION = (By.ID, "kc-register")
  LINK_AGREEMENT = (By.ID, "rt-footer-agreement-link")
  ICON_VK = (By.ID, "oidc_vk")
  ICON_OK = (By.ID, "oidc_ok")
  ICON_MALE = (By.ID, "oidc_mail")
  ICON_GOOGLE = (By.ID, "oidc_google")
  ICON_YANDEX = (By.ID, "oidc_ya")
  AUTH_ERROR = (By.ID, 'form-error-message')

class RegLocators:
  REG_TITLE = (By.TAG_NAME, 'h1')
  NAME = (By.NAME, 'firstName') 
  SURNAME = (By.NAME, 'lastName')
  REG_LOGIN = (By.ID, 'address') 
  REG_PASS = (By.ID, 'password')
  REG_PASS_CONFIRM = (By.ID, 'password-confirm')
  REG_BTN = (By.NAME, 'register')
  REG_ERROR = (By.XPATH, '//span[contains(@class, "rt-input-container__meta--error")]')

class PassRecoveryLocators: 
  PASS_TITLE = (By.TAG_NAME, 'h1') 
  PASS_LOGIN = (By.ID, 'username')
  PASS_BTN = (By.ID, 'reset')
  PASS_ERROR = (By.ID, 'form-error-message')

class AgrLocators:
  AGR_TITLE = (By.CLASS_NAME, 'offer-title') 

class SocialLocators:
  VK_LOGIN = (By.NAME, 'email')
  VK_PASS = (By.NAME, 'pass')
  VK_SUBMIT_BTN = (By.ID, 'install_allow')
  VK_ERROR_MESSAGE = (By.CLASS_NAME, 'box_error')
  OK_LOGIN = (By.ID, 'field_email')
  OK_PASS = (By.ID, 'field_password')
  OK_SUBMIT_BTN = (By.CLASS_NAME, 'form-actions_yes' )
  OK_ERROR_MESSAGE = (By.CLASS_NAME, 'input-e')
  MAIL_LOGIN = (By.ID, 'login')
  MAIL_PASS =(By.ID, 'password')
  MAIL_SUBMIT_BTN = (By.CLASS_NAME, 'ui-button-main')
  MAIL_ERROR_MESSAGE = (By.CLASS_NAME, 'login-form__error')
  GOOGLE_LOGIN = (By.ID, 'identifierId')
  GOOGLE_SUBMIT_BTN = (By.XPATH, '//button[contains(@class, "AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b")]')
  GOOGLE_ERROR_MESSAGE = (By.CLASS_NAME, 'o6cuMc')
  YANDEX_LOGIN =(By.ID, 'passp-field-login')
  YANDEX_SUBMIT_BTN = (By.ID, 'passp:sign-in')
  YANDEX_ERROR_MESSAGE = (By.ID, 'field:input-login:hint')

