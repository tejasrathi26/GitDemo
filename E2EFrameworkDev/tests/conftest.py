import pytest
from selenium import webdriver
# use request instance and instead of using return use "request.cls.driver = driver" which means
# class driver object to be returned


@pytest.fixture(scope="class")
def setUp(request):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path="F:\\chromedriver_win32 (1)\chromedriver.exe", options=chrome_options)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()