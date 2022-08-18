import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseDriver:
    def __init__(self,driver):
        self.driver = driver

    def pagescroll(self):
        pageLength = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight); var pageLength=document.body.scrollHeight;return pageLength;"
        )
        match=False
        while(match==False):
                lastCount = pageLength
                time.sleep(3)
                lenOfPage = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
                if lastCount==lenOfPage:
                    match=True
        time.sleep(3)

    def wait_for_presence_of_an_element(self, locator_type, locator):
        wait = WebDriverWait(self.driver,10)
        waitPage = wait.until(EC.presence_of_element_located((locator_type, locator)))
        return waitPage

    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver,10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element
