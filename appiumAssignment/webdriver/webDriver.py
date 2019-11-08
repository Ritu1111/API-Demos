from appium import webdriver
import os


class Driver:

    def __init__(self):
        desired_cap = {
            "platformName": "Android",
            "deviceName": "Android Emulator",
            "appPackage": "com.example.android.apis",
            "appActivity": "com.example.android.apis.ApiDemos",
            "noReset": "true",
            "platformVersion": "7.1.1"
        }
        self.instance = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)