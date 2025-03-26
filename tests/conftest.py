import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def driver_setup():
    service = Service(executable_path="./drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.set_page_load_timeout(5)
    yield driver
    driver.quit()

