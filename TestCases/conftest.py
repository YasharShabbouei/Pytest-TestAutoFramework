import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.support.wait import WebDriverWait
import time

@pytest.fixture(scope='class')
#def setup(request, browser, URL):
def setup(request, browser):
    if browser == 'Chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == 'FireFox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    #wait = WebDriverWait(driver,10)
    driver.get("https://admin-demo.nopcommerce.com/")
    #driver.get(URL)
    driver.maximize_window()
    request.cls.driver = driver
    #request.cls.wait = wait

    yield 
    time.sleep(5)
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope='class', autouse = True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope='class', autouse = True)
def URL(request):
    return request.config.getoption("--url")


