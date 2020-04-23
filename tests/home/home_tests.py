from selenium import webdriver

from pages.home.home_page import HomePage
from pages.home.login_page import LoginPage
import unittest
import pytest


class HomeTests(unittest.TestCase):

    def test_validHomePage(self):
        baseURL = "https://jonathanopperman.info/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        hp = HomePage(driver)
        result = sel
        assert result == True
        self.driver.quit()
