from pages.auth_page import AuthPage
from pages.locators import AuthLocators, RegLocators, PassRecoveryLocators, AgrLocators, SocialLocators
import pytest
import test_data

def test_load_auth_page_positive(browser):
  '''тест загрузки страницы авторизации'''
  page = AuthPage(browser)
  page.go_to_site()
  assert 'https://b2c.passport.rt.ru/' in page.get_current_url()
  assert page.get_text_from_element(AuthLocators.AUTH_TITLE) == 'Авторизация'

def test_load_reg_page_positive(browser):
  '''тест загрузки страницы регистрации'''
  page = AuthPage(browser)
  page.go_to_site()
  page.click_link(AuthLocators.LINK_REGISTRATION)
  assert 'registration' in page.get_current_url()
  assert page.get_text_from_element(RegLocators.REG_TITLE) == 'Регистрация'

def test_load_forgot_pass_page_positive(browser):
  '''тест загрузки страницы восстановления пароля'''
  page = AuthPage(browser)
  page.go_to_site()
  page.click_link(AuthLocators.LINK_FORGOT_PASS)
  assert 'login-actions/reset-credentials' in page.get_current_url()
  assert page.get_text_from_element(PassRecoveryLocators.PASS_TITLE) == 'Восстановление пароля'

@pytest.mark.parametrize('locator, expected', [(AuthLocators.TAB_MAIL, 'Электронная почта'), (AuthLocators.TAB_LOGIN, 'Логин'), (AuthLocators.TAB_PERS_ACCOUNT, 'Лицевой счёт'), (AuthLocators.TAB_PHONE, 'Мобильный телефон')])
def test_change_tabs_auth_page_positive(browser, locator, expected):
  '''тест смены типов логина на странице авторизации'''
  page = AuthPage(browser)
  page.go_to_site()
  page.click_link(locator)
  assert page.get_text_from_element(AuthLocators.LOGIN_PLACEHOLDER) == expected

@pytest.mark.parametrize('login', test_data.VALID_LOGINS)
def test_auth_user_with_valid_email_positive(browser, login):
  '''тест авторизации пользователя с валидными учетными данными'''
  page = AuthPage(browser)
  page.go_to_site()
  page.enter_data(AuthLocators.AUTH_LOGIN, login)
  page.enter_data(AuthLocators.AUTH_PASS, test_data.VALID_PASS)  
  page.click_enter_btn()
  assert 'account_b2c/page' in page.get_current_url()

def test_auth_user_with_invalid_phone_negative(browser):
  '''тест авторизации пользователя с невалидным номером телефона и валидным паролем'''
  page = AuthPage(browser)
  page.go_to_site()
  page.enter_data(AuthLocators.AUTH_LOGIN, test_data.INVALID_PHONE)
  page.enter_data(AuthLocators.AUTH_PASS, test_data.VALID_PASS)  
  page.click_enter_btn()
  assert page.get_text_from_element(AuthLocators.AUTH_ERROR) == test_data.WRONG_LOGIN_OR_PASS_MESSAGE or test_data.WRONG_CAPCHA_MESSAGE

def test_auth_user_with_invalid_mail_negative(browser):
  '''тест авторизации пользователя с невалидным адресом почты и валидным паролем'''
  page = AuthPage(browser)
  page.go_to_site()
  page.enter_data(AuthLocators.AUTH_LOGIN, test_data.INVALID_EMAIL)
  page.enter_data(AuthLocators.AUTH_PASS, test_data.VALID_PASS)  
  page.click_enter_btn()
  assert page.get_text_from_element(AuthLocators.AUTH_ERROR) == test_data.WRONG_LOGIN_OR_PASS_MESSAGE or test_data.WRONG_CAPCHA_MESSAGE

