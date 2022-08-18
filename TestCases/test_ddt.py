import pytest
import sys
sys.path.append(r"C:\\Users\\yasha\\OneDrive\\Desktop\\Selenium\\testAutomationFramework")

from Pages.PageObjects import PageElements
from Utilities.userDefinedCode import read_data_from_excel as ReadExcel
from Base.base_driver import BaseDriver


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import softest
from ddt import ddt, unpack, data

  
@pytest.mark.usefixtures('setup')
@ddt
class TestLoginAndSearch(softest.TestCase):
    
    # 2) use pytest.parameteraize to do the above work, no need for self
    #@pytest.mark.parametrize("email, password, searchKey",[("admin@yourstore.com","admin", "WEB API")])
    @data(("admin@yourstore.com","admin", "WEB API"))
    @unpack
    def test_login(self, email, password, searchKey):
        LoginObject = PageElements(self.driver)
        LoginObject.loginTowebsite(email, password)
        LoginObject.pagescroll()
        LoginObject.searchValue(searchKey) 
        LoginObject.clickSearchValue()
        LoginObject.wait_for_presence_of_an_element(By.XPATH, "//h1[normalize-space()='Web API (official plugin)']")
        LoginObject.clickLogout()





