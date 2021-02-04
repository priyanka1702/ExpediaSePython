#This file is used to test the functionality of Flights option on expedia page.

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
from base.selenium_driver import SeleniumDriver
from utilities import custom_logger as cl
import logging

class ExpediaPage(SeleniumDriver):

    log = cl.customloger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    _flight_btn = "//span[contains(text(),'Flights')]"
    _fromfield = "//button[starts-with(@aria-label,'Leaving from')]"
    _selectfrom = "//strong[contains(text(),'{0}')]"
    _tofield = "//button[starts-with(@aria-label,'Going to')]"
    _selectto = "//strong[contains(text(),'{0}')]"
    _search = "//button[@data-testid='submit-button']"
    _selectdep = "d1-btn"
    _retdate = "d2-btn"

    def clicktab(self,locator,loctype):
        self.elementClick(locator,loctype)

    def enterdata(self,data,locator,loctype):
        self.sendKeys(data,locator,loctype)

    def dateselection(self,ddate,locator,loctype):
        self.selectdate(ddate,locator,loctype)

    def trip_selection(self,key,option,locator,loctype):
        self.selecttrip(key,option,locator,loctype)
        self.sleep(2)

    def searchtest(self,_fromloc="",_toloc="",dep_date="",ret_date="",option=""):

        self.clicktab(self._flight_btn,"xpath")
        self.enterdata(_fromloc,self._fromfield,"xpath")
        self.clicktab(self._selectfrom.format(_fromloc),"xpath")
        self.enterdata(_toloc,self._tofield,"xpath")
        self.clicktab(self._selectto.format(_toloc),"xpath")
        self.dateselection(dep_date,self._selectdep,"id")
        self.dateselection(ret_date,self._retdate,"id")
        self.clicktab(self._search,"xpath")

    def nonstopOption(self,locator,loctype):
        nonstop_option = self.Explicitwaitfunc(locator,loctype)
        if nonstop_option is not None:
            return True
        else:
            return False

    def verifytitle(self):
        return self.VerifyPageTitle("BLR to DEL flights")

    def invalidloc(self,locator,loctype):
        invalidalert = self.elepresentchk(locator,loctype)
        return invalidalert

    def clearfields(self,locator,loctype):
        element = self.getelement(locator,loctype)
        element.clear()

    def homepage(self):
        self.backtohome()
