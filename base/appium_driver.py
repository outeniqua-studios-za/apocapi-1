from appium import webdriver
import utilities.custom_logger as cl
import logging
from traceback import print_stack


class SeleniumDriver():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
