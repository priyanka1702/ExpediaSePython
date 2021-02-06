# This file Tests the Flights functionality of Expedia page.


# from selenium import webdriver
# from base.selenium_driver import SeleniumDriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import *
# from selenium.webdriver.common.by import By
# import time
from pages.home.expedia_page import ExpediaPage
from utilities.teststatus import Status
from utilities.read_data import getcsvdata
import unittest
import pytest
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("CLSetup_returnvalue","setup")
@ddt()
class TestingLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def clsdemosetup(self, CLSetup_returnvalue):
        self.searchloc = ExpediaPage(self.driver)
        self.ts = Status(self.driver)

    def setUp(self):
        self.driver.get("https://www.expedia.com/")

    @pytest.mark.run(order=1)
    @data(*getcsvdata("C:\\expediaproject\\Project1_LetsKodeIt\\expediatestdata.csv"))
    @unpack
    def test_valid(self,fromlocation,tolocation,depdate,arrdate):
        self.searchloc.searchtest(fromlocation, tolocation, depdate, arrdate)
        tobefound = self.searchloc.nonstopOption("//div[@data-test-id='stops-0-label']", "xpath")
        self.ts.finalresult("test_valid",tobefound,"Non-stop option verified")

    @pytest.mark.run(order=1)
    def test_invalid(self):
        self.searchloc.searchtest("Bengaluru", "ibibibibibibibib")
        errorresult = self.searchloc.invalidloc("//div[contains(text(),'Search by city or airport')]", "xpath")

        self.ts.finalresult("test_invalid",errorresult,"Error message Verified")
