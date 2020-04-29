from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class HomePage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _link_home = "home"
    _blurb_container = "blurb"
    _social_github = "social_github"
    _social_linkedin = "social_linkedin"
    _social_twitter = "social_twitter"
    _email_button = "email"

    def verifyGithubSocialLinkExists(self):
        result = self.isElementPresent(self._social_github)
        return result

    def verifyLinkedInSocialLinkExists(self):
        result = self.isElementPresent(self._social_twitter)
        return result

    def verifyTwitterSocialLinkExists(self):
        result = self.isElementPresent(self._social_twitter)
        return result

    def verifyEmailButtonExist(self):
        result = self.isElementPresent(self._email_button)
        return result

    def verifyPageLoadSuccessful(self):
        result = self.isElementPresent(self._email_button)
        return result

    def clickTwitterSocialLink(self):
        self.elementClick(self._social_twitter)
