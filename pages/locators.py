from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    URL_LINK = "http://selenium1py.pythonanywhere.com/ru/login/"
    ENTER_ADDRESS = (By.XPATH, "//input[@name='login-username']")
    ENTER_PASSWORD = (By.XPATH, "//input[@name='login-password']")
    REG_ADDRESS = (By.XPATH, "//input[@name='registration-email']")
    REG_PASSWORD = (By.XPATH, "//input[@name='registration-password']")
    REG_REPEAT_PASSWORD = (By.XPATH, "//input[@name='registration-password2']")


class ProductPageLocators():
    BUTTON_ADD_PRODUCT_TO_BASKET = (By.XPATH, "//*[@id='add_to_basket_form']/button")
    MES_ABOUT_ADDING = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRODUCT_NAME = (By.XPATH, "//div/h1")
    MESSAGE_BASKET_TOTAL = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    PRODUCT_PRICE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
