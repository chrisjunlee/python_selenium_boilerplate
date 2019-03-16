import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class DistTest01:

    def test_InputForm(self):

        mainMenu = self.driver.find_element_by_xpath("//li/a[contains(text(), 'Input Forms')]")
        mainMenu.click()

        subMenu = self.driver.find_element_by_xpath("//li/a[contains(text(), 'Simple Form Demo')]")
        subMenu.click()

        # finding "Single input form" input text field by id. And sending keys(entering data) in it.
        eleUserMessage = self.driver.find_element_by_id("user-message")
        eleUserMessage.clear()
        eleUserMessage.send_keys("Test Python")

        # finding "show your message" button element by css selector using both id and class name. and clicking it.
        eleShowMsgBtn=self.driver.find_element_by_css_selector('#get-input > .btn')
        eleShowMsgBtn.click()

        # checking whether the input text and output text are same using assertion.
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'display')))
        eleYourMsg=self.driver.find_element_by_id("display")
        assert "Test Python" in eleYourMsg.text
