from utility.utills import UtilClass
from utility.locators import readLocators
import utility.custom_logger as cl
import logging

class DisplayOptPage:
    log = cl.customLogger(logging.DEBUG)

    def setup_display_options(self):

        self.Display = UtilClass()
        self.Display.set_up()
        self.Display.click(readLocators.read_xpaths('displayOptionsPage','app'))
        self.Display.wait()
        self.Display.click(readLocators.read_xpaths('displayOptionsPage','actionBar'))
        self.Display.wait()
        self.Display.click(readLocators.read_xpaths('displayOptionsPage','displayOptions'))
        self.Display.wait()
        self.Display.click(readLocators.read_xpaths('displayOptionsPage','displayTitle'))
        self.Display.wait()

    def visible(self):
        title= self.Display.visiblity(readLocators.read_xpaths('displayOptionsPage','title'))
        return title

DisplayOptPage()