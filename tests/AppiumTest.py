import unittest
from appium import webdriver


class MyTestCase(unittest.TestCase):
    dc = {}
    driver = None

    def setUp(self):
        self.dc['app'] = "D:\\Builds\\Test\\app-debug.apk"
        self.dc['appPackage'] = "com.experitest.ExperiBank"
        self.dc['appActivity'] = "LoginActivity"
        self.dc['platformName'] = 'Android'
        self.dc['deviceName'] = 'HMD Global Nokia 8 Sirocco'
        self.dc['noSign'] = 'true'
        self.dc['remoteAppsCacheLimit '] = 0

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)

    def testFirstAutomation(self):
        if len(self.driver.find_elements_by_xpath("//*[@text='OK']")) > 0:
            self.driver.find_elements_by_xpath("//*[@text='OK']").click()
        self.driver.find_elements_by_xpath("//*[@text='Username']").send_keys('company')
        self.driver.find_elements_by_xpath("//*[@text='Password']").send_keys('company')
        self.driver.find_elements_by_xpath("//*[@text='Login']").click()


if __name__ == '__main__':
    unittest.main()
