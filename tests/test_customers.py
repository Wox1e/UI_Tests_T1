"""Модуль с тестами для страницы Customers"""

import allure
import pytest

from pages.CustomersPage import CustomersPage


@allure.feature("Тестирование страницы Customers")
class TestCustomersPage:
    """Класс тестов страницы Customers"""

    @allure.story("Сортировка клиентов по имени (First Name)")
    def test_customers_sort(self, customers_page):
        """Проверяет корректность сортировки клиентов в обратном и прямом порядке."""

        before_sort = customers_page.get_fnames()
        customers_page.sort_by_fname()
        after_sort = customers_page.get_fnames()

        with allure.step("Проверка отсортированности в обратном порядке"):
            assert sorted(before_sort, reverse=True) == after_sort, f"Ожидалось: {sorted(before_sort, reverse=True)}, Получено: {after_sort}"

        with allure.step("Проверка отсортированности в прямом порядке"):
            customers_page.sort_by_fname()
            after_sort = customers_page.get_fnames()
            assert sorted(before_sort) == after_sort, f"Ожидалось: {sorted(before_sort)}, Получено: {after_sort}"

    @allure.story("Удаление клиента с длинной First Name, ближайшей к среднему значению длин всех First Name")
    def test_remove_particular_customer(self, customers_page):
        """Тест на удаление клиента с длиной First Name,
        ближайшей к среднему значению длин всех First Name.
        """
        before_remove = customers_page.get_fnames()
        customers_page.remove_customer_with_avg_fname_len()
        after_remove = customers_page.get_fnames()
        assert len(before_remove) - 1 == len(after_remove), "Клиент не был удален."

    @allure.story("Удаление всех оставшихся клиентов")
    def test_remove_all(self, customers_page):
        """Проверяет, что после удаления всех клиентов список клиентов пуст."""
        fnames = customers_page.get_fnames()
        for fname in fnames:
            customers_page.remove_customer(fname)
        fnames = customers_page.get_fnames()

        assert len(fnames) == 0, "Список клиентов не пуст."
