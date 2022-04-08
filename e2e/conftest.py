import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions() 
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    yield driver
    #teardown
    driver.close()

@pytest.fixture
def loginPage(driver):
    return LoginPage(driver)

@pytest.fixture
def homepage(driver):
    return HomePage(driver) 