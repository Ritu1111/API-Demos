from webdriver.webDriver import Driver
import time


class UtilClass:

    def set_up(self):
        self.driver = Driver()

    def click(self,xpath):
        self.driver.instance.find_element_by_xpath(xpath).click()

    def visiblity(self,xpath):
        visible = self.driver.instance.find_element_by_xpath(xpath).is_displayed()
        return visible

    def wait(self):
        time.sleep(3)