@pytest.mark.parametrize('login', test_data.VALID_LOGINS)
def test_auth_user_with_invalid_pass_negative(browser, login):
  '''тест авторизации пользователя с валидным логином и невалидным паролем'''
  page = AuthPage(browser)
  page.go_to_site()
  page.enter_data(AuthLocators.AUTH_LOGIN, login)
  page.enter_data(AuthLocators.AUTH_PASS, test_data.INVALID_PASS)  
  page.click_enter_btn()
  assert page.get_text_from_element(AuthLocators.AUTH_ERROR) == test_data.WRONG_LOGIN_OR_PASS_MESSAGE or test_data.WRONG_CAPCHA_MESSAGE

def test_reg_user_without_data_negative(browser):
  '''тест регистрации нового пользователя без указания учетных данных''' 
  page = AuthPage(browser)
  page.go_to_site()
  page.click_link(AuthLocators.LINK_REGISTRATION)
  reg_url = page.get_current_url()
  page.click_reg_btn()
  assert reg_url == page.get_current_url()

@pytest.mark.parametrize('name', test_data.INVALID_NAMES)
def test_reg_invalid_name_negative(browser, name):
  '''тест регистрации нового пользователя с указанием имени в неверном формате'''
  page = AuthPage(browser)
  page.go_to_site()
  page.click_link(AuthLocators.LINK_REGISTRATION)
  page.enter_data(RegLocators.NAME, name)
  page.click_reg_btn()
  assert page.get_text_from_element(RegLocators.REG_ERROR) == test_data.WRONG_NAME_MESSAGE

@pytest.mark.parametrize('surname', test_data.INVALID_SURNAMES)
def test_reg_invalid_surname_negative(browser, surname):
  '''тест регистрации нового пользователя с указанием фамилии в неверном формате'''
  page = AuthPage(browser)
  page.go_to_site()
  page.click_link(AuthLocators.LINK_REGISTRATION)
  page.enter_data(RegLocators.SURNAME, surname)
  page.click_reg_btn()
  assert page.get_text_from_element(RegLocators.REG_ERROR) == test_data.WRONG_SURNAME_MESSAGE

@pytest.mark.parametrize('phone', test_data.INVALID_PHONES)
def test_reg_invalid_phone_negative(browser, phone):
  '''тест регистрации нового пользователя с указанием номера телефона в неверном формате'''
  page = AuthPage(browser)
  page.go_to_site()
  page.click_link(AuthLocators.LINK_REGISTRATION)
  page.enter_data(RegLocators.REG_LOGIN, phone)
  page.click_reg_btn()
  assert page.get_text_from_element(RegLocators.REG_ERROR) == test_data.WRONG_LOGIN_MESSAGE

@pytest.mark.parametrize('email', test_data.INVALID_EMAILS)
def test_reg_invalid_email_negative(browser, email):
  '''тест регистрации нового пользователя с указанием адреса почты в неверном формате'''
  page = AuthPage(browser)
  page.go_to_site()
  page.click_link(AuthLocators.LINK_REGISTRATION)
  page.enter_data(RegLocators.REG_LOGIN, email)
  page.click_reg_btn()
  assert page.get_text_from_element(RegLocators.REG_ERROR) == test_data.WRONG_LOGIN_MESSAGE

@pytest.mark.parametrize('password', test_data.INVALID_PASSWORDS)
def test_reg_invalid_password_negative(browser, password):
  '''тест регистрации нового пользователя с указанием пароля в неверном формате'''
  page = AuthPage(browser)
  page.go_to_site()
  page.click_link(AuthLocators.LINK_REGISTRATION)
  page.enter_data(RegLocators.REG_PASS, password)
  page.click_reg_btn()
  assert page.get_text_from_element(RegLocators.REG_ERROR) == test_data.WRONG_PASSWORD_MESSAGE

@pytest.mark.parametrize('login', test_data.INVALID_LOGINS)
def test_pass_recovery_with_invalid_login_negative(browser, login):
  '''тест восстановления пароля с использованием невалидных логинов'''
  page = AuthPage(browser)
  page.go_to_site()
  page.click_link(AuthLocators.LINK_FORGOT_PASS)
  page.enter_data(PassRecoveryLocators.PASS_LOGIN, login)
  page.click_continue_btn()
  assert page.get_text_from_element(PassRecoveryLocators.PASS_ERROR) == test_data.WRONG_RECOVERY_MESSAGE

