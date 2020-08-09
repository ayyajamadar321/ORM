import pytest
from selenium import webdriver
from PageObjects.HomePage import HomePage
from TestData.homepage_data import HomePageData
from utilities.utiliti import base


class TestHomepage(base):

    def test_loginpage(self, get_data):
        homepage = HomePage(self.driver)
        homepage.get_username().send_keys(get_data["username"])
        homepage.get_password().send_keys(get_data["password"])
        homepage.get_submit().click()
        self.driver.save_screenshot('C:\\Users\\account.test\\PycharmProjects\\ORM Project\\screenshots\\filename2.png')
        print("User Logged in")

    @pytest.fixture(params=HomePageData.testHomepage_Data)  # use param whenever you send data
    def get_data(self, request):
        return request.param
