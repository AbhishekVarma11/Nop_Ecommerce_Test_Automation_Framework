import time
from Pageobjects.LoginPage import LoginPage
from selenium import webdriver
import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLutilities
class Test_002_DDT_Login:
    baseUrl=ReadConfig.getApplicationURL()
    path='.//TestData/logintestdata.xlsx'
    logger=LogGen.loggen()
    def test_login_ddt(self,setup):
        self.logger.info('*****Test_002_DDT_Login*******')
        self.logger.info('*****verifing login using DATA *******')
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.lp=LoginPage(self.driver)
        self.rows=XLutilities.getRowCount(self.path,'Sheet1')
        print(self.rows)
        rest=[]
        for i in range(2,self.rows+1):
            self.user=XLutilities.readData(self.path,'Sheet1',i,1)
            self.password=XLutilities.readData(self.path,'Sheet1',i,2)
            self.exp=XLutilities.readData(self.path,'Sheet1',i,3)
            
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title=self.driver.title
            exp_title='Dashboard / nopCommerce administration'
            
            if act_title==exp_title:
                if self.exp=='pass':
                    self.logger.info("**passed**")
                    self.lp.clickLogout()
                    rest.append('pass')
                elif self.exp=='fail':
                    self.logger.info('**failed**')
                    rest.append('fail')
        
            elif act_title!=exp_title:
                if self.exp=='pass':
                    self.logger.info("**failed**")
                    self.lp.clickLogout()
                    rest.append('fail')
                elif self.exp=='fail':
                    self.logger.info('**passed**')
                    rest.append('pass')
        if 'fail' not in rest:
            self.logger.info('**Login ddt passed**')
            self.driver.close()
            assert True
        else:
            self.logger.info('**login ddt failed')
            self.driver.close()
            assert False         
        self.logger.info('** end of login ddt **')
        self.logger.info('***completed est_002_DDT_Login***')
        