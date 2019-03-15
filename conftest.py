import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def setup(request):
    driver = webdriver.Chrome("/usr/bin/chromedriver")
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    driver.get("http://seleniumeasy.com/test")
    driver.maximize_window()

    yield driver
    driver.close()
