#This file is used to test the functionality of Flights option on expedia page and
# select option after the search is successful.
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
from base.selenium_driver import SeleniumDriver
from utilities import custom_logger as cl
import logging

class ExpediaPage2(SeleniumDriver):

    log = cl.customloger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    _flight_btn2 = "//span[contains(text(),'Flights')]"
    _fromfield2 = "//button[starts-with(@aria-label,'Leaving from')]"
    _selectfrom2 = "//strong[contains(text(),'{0}')]"
    _tofield2 = "//button[starts-with(@aria-label,'Going to')]"
    _selectto2 = "//strong[contains(text(),'{0}')]"
    _search2 = "//button[@data-testid='submit-button']"
    _selectdep2 = "d1-btn"
    _retdate2 = "d2-btn"
    # _Roundtrip_btn2 = "//button[@data-test-id='flights-trip-type-options-toggle']"
    # _travellers_btn2= "//button[@data-test-id='flights-travelers-options-toggle']"
    # _Economy_btn2 = "//button[@data-test-id='flights-cabin-class-options-toggle']"
    # _anyairline2 = "//button[@data-test-id='flights-airlines-options-toggle']"
    # _moreoptions2 = "//button[@data-test-id='flights-more-options-toggle']"
    choseoption2 = "//button[@data-test-id='flights-{0}-options-toggle']"

    def clicktab2(self, locator, loctype):
        self.elementClick(locator,loctype)

    def enterdata2(self, data, locator, loctype):
        self.sendKeys(data,locator,loctype)

    def dateselection2(self, date, locator, loctype):
        self.selectdate(date,locator,loctype)

    def trip_selection2(self, key, option, locator, loctype):
        self.selecttrip(key,option,locator,loctype)
        self.sleep(2)

    def searchtest2(self,_fromloc="",_toloc="",dep_date="",ret_date="",option=""):

        self.clicktab2(self._flight_btn2, "xpath")
        self.enterdata2(_fromloc, self._fromfield2, "xpath")
        self.clicktab2(self._selectfrom2.format(_fromloc), "xpath")
        self.enterdata2(_toloc, self._tofield2, "xpath")
        self.clicktab2(self._selectto2.format(_toloc), "xpath")
        self.dateselection2(dep_date, self._selectdep2, "id")
        self.dateselection2(ret_date, self._retdate2, "id")
        self.clicktab2(self._search2, "xpath")

    def options_1_Trip(self,selectiondict):
        for key in selectiondict:
            if key == "Roundtrip":
                type = "trip-type"
                self.trip_selection2(key, selectiondict[key], self.choseoption2.format(type), "xpath")
            elif key == "Economy":
                type = "cabin-class"
                self.trip_selection2(key, selectiondict[key], self.choseoption2.format(type), "xpath")
            elif key == "Airlines":
                type = "airlines"
                self.trip_selection2(key, selectiondict[key], self.choseoption2.format(type), "xpath")

    def airlineoption(self,locator,loctype):
        airline_option = self.Explicitwaitfunc(locator,loctype)
        if airline_option is not None:
            return True
        else:
            return False
