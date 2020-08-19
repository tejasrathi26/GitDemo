import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setUp")
class E2E:

    def test_E2ETest(self):

        shopButton = self.driver.find_element_by_css_selector("a[href*='shop']")
        self.driver.execute_script("arguments[0].click();", shopButton)

        products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        for product in products:
            productName = product.find_element_by_xpath("div/h4").text
            if productName == "Nokia Edge":
                product.find_element_by_xpath("div/button").click()
                break

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        name = self.driver.find_element_by_css_selector("div[class='media-body'] h4 a").text

        assert productName == name
        print("Success")

        self.driver.find_element_by_css_selector("button[class='btn btn-success']").click()
        self.driver.find_element_by_id("country").send_keys("ind")

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        self.driver.find_element_by_link_text("India").click()
        # by xpath ===== //div[@class='checkbox checkbox-primary']
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("input[type='submit']").click()

        SuccessMsg = self.driver.find_element_by_css_selector("div[class*='alert-success']").text
        assert "Success! Thank you!" in SuccessMsg

        self.driver.get_screenshot_as_file("Screen.png")


