from selenium import webdriver

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.maximize_window()
driver.get("http://www.seleniumeasy.com/test/basic-first-form-demo.html")
assert "Selenium Easy Demo - Simple Form to Automate using Selenium" in driver.title

test_message = "Test message from python selenium"
eleUserMessage = driver.find_element_by_id("user-message")
eleUserMessage.clear()
eleUserMessage.send_keys(test_message)

eleShowMsgBtn=driver.find_element_by_css_selector('#get-input > .btn')
eleShowMsgBtn.click()

eleYourMsg=driver.find_element_by_id("display")
assert test_message in eleYourMsg.text
driver.close()
