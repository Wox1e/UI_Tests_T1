from pages.AddCustomerPage import AddCustomerPage
from pages.CustomersPage import CustomersPage

import pytest
import allure
from selenium import webdriver



@allure.feature('Customers Page Tests')
class TestCustomersPage:

    @pytest.fixture(autouse=True)
    def setup(self, driver_setup):
        self.driver = driver_setup
        self.customers_page = CustomersPage(self.driver)

    @allure.story("Сортировка клиентов по имени (First Name)")
    def test_customers_sort(self):
        before_sort = self.customers_page.get_fnames()
        self.customers_page.sort_by_fname()
        after_sort = self.customers_page.get_fnames()
        
        with allure.step("Проверка отсортированности в обратном порядке"):
            assert sorted(before_sort, reverse=True) == after_sort

        with allure.step("Проверка отсортированности в прямом порядке"):
            self.customers_page.sort_by_fname()
            after_sort = self.customers_page.get_fnames()
            assert sorted(before_sort, reverse=False) == after_sort

    @allure.story("Удаление клиента с длинной First Name, ближайшей к среднему значению длин всех First Name")
    def test_remove_particular_customer(self):
        self.customers_page.remove_customer_with_avg_fname_len()

        ## Сделать проверку !!
    


@allure.feature('Тесты страницы Add Customer')
class TestAddCustomerPage:

    @pytest.fixture(autouse=True)
    def setup(self, driver_setup):
        self.driver = driver_setup
        self.add_customer_page = AddCustomerPage(self.driver)

    @allure.story('Тестирование добавления нового клиента')
    def test_add_customer_page(self):
        with allure.step("Заполнение поля First Name"):
            self.add_customer_page.fill_first_name()

        with allure.step("Заполнение поля Last Name"):
            self.add_customer_page.fill_last_name()

        with allure.step("Заполнение поля Post Code"):
            self.add_customer_page.fill_post_code()

        with allure.step("Нажатие на кнопку Add Customer"):
            self.add_customer_page.click_add_customer_button()

        with allure.step("Проверка появления алерта"):
            assert self.add_customer_page.is_alert_appeared(2)
        

