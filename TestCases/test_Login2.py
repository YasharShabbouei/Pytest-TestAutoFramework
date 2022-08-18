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
    
    # 1) uncomments theses lines, remove parametrize, and add self. to email, password and searchKey
    """ email = "admin@yourstore.com"
    password = "admin"
    searchKey = "WEB API" """
    # 2) use pytest.parameteraize to do the above work, no need for self
    @pytest.mark.parametrize("email, password, searchKey",[("admin@yourstore.com","admin", "WEB API")])
    def test_login(self, email, password, searchKey):
        LoginObject = PageElements(self.driver)
        # Enter Email
        LoginObject.setUsername(email)
        # Enter Password
        LoginObject.setPassword(password)
        # Click on Login
        LoginObject.clickLogin()

        # Wait: interresting: it will until the page contains Dashbord then moves to the next line
        LoginObject.wait_for_presence_of_an_element(By.XPATH, "//h1[normalize-space()='Dashboard']")

        # scroll down (LoginObject is an object of PageElements which inherited the pagescroll from BaseDriver of the base_driver-py
        # so we dont need to inherit the BaseDriver here in the TestAutomationFramework class)
        LoginObject.pagescroll()

        # Type search key
        LoginObject.searchValue(searchKey)

        # Enter on the found search 
        LoginObject.clickSearchValue()

        #wait and Logout
        LoginObject.wait_for_presence_of_an_element(By.XPATH, "//h1[normalize-space()='Web API (official plugin)']")
        ####waitPage = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1[normalize-space()='Web API (official plugin)']")))
        LoginObject.clickLogout()





