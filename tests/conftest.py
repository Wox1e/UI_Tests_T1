"""Модуль с фикстурами для pytest"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.AddCustomerPage import AddCustomerPage
from pages.CustomersPage import CustomersPage

@pytest.fixture(scope="session")
def driver_setup():
    """Инициализация вебдрайвера для Chrome"""
    service = Service(executable_path="./drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.set_page_load_timeout(5)
    yield driver
    driver.quit()

@pytest.fixture()
def add_customer_page(driver_setup):
    """Инициализация драйвера из фикстуры"""
    add_customer_page = AddCustomerPage(driver_setup)
    return add_customer_page

@pytest.fixture()
def customers_page(driver_setup):
    """Инициализация драйвера из фикстуры"""
    customers_page = CustomersPage(driver_setup)
    return customers_page