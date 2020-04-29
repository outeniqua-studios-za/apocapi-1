from selenium import webdriver
from pages.home.home_page import HomePage
import unittest
import pytest


class HomeTests(unittest.TestCase):

    def test_validHomePage(self):
        baseURL = "https://jonathanopperman.info/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        hp = HomePage(driver)

        hp.clickTwitterSocialLink()

        # self.driver.quit()