def test_agreement_link_positive(browser):
  '''тест работоспособности ссылки на пользовательское соглашение и политику конфиденциальности'''
  page = AuthPage(browser)
  page.get(test_data.AGREEMENT_URL)
  assert page.get_text_from_element(AgrLocators.AGR_TITLE) == test_data.AGREEMENT_TITLE

def test_auth_with_vk_profile_negative(browser):
  '''тест авторизации при помощи учетной записи vk с указанием невалидных учетных данных'''
  page = AuthPage(browser)
  page.go_to_site()
  page.click_link(AuthLocators.ICON_VK)
  page.enter_data(SocialLocators.VK_LOGIN, test_data.INVALID_EMAIL)
  page.enter_data(SocialLocators.VK_PASS, test_data.INVALID_PASS)
  page.click_link(SocialLocators.VK_SUBMIT_BTN)
  assert page.get_text_from_element(SocialLocators.VK_ERROR_MESSAGE) == test_data.VK_WRONG_MESSAGE
  assert 'oauth.vk.com' in page.get_current_url()

def test_auth_with_ok_profile_negative(browser):
  '''тест авторизации при помощи учетной записи ok с указанием невалидных учетных данных'''
  page = AuthPage(browser)
  page.go_to_site()
  page.click_link(AuthLocators.ICON_OK)
  page.enter_data(SocialLocators.OK_LOGIN, test_data.INVALID_EMAIL)
  page.enter_data(SocialLocators.OK_PASS, test_data.INVALID_PASS)
  page.click_link(SocialLocators.OK_SUBMIT_BTN)
  assert page.get_text_from_element(SocialLocators.OK_ERROR_MESSAGE) == test_data.OK_WRONG_MESSAGE
  assert 'connect.ok.ru' in page.get_current_url()

def test_auth_with_mail_profile_negative(browser):
  '''тест авторизации при помощи учетной записи mail.ru с указанием невалидных учетных данных'''
  page = AuthPage(browser)
  page.go_to_site()
  page.click_link(AuthLocators.ICON_MALE)
  page.enter_data(SocialLocators.MAIL_LOGIN, test_data.INVALID_EMAIL[:10])
  page.enter_data(SocialLocators.MAIL_PASS, test_data.INVALID_PASS)
  page.click_link(SocialLocators.MAIL_SUBMIT_BTN)
  assert page.get_text_from_element(SocialLocators.MAIL_ERROR_MESSAGE) == test_data.MAIL_WRONG_MESSAGE
  assert 'connect.mail.ru' in page.get_current_url()

def test_auth_with_google_profile_negative(browser):
  '''тест авторизации при помощи учетной записи google с указанием невалидных учетных данных'''
  page = AuthPage(browser)
  page.go_to_site()
  page.click_link(AuthLocators.ICON_GOOGLE)
  page.enter_data(SocialLocators.GOOGLE_LOGIN, test_data.INVALID_EMAIL)
  page.click_link(SocialLocators.GOOGLE_SUBMIT_BTN)
  assert page.get_text_from_element(SocialLocators.GOOGLE_ERROR_MESSAGE) == test_data.GOOGLE_WRONG_MESSAGE
  assert 'accounts.google.com' in page.get_current_url()

def test_auth_with_yandex_profile_negative(browser):
  '''тест авторизации при помощи учетной записи yandex с указанием невалидных учетных данных'''
  page = AuthPage(browser)
  page.go_to_site()
  page.click_link(AuthLocators.ICON_YANDEX)
  page.enter_data(SocialLocators.YANDEX_LOGIN, test_data.INVALID_LOGIN_YANDEX)
  page.click_link(SocialLocators.YANDEX_SUBMIT_BTN)
  assert page.get_text_from_element(SocialLocators.YANDEX_ERROR_MESSAGE) == test_data.YANDEX_WRONG_MESSAGE
  assert 'passport.yandex.ru' in page.get_current_url()  
  





  



  