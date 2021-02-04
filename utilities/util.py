from selenium import webdriver
import time
from ..base.selenium_driver import SeleniumDriver
from ..utilities import custom_logger as cl

class Util(SeleniumDriver):
    log = cl.customloger(logging.DEBUG)

    def sleep(self,sec,info=" "):
        if info is not None:
            self.log.info("Wait {} seconds for {}".format(sec,info))
        try:
            time.sleep(sec)
        except:
            self.log.error("Exception in sleep function")

    def VerifyPageTitle(self,titletoverify):
        actualtitle = self.getTitle()
        self.log.info("Title of the Page to verify: {}".format(titletoverify))
        self.log.info("Actual Title of the Page: {}".format(actualtitle))
        if titletoverify.lower() in actualtitle.lower():
            self.log.info("Title Verified")
            return True
        else:
            self.log.error("Title Error")
            return False