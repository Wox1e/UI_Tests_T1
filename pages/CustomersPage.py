"""Модуль для работы с классом CustomersPage и его локаторами"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from helpers.utils import average_str_len, find_closest_el_by_len
from pages.BasePage import BasePage


class CustomersPageLocators:
    """Локаторы для элементов на странице взаимодействия с клиентами."""

    BTN_FirstName_CSS = (By.CSS_SELECTOR, ".table > thead:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)")
    Customers_Table_CSS = (By.CSS_SELECTOR, ".table > tbody:nth-child(2)")

    BTN_FirstName_XPATH = (By.XPATH, "//table/thead/tr/td[1]/a")
    Customers_Table_XPATH = (By.XPATH, "//table/tbody")

class CustomersPage(BasePage):
    """Класс для работы со страницей взаимодействия с клиентами."""

    def __init__(self, driver):
        """Инициализация страницы взаимодействия с клиентами."""
        super().__init__(driver)
        self.base_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list"
        self.driver.get(self.base_url)

    def sort_by_fname(self):
        """Сортирует клиентов по имени (First Name)."""
        element = self.find_element(CustomersPageLocators.BTN_FirstName_CSS)
        self.click_on_element(element)

    def _get_table_rows(self) -> list[WebElement]:
        """Получает строки таблицы клиентов.

        Returns:
            list[WebElement]: Список строк таблицы.
        """
        table = self.find_element(CustomersPageLocators.Customers_Table_XPATH)
        rows = table.find_elements(By.TAG_NAME, "tr")
        return rows

    def get_fnames(self) -> list[str]:
        """Получает имена (First Name) клиентов из таблицы.
        Returns:
            list[str]: Список имен (First Name) клиентов.
        """
        rows = self._get_table_rows()
        fnames = [element.text.split(" ")[0] for element in rows]
        return fnames

    def remove_customer(self, first_name: str) -> None:
        """Удаляет клиента по имени (First Name).
        Args:
            first_name (str): Имя клиента для удаления.
        """
        rows = self._get_table_rows()

        for row in rows:
            fname = row.text.split(" ")[0]

            if fname == first_name:
                delete_btn = row.find_element(By.TAG_NAME, "button")
                self.click_on_element(delete_btn)
                return

    def remove_customer_with_avg_fname_len(self):
        """Удаляет клиента с именем, длина которого близка к средней длине имен."""
        fnames = self.get_fnames()
        target_fname = find_closest_el_by_len(fnames, average_str_len(fnames))
        self.remove_customer(target_fname)
        print(f"Клиент с именем = {target_fname} удален")
