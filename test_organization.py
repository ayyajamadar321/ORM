import time

from PageObjects.HomePage import HomePage
from PageObjects.MainPage import MainPage
from PageObjects.OrganizationPage import Organization
from utilities.readProperties import ReadConfig
from utilities.utiliti import base


class TestOrganization(base):

    def test_organization(self):
        homepage = HomePage(self.driver)
        homepage.get_username().send_keys(ReadConfig.getUsername())
        homepage.get_password().send_keys(ReadConfig.getPassword())
        homepage.get_submit().click()

        mainpage = MainPage(self.driver)
        self.explicitwait()                                      # Explicit wait till logo displayed
        logotest = mainpage.get_logo()
        print(logotest.is_displayed())
        assert logotest.is_displayed(), "Log is not available"  # assertion for logo
        # mainpage.get_Logout().click()
        # print("User Logged Out")

        organiz = Organization(self.driver)
        self.actionClass(organiz.get_topmenu()).perform()
        self.actionClass(organiz.get_admin()).perform()
        self.actionClass(organiz.get_organization()).perform()
        self.actionClass(organiz.get_genralinfo()).click().perform()
        time.sleep(2)
        self.driver.switch_to.frame(organiz.get_ifarme())
        verifypage = organiz.get_verifygeninfo()


        print(verifypage.text)
        assert verifypage.text == "General Information"
        assert "General" in verifypage.text                     # General is not present in ans
