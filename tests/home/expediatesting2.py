# This file Tests the option selection functionality.
#
# from selenium import webdriver
# from base.selenium_driver import SeleniumDriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import *
# from selenium.webdriver.common.by import By
# import time
from pages.home.expedia_page2 import ExpediaPage2
from utilities.teststatus import Status
from utilities.read_data import getcsvdata
import unittest
import pytest
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("CLSetup_returnvalue","setup")
@ddt()
class Optionstesting(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def clsdemosetup2(self, CLSetup_returnvalue):
        self.optionselection = ExpediaPage2(self.driver)
        self.ts2 = Status(self.driver)

    @pytest.mark.run(order=3)
    @data(*getcsvdata("C:\\expediaproject\\Project1_LetsKodeIt\\expediatestdata2.csv"))
    @unpack
    def test_search(self, fromlocation2, tolocation2, depdate2, arrdate2):
        self.optionselection.searchtest2(fromlocation2, tolocation2, depdate2, arrdate2)
        selectiondict = {"Roundtrip": "Multi-city", "Economy": "First Class", "Airlines": "Air India"}
        self.optionselection.options_1_Trip(selectiondict)
        tobefound2 = self.optionselection.airlineoption("//div[contains(text(),'Air India')]","xpath")
        self.ts2.finalresult("test_search",tobefound2,"Air line option selected")