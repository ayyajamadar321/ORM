
from PageObjects.HomePage import HomePage
from PageObjects.MainPage import MainPage
from utilities.utiliti import base


class TestMainPage(base):

    def test_mainpage(self):
        homepage = HomePage(self.driver)
        homepage.get_username().send_keys("opensourcecms")
        homepage.get_password().send_keys("opensourcecms")
        homepage.get_submit().click()
        mainpage = MainPage(self.driver)
        self.verifyLogo()                                # Explicit wait till logo displayed
        logotest = mainpage.get_logo()
        print(logotest.is_displayed())
        assert logotest.is_displayed(), "Log is not available"      # assertion for logo
        mainpage.get_Logout().click()
        print("User Logged Out")