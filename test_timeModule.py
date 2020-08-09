import time

from selenium.webdriver import ActionChains

from PageObjects.HomePage import HomePage
from PageObjects.MainPage import MainPage
from PageObjects.TimePage import TimePage
from utilities.utiliti import base


class TesttimeModule(base):

    def test_timemodule(self):
        pass

        # homepage = HomePage(self.driver)
        # homepage.get_username().send_keys("opensourcecms")
        # homepage.get_password().send_keys("opensourcecms")
        # homepage.get_submit().click()
        #
        # # mainpage = MainPage(self.driver)
        # # self.verifyLogo()                                # Explicit wait till logo displayed
        # # logotest = mainpage.get_logo()
        # # print(logotest.is_displayed())
        # # assert logotest.is_displayed(), "Log is not available"      # assertion for logo
        # # mainpage.get_Logout().click()
        # # print("User Logged Out")
        #
        # timemodule = TimePage(self.driver)
        # # timemodule.get_time().click()
        # self.actionClass(timemodule.get_time()).perform()
        # time.sleep(3)
        # self.actionClass(timemodule.get_timesheet()).click().perform()
        # print("You successfully click on time module")
        # self.driver.switch_to.frame(timemodule.get_ifarme())
        # time.sleep(3)
        # timemodule.get_empname().clear()
        # timemodule.get_empname().send_keys("ajju")
        # time.sleep(3)
        # timemodule.get_viewbutton().click()
        # time.sleep(3)
        # assert timemodule.get_msgfailure().text == "No Employees Available"