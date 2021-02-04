#This file is used to test the functionality of Stays option on expedia page.
from base.selenium_driver import SeleniumDriver
from utilities import custom_logger as cl
import logging

class ExpediaPage3(SeleniumDriver):
    log = cl.customloger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    _stays_btn = "//li//span[contains(text(),'Stays')]" #XPATH
    _goingto = "uitk-faux-input" #CLASS NAME
    _selectloc = "//strong[contains(text(),'{0}')]" #XPATH
    _checkin = "d1-btn" #ID
    _checkout = "d2-btn"  #ID
    _search3 = "//button[contains(text(),'Search')]" #XPATH
    _travelers = "undefined__btn" #ID
    _adultminus = "//div[@data-stid='room-count']/div[1]/div/button[1]" #XPATH
    _adultsplus = "//div[@data-stid='room-count']/div[1]/div/button[2]" #XPATH
    _childrenplus = "//div[@data-stid='room-count']/div[2]/div/button[2]" #XPATH
    _addanotherroom = "//button[@data-stid='add-room']" #XPATH
    _donetravelers = "//button[@data-stid='apply-room-picker']" #XPATH
    _spa = "popularFilter-0-SPA_ON_SITE" #ID

    def clicktab3(self, locator, loctype):
        self.elementClick(locator,loctype)

    def enterdata3(self, data, locator, loctype):
        self.sendKeys(data,locator,loctype)

    def dateselection3(self, date, locator, loctype):
        self.selectdate(date,locator,loctype)

    def searchtest3(self,_goingloc="",_checkindate="",_checkoutdate=""):

        self.clicktab3(self._stays_btn, "xpath")
        self.enterdata3(_goingloc, self._goingto, "classname")
        self.clicktab3(self._selectloc.format(_goingloc), "xpath")
        self.dateselection3(_checkindate, self._checkin, "id")
        self.dateselection3(_checkoutdate, self._checkout, "id")
        self.clicktab3(self._search3, "xpath")

    def spaoption(self,locator,loctype):
        spa_option = self.Explicitwaitfunc(locator,loctype)
        if spa_option is not None:
            return True
        else:
            return False

