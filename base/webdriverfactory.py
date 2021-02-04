#This file is used to assign chrome driver and load expedia webpage.

#import os
from selenium import webdriver


class Webdriverfactory():

    def __init__(self,browser):
        self.browser = browser

    def getdriverInstance(self):
        baseurl = "https://www.expedia.com/"
        driver = webdriver.Chrome(executable_path="C:\\expediaproject\\Chromedriver\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseurl)
        return driver