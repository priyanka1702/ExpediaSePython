# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.select import Select
# from traceback import print_stack
# import inspect
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from utilities import custom_logger as cl
import logging
import time
import os

class SeleniumDriver():

    log = cl.customloger(logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver

    def getbytype(self, loctype):
        # This method returns the By type.
        # Input: type of the locator in text.
        # Output: type of the locator.

        loctype = loctype.lower()
        if loctype == "id":
            return By.ID
        elif loctype == "xpath":
            return By.XPATH
        elif loctype == "name":
            return By.NAME
        elif loctype == "tagname":
            return By.TAG_NAME
        elif loctype == "classname":
            return By.CLASS_NAME
        elif loctype == "css":
            return By.CSS_SELECTOR
        elif loctype == "linktext":
            return By.LINK_TEXT
        elif loctype == "plinktext":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.info("*****Unsuppoted Loctype : {}*****".format(loctype))
        return False

    def getelement(self,locator,loctype="id"):
        # This method tries to find the element in the Webpage.
        # Input: Locator of the element and its type.
        # Output: return the element if found.
        #         Throws exception if not found.

        element = None
        try:
            loctype = loctype.lower()
            bytype = self.getbytype(loctype)
            element = self.driver.find_element(bytype,locator)
            self.log.info("*****Element Found*****")
        except:
            self.log.info("*****Element Not Found*****")
        return element

    def getelementlist(self,locator,loctype="id"):
        # This method return the list of elements.
        # Input: Locator of the element.
        # Output: List of elements.

        element = None
        try:
            loctype = loctype.lower()
            bytype = self.getbytype(loctype)
            element = self.driver.find_elements(bytype,locator)
            self.log.info("Element list Found with locator-{} and loctype-{}".format(locator,loctype))
        except:
            self.log.info("Element list Not Found with locator-{} and loctype-{}".format(locator,loctype))
        return element

    def elepresentchk(self,locator="",loctype="id",element=None):
        # This method check if the element is displayed.
        # Input: Locator of the element with its type.
        # Output: Return True if dispalyed and False if not.
        try:
            if locator:
                element = self.driver.find_element(loctype,locator)
            if element:
                self.log.info("Element Found with locator-{} and loctype-{}".format(locator,loctype))
                return True
            else:
                self.log.info("Element Not Foundwith locator-{} and loctype-{}".format(locator,loctype))
                return False
        except:
            self.log.info("*****Invalid Input*****")
            return False

    def elespresencechk(self,locator,loctype="id"):
        # This method checks if the list of the element is present.
        # Input: Locator for the elements and its type.
        # Output: True if list of Elements is non-empty, False otherwise.
        try:
            element = self.driver.find_elements(loctype,locator)
            if len(element) > 0:
                print("*****Elements Found*****")
                return True
            else:
                print("*****Elements Not Found*****")
                return False
        except:
            print("*****Invalid Input*****")
            return False

    def elementdisplayed(self,locator="",loctype="id",element=None):
        # This method checks if a element is displayed through a in-build function.
        # Input: Locator of the element with its type.
        # Output: True if dispalyed, False otherwise.
        isdiaplyed = False
        try:
            if locator:
                element = self.getelement(locator,loctype)
            if element:
                isdiaplyed = element.is_displayed()
                self.log.info("Element is displayed with locator-{} and loctype-{}".format(locator, loctype))
            else:
                self.log.info("Element is not displayed with locator-{} and loctype-{}".format(locator, loctype))
            return isdiaplyed
        except:
            self.log.info("Element is not displayed with locator-{} and loctype-{}".format(locator, loctype))
            return False


    def elementClick(self,locator="",loctype="id",element=None):
        # This method clicks on the element.
        # Input: Locator of the element with its type or the element itself.
        # Output: NA
        try:
            if locator:
                element = self.getelement(locator,loctype)
            element.click()
            self.log.info("Clicked on the Element - Locator:{} - LocType:{}".format(locator,loctype))
        except:
            self.log.info("Could not click on the Element - Locator:{} - LocType:{}".format(locator, loctype))
            #print_stack()

    def sendKeys(self,data,locator="",loctype="id",element=None):
        # This method enter data to the element.
        # Input: Data and Locator of the element with its type.
        # Output: NA
        try:
            if locator:
                element = self.getelement(locator,loctype)
            element.send_keys(data)
            self.log.info("Sent data on the Element - Locator:{} - LocType:{}".format(locator,loctype))
        except:
            self.log.info("Could not send data on the Element - Locator:{} - LocType:{}".format(locator, loctype))
            #print_stack()

    def selectdate(self,ddate,locator="",loctype=""):
        # This method selects date.
        # Input: Date and Locator of the element with its type.
        # Output: Selects date if provided date is valid else throws exception.
        try:
            self.elementClick(locator,loctype)
            datestoselect = self.driver.find_element_by_xpath("//div[@class='uitk-new-date-picker-month'][1]/table/tbody")
            validdates = datestoselect.find_elements_by_tag_name("button")
            for v in validdates:
                if ddate in str(v.get_attribute("aria-label")):
                    v.click()
                    break
            self.driver.find_element_by_xpath("//span[contains(text(),'Done')]").click()
            self.log.info("Selected date on the Element - Locator:{} - LocType:{}".format(locator, loctype))
        except:
            self.log.info("Could not Select date on the Element - Locator:{} - LocType:{}".format(locator, loctype))

    def selecttrip(self,key,option,locator,loctype):
        # This method selects required options for the Trip.
        # Input: Key- name of the option, option- to be selected option from the key.
        #        Locator of the element with its type.
        # Output: Selects specified option else throws exception.
        try:
            self.elementClick(locator, loctype)
            if key == "Roundtrip":
                selectoption = self.driver.find_element_by_xpath("//section/div/div[1]/div[1]/div[2]/div")
                options = selectoption.find_elements_by_tag_name("a")
            elif key == "Economy":
                selectoption = self.driver.find_element_by_xpath("//section/div/div[1]/div[3]/div[2]/div")
                options = selectoption.find_elements_by_tag_name("a")
            elif key == "Airlines":
                selectoption = self.driver.find_element_by_xpath("//section/div/div[1]/div[4]/div[2]/div")
                options = selectoption.find_elements_by_tag_name("a")
            for opt in options:
                self.log.info(opt.text)
                if option == opt.text:
                    opt.click()
                    break
            self.log.info("Selected option {} on the Element - Locator:{} - LocType:{}".format(option,locator, loctype))
        except:
            self.log.info("Could not Select option {} on the Element - Locator:{} - LocType:{}".format(option,locator, loctype))

    def getText(self,locator="",loctype="id",element=None,info=""):
        # This method returns the Text of the locator.
        # Input: Locator of the element with its type.
        # Output: Text of the Locator.

        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.getelement(locator,loctype)
            self.log.debug("Before finding Text")
            text = element.text
            self.log.debug("After finding element,size is {}".format(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innertext")
            if len(text) != 0:
                self.log.info("Getting text on element :{}".format(info))
                self.log.info("The text is {}".format(text))
                text = text.strip()
        except:
            self.log.error("Failed to get the Text {}".format(info))
            text = None
        return text

    def backtohome(self):
        # This method takes back to the previous page.
        # Input: NA
        # Output: Takes one step backwards.
        self.driver.back()
        self.log.info("Back to home page")

    def getTitle(self):
        # This method returns Title of the Webpage.
        # Input: NA
        # Output: Returns Title of the page.
        return self.driver.title

    def sleep(self,sec,info=" "):
        # This method sleep for the specified seconds.
        # Input: Seconds to sleep.
        # Output: Wait for specified seconds.
        if info is not None:
            self.log.info("Wait {} seconds for {}".format(sec,info))
        try:
            time.sleep(sec)
        except:
            self.log.error("Exception in sleep function")

    def VerifyPageTitle(self,titletoverify):
        # This method verifies the Title of the page with given title.
        # Input: Title to be Verified.
        # Output: True if Title matches with the Title of Webpage, False otherwise.
        actualtitle = self.getTitle()
        self.log.info("Title of the Page to verify: {}".format(titletoverify))
        self.log.info("Actual Title of the Page: {}".format(actualtitle))
        if titletoverify.lower() in actualtitle.lower():
            self.log.info("Title Verified")
            return True
        else:
            self.log.error("Title Error")
            return False

    def Explicitwaitfunc(self,locator,loctype="id",timeout=50,pf=1):
        # This method waits for a element to be clickable.
        # Input:Locator of the element with its type, timeout(maximum sec to wait) and poll frequency.
        # Output: Waits for the element to appear and to be able to click on that.
        element = None
        try:
            bytype = self.getbytype(loctype)
            self.log.info("Waiting for maximium :: {0} :: seconds for element to be clickable".format(timeout))
            wait = WebDriverWait(self.driver,timeout,poll_frequency=pf,
                                 ignored_exceptions=[NoSuchElementException,ElementNotSelectableException,
                                                     ElementNotVisibleException])
            element = wait.until(EC.element_to_be_clickable((bytype,locator)))
            self.log.info("Element appeared on the webpage")
            element.click()
        except:
            self.log.info("Element did not appeared on the webpage")
        return element

    def TakeScreenShot(self,resultmsg):
        # This method takes screenshot of the error during execution.
        # Input: Test of the error message.
        # Output: Screen shot which contains error message in its name.
        filename = resultmsg+"_"+str(round(time.time()*1000))+".png"
        scrsdir = "C:\\expediaproject\\Project1_LetsKodeIt\\screenshots\\"
        #scrsdir = "../screenshots/"
        relativefilename = scrsdir + filename
        currdir = os.path.dirname(__file__)
        destfile = os.path.join(currdir,relativefilename)
        destdir = os.path.join(currdir,scrsdir)


        try:
            if not os.path.exists(destdir):
                os.makedirs(destdir)

            self.driver.save_screenshot(destfile)
            self.log.info("***** Screen shot saved under: {} *****".format(destfile))
        except:
            self.log.info("***** Exception case *****")


    def scrolling(self,direction="up"):
        # This method scrolls the window.
        # Input: Direction of the scroll, either up or down.
        # Output: Scrolls the window based on the direction.

        if direction == "up":
            self.driver.execute_script("window.scrollBy(0,-1000);")
        if direction == "down":
            self.driver.execute_script("window.scrollBy(0,1000);")


    def scrollforelement(self,locator="",loctype="id",element=""):
        # This method scrolls the window to find the required locator.
        # Input: Locator of the element with its type.
        # Output: Scrolls the window to preferred locator.
        try:
            if locator:
                element = self.getelement(locator,loctype)
            self.driver.execute_script("arguments[0].scrollIntoView(true);",element)
            self.driver.execute_script("windows.scrollBy(0,-150);")
            self.log.info("Scrolled to the Element - Locator:{} - LocType:{}".format(locator, loctype))
        except:
            self.log.info("Could not Scrolled to the Element - Locator:{} - LocType:{}".format(locator, loctype))