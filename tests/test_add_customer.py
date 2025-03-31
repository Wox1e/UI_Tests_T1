"""Тесты для страницы AddCustomer"""

import allure
import pytest

from pages.AddCustomerPage import AddCustomerPage

@allure.feature("Тесты страницы Add Customer (корректные)")
class TestAddCustomerPageCorrect:
    """Класс корректных тестов для страницы Add Customer"""

    @allure.story("Тестирование добавления нового клиента")
    def test_add_customer(self, add_customer_page):
        """Тест на добавление одного корректного клиента"""
        with allure.step("Заполнение поля First Name"):
            add_customer_page.fill_fname_by_post_code()

        with allure.step("Заполнение поля Last Name"):
            add_customer_page.fill_lname_by_post_code()

        with allure.step("Заполнение поля Post Code"):
            add_customer_page.fill_post_code()

        with allure.step("Нажатие на кнопку Add Customer"):
            add_customer_page.click_add_customer_button()

        with allure.step("Проверка появления алерта"):
            assert add_customer_page.is_alert_appeared(2), "Пользователь не создан"

    @allure.story("Тестирование добавления 15 новых клиентов")
    def test_add_many_customers(self, add_customer_page):
        """Тест на добавление множества корректных клиентов"""
        for _ in range(15):
            self.test_add_customer(add_customer_page)

@allure.feature("Тесты страницы Add Customer (некорректные)")
class TestAddCustomerPage_incorrect():
    """Класс некорректных тестов для страницы Add Customer"""

    @allure.story("Тестирование добавления клиента с пустым first name")
    def test_empty_fname(self, add_customer_page):
        """Тест на добавление клиента с пустым полем First Name"""
        with allure.step("Заполнение поля First Name"):
            add_customer_page.fill_fname_by_value("")

        with allure.step("Заполнение поля Last Name"):
            add_customer_page.fill_lname_by_value("Testov")

        with allure.step("Заполнение поля Post Code"):
            add_customer_page.fill_post_code()

        with allure.step("Нажатие на кнопку Add Customer"):
            add_customer_page.click_add_customer_button()

        with allure.step("Проверка появления алерта"):
            assert not add_customer_page.is_alert_appeared(2), "Создан пользователь с пустым First Name"

    @allure.story("Тестирование добавления клиента с пустым last name")
    def test_empty_lname(self, add_customer_page):
        """Тест на добавление клиента с пустым полем Last Name"""
        with allure.step("Заполнение поля First Name"):
            add_customer_page.fill_fname_by_value("Test")

        with allure.step("Заполнение поля Last Name"):
            add_customer_page.fill_lname_by_value("")

        with allure.step("Заполнение поля Post Code"):
            add_customer_page.fill_post_code()

        with allure.step("Нажатие на кнопку Add Customer"):
            add_customer_page.click_add_customer_button()

        with allure.step("Проверка появления алерта"):
            assert not add_customer_page.is_alert_appeared(1), "Создан пользователь с пустым Last Name"

    @allure.story("Тестирование добавления клиента с пустым post code")
    def test_empty_postcode(self, add_customer_page):
        """Тест на добавление клиента с пустым полем Post Code"""
        with allure.step("Заполнение поля First Name"):
            add_customer_page.fill_fname_by_value("Test")

        with allure.step("Заполнение поля Last Name"):
            add_customer_page.fill_lname_by_value("Testov")

        with allure.step("Заполнение поля Post Code"):
            add_customer_page.fill_post_code_by_value("")

        with allure.step("Нажатие на кнопку Add Customer"):
            add_customer_page.click_add_customer_button()

        with allure.step("Проверка появления алерта"):
            assert not add_customer_page.is_alert_appeared(1), "Создан пользователь с пустым Post Code"

    @allure.story("Тестирование добавления клиента с некорректным first name")
    def test_incorrect_fname(self, add_customer_page):
        """Тест на добавление клиента с некорректным полем First Name"""
        with allure.step("Заполнение поля First Name"):
            add_customer_page.fill_fname_by_value("123")

        with allure.step("Заполнение поля Last Name"):
            add_customer_page.fill_lname_by_value("Testov")

        with allure.step("Заполнение поля Post Code"):
            add_customer_page.fill_post_code()

        with allure.step("Нажатие на кнопку Add Customer"):
            add_customer_page.click_add_customer_button()

        with allure.step("Проверка появления алерта"):
            assert not add_customer_page.is_alert_appeared(1), "Создан пользователь с некорректным First Name"

    @allure.story("Тестирование добавления клиента с некорректным last name")
    def test_incorrect_lname(self, add_customer_page):
        """Тест на добавление клиента с некорректным полем Last Name"""
        with allure.step("Заполнение поля First Name"):
            add_customer_page.fill_fname_by_value("Test")

        with allure.step("Заполнение поля Last Name"):
            add_customer_page.fill_lname_by_value("123")

        with allure.step("Заполнение поля Post Code"):
            add_customer_page.fill_post_code()

        with allure.step("Нажатие на кнопку Add Customer"):
            add_customer_page.click_add_customer_button()

        with allure.step("Проверка появления алерта"):
            assert not add_customer_page.is_alert_appeared(1), "Создан пользователь с некорректным Last Name"

    @allure.story("Тестирование добавления клиента с некорректным post code")
    def test_incorrect_postcode(self, add_customer_page):
        """Тест на добавление клиента с некорректным полем Post Code"""
        with allure.step("Заполнение поля First Name"):
            add_customer_page.fill_fname_by_value("Test")

        with allure.step("Заполнение поля Last Name"):
            add_customer_page.fill_lname_by_value("Testov")

        with allure.step("Заполнение поля Post Code"):
            add_customer_page.fill_post_code_by_value("not a numbers")

        with allure.step("Нажатие на кнопку Add Customer"):
            add_customer_page.click_add_customer_button()

        with allure.step("Проверка появления алерта"):
            assert not add_customer_page.is_alert_appeared(1), "Создан пользователь с некорректным Post Code"
