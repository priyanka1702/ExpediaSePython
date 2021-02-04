# This file Tests the Stays functionality of Expedia page.
from pages.home.expedia_page3 import ExpediaPage3
from utilities.teststatus import Status
from utilities.read_data import getcsvdata
import unittest
import pytest
from ddt import ddt,data,unpack

@pytest.mark.usefixtures("CLSetup_returnvalue","setup")
@ddt()
class StaysTesting(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def clsdemosetup3(self,CLSetup_returnvalue):
        self.staystest = ExpediaPage3(self.driver)
        self.ts3 = Status(self.driver)

    def setUp(self):
        self.driver.get("https://www.expedia.com/")


    @pytest.mark.run(order=4)
    @data(*getcsvdata("C:\\expediaproject\\Project1_LetsKodeIt\\expediatestdata3.csv"))
    @unpack
    def test_stays(self,going_to,check_in,check_out):
        self.staystest.searchtest3(going_to,check_in,check_out)
        tobefound3 = self.staystest.spaoption("//span[contains(text(),'View in a map')]","xpath")
        self.ts3.finalresult("test_stays",tobefound3,"View in a map option")