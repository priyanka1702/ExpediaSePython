# This File is used to set the status of the Tests ran.
# Logs Successful message if Successful, captures error with screen shot otherwise.
from base.selenium_driver import SeleniumDriver
from utilities import custom_logger as cl
import logging

class Status(SeleniumDriver):

    log = cl.customloger(logging.INFO)

    def __init__(self,driver):
        super(Status,self).__init__(driver)
        self.resultlist = []

    def setresult(self,result,resultmsg):
        try:
            if result is not None:
                if result:
                    self.resultlist.append("PASS")
                    self.log.info("VERIFICATION SUCCESSFUL ::"+resultmsg)
                else:
                    self.resultlist.append("FAIL")
                    self.log.error("VERIFICATION FAILED ::" + resultmsg)
                    self.TakeScreenShot(resultmsg)
            else:
                self.resultlist.append("FAIL")
                self.log.error("VERIFICATION FAILED ::" + resultmsg)
                self.TakeScreenShot(resultmsg)
        except:
            self.resultlist.append("FAIL")
            self.log.info("EXCEPTION CASE")
            self.TakeScreenShot(resultmsg)


    def mark(self,result,resultmsg):
        self.setresult(result,resultmsg)

    def finalresult(self,testName,result,resultmsg):
        self.setresult(result, resultmsg)

        if "FAIL" in self.resultlist:
            self.log.error(testName+":" + "TEST FAILED")
            self.resultlist.clear()
            assert True == False
        else:
            self.log.info(testName+":" + "TEST SUCCESSFUL")
            self.resultlist.clear()
            assert True == True