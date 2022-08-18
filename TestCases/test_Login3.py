import pytest
import sys
sys.path.append(r"C:\\Users\\yasha\\OneDrive\\Desktop\\Selenium\\testAutomationFramework")

from Pages.PageObjects import PageElements
from Utilities.userDefinedCode import read_data_from_excel as ReadExcel
from Base.base_driver import BaseDriver


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



@pytest.mark.usefixtures('setup')
class TestLoginAndSearch():
    # 0) create a method for our needed objectes within the test cases
    @pytest.fixture(autouse = True)
    def class_setup(self):
        self.LoginObject = PageElements(self.driver)


    # 1) uncomments theses lines, remove parametrize, and add self. to email, password and searchKey
    """ email = "admin@yourstore.com"
    password = "admin"
    searchKey = "WEB API" """
    # 2) use pytest.parameteraize to do the above work, no need for self
    @pytest.mark.parametrize("email, password, searchKey",[("admin@yourstore.com","admin", "WEB API")])
    @pytest.mark.regression
    def test_login_test1(self, email, password, searchKey):
        #LoginObject = PageElements(self.driver)
        """ # Enter Email
        LoginObject.setUsername(email)
        # Enter Password
        LoginObject.setPassword(password)
        # Click on Login
        LoginObject.clickLogin() """
        ### by changing the codes in PageObjects.py, the above three lines of code are changed to one line code below
        self.LoginObject.loginTowebsite(email, password)
        # Wait: interresting: it will until the page contains Dashbord then moves to the next line
        self.LoginObject.wait_for_presence_of_an_element(By.XPATH, "//h1[normalize-space()='Dashboard']")

        # scroll down (LoginObject is an object of PageElements which inherited the pagescroll from BaseDriver of the base_driver-py
        # so we dont need to inherit the BaseDriver here in the TestAutomationFramework class)
        self.LoginObject.pagescroll()

        # Type search key
        self.LoginObject.searchValue(searchKey)

        # Enter on the found search 
        self.LoginObject.clickSearchValue()

        #wait and Logout
        self.LoginObject.wait_for_presence_of_an_element(By.XPATH, "//h1[normalize-space()='Web API (official plugin)']")
        ####waitPage = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1[normalize-space()='Web API (official plugin)']")))
        self.LoginObject.clickLogout()

    @pytest.mark.parametrize("email, password, searchKey",[("admin@yourstore.com","admin", "WEB API")])
    @pytest.mark.sanity
    def test_login_test2(self, email, password, searchKey):
        self.LoginObject.loginTowebsite(email, password)
        #self.LoginObject.wait_for_presence_of_an_element(By.XPATH, "//h1[normalize-space()='Dashboard']")
        self.LoginObject.pagescroll()
        self.LoginObject.searchValue(searchKey)
        self.LoginObject.clickSearchValue()
        self.LoginObject.wait_for_presence_of_an_element(By.XPATH, "//h1[normalize-space()='Web API (official plugin)']")
        self.LoginObject.clickLogout()
        
        



