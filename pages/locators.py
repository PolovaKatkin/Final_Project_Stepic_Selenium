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
    BUTTON_ADD_PRODUCT_TO_BASKET = (By.XPATH, "//button[@value='Добавить в корзину']")
    MES_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
