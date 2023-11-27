from Pageobjects.LoginPage import LoginPage
from selenium import webdriver
import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseUrl=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()
    def test_homePageTitle(self,setup):
        self.logger.info('*****Test_001_Login*******')
        self.logger.info('*****verifying the Home page*******')
        self.driver=setup
        self.driver.get(self.baseUrl)
        act_title=self.driver.title       
        if act_title=="Your store. Login":
            assert True
            self.logger.info('*****Home Page Title test is Passed*******')
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.logger.error('*****Home Page Title test is Failed*****')
            assert False
        self.driver.close()
    def test_login(self,setup):
        self.logger.info('*****verifing login*******')
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        
        if act_title=='Dashboard / nopCommerce administration':
            self.logger.info('*****login sucessful *******')
            assert True
            self.driver.close() 
        else:
            self.logger.error('*****login failed*******')
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            assert False
                    
        