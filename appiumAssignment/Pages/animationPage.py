from utility.utills import UtilClass
from utility.locators import readLocators
import utility.custom_logger as cl
import logging

class HideAnimationPage:
    log = cl.customLogger(logging.DEBUG)
    def setup_animation_hide_show(self):
        self.Hide_show = UtilClass()
        self.Hide_show.set_up()
        self.Hide_show.click(readLocators.read_xpaths('animationPage','Animation'))
        self.Hide_show.wait()
        self.Hide_show.click(readLocators.read_xpaths('animationPage','HideShowAnimations'))

    def setup_animation_hide(self):
        self.Hide_show.wait()
        self.Hide_show.click(readLocators.read_xpaths('animationPage','btn0'))
        self.Hide_show.click(readLocators.read_xpaths('animationPage','btn1'))
        self.Hide_show.click(readLocators.read_xpaths('animationPage','btn2'))
        self.Hide_show.click(readLocators.read_xpaths('animationPage','btn3'))

    def setup_animation_show(self):
        self.Hide_show.click(readLocators.read_xpaths('animationPage','showBtn'))
        self.Hide_show.wait()

    def visible(self):
        btn0= self.Hide_show.visiblity(readLocators.read_xpaths('animationPage','btn0'))
        btn1= self.Hide_show.visiblity(readLocators.read_xpaths('animationPage','btn1'))
        btn2= self.Hide_show.visiblity(readLocators.read_xpaths('animationPage','btn2'))
        btn3= self.Hide_show.visiblity(readLocators.read_xpaths('animationPage','btn3'))
        return btn0,btn1,btn2,btn3
