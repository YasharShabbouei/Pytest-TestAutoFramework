import sys
sys.path.append(r"C:\\Users\\yasha\\OneDrive\\Desktop\\Selenium\\testAutomationFramework")

from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver


class PageElements(BaseDriver):
    #locators
    email_xpath = "//input[@id='Email']"
    password_xpath = "//input[@id='Password']"
    logIn_xpath = "//button[@type='submit']"
    search_xpath = "//input[@placeholder='Search']"
    selectSearch_xpath = "//div[@class='tt-dataset tt-dataset-pages']//div[1]"
    logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def getElementLocator(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def setUsername(self,email):
        self.getElementLocator(self.email_xpath).clear()
        self.getElementLocator(self.email_xpath).send_keys(email)

    def setPassword(self,password):
        self.getElementLocator(self.password_xpath).clear()
        self.getElementLocator(self.password_xpath).send_keys(password)
    
    def clickLogin(self):
        self.getElementLocator(self.logIn_xpath).click()

    def searchValue(self,searchKey):
        self.getElementLocator(self.search_xpath).clear()
        self.getElementLocator(self.search_xpath).send_keys(searchKey)

    def clickSearchValue(self):
        self.getElementLocator(self.selectSearch_xpath).click()

    def clickLogout(self):
        self.getElementLocator(self.logout_xpath).click()

    def loginTowebsite(self, email, password):
        self.getElementLocator(self.email_xpath).clear()
        self.getElementLocator(self.email_xpath).send_keys(email)
        self.getElementLocator(self.password_xpath).clear()
        self.getElementLocator(self.password_xpath).send_keys(password)
        self.getElementLocator(self.logIn_xpath).click()