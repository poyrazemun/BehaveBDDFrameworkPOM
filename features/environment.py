from selenium import webdriver
from utilities import config_reader
from features.pages.base_page import BasePage
from features.pages.home_page import HomePage
from features.pages.login_page import LoginPage
from features.pages.my_account_page import MyAccountPage
from features.pages.search_page import SearchPage
from features.pages.register_page import RegisterPage
from features.pages.account_success_page import AccountSuccessPage


def before_scenario(context, scenario):
    browser_name = config_reader.read_configuration("basic info", "browser")
    if browser_name == "chrome":
        context.driver = webdriver.Chrome()
    elif browser_name == "firefox":
        context.driver = webdriver.Firefox()
    elif browser_name == "edge":
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(config_reader.read_configuration("basic info", "url"))

    context.hp = HomePage(context.driver)
    context.lp = LoginPage(
        context.driver)  # bu sekilde pagelerin objectini her senaryodan once olusturuyorum ki senaryolarda rahatlikla pagelerden gelen methodlari vs. kullanabileyim
    context.map = MyAccountPage(context.driver)
    context.sp = SearchPage(context.driver)
    context.rp = RegisterPage(context.driver)
    context.asp = AccountSuccessPage(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()
