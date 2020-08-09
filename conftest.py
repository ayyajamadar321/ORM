import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

from TestData.homepage_data import HomePageData
from utilities.readProperties import ReadConfig


@pytest.fixture(scope="class")
def setup(request):
    browserName = "chrome"

    if browserName == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())

    elif browserName == 'firefox':
        driver = webdriver.Chrome(executable_path=GeckoDriverManager.install())

    elif browserName == 'ie':
        driver = webdriver.Chrome(IEDriverManager().install())

    else:
        print("Please select the browser")

    driver.get(ReadConfig.getApplicationUrl())
    print(driver.title)
    driver.set_window_size(1000, 694)
    driver.delete_all_cookies()
    request.cls.driver = driver
    yield
    driver.close()



