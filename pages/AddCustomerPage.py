"""Модуль для работы с AddCustomerPage и её локаторами"""

from selenium.webdriver.common.by import By

from helpers.utils import generate_str_digit, code_to_letter
from pages.BasePage import BasePage


class AddCustomerPageLocators:
    """Локаторы для элементов на странице добавления клиента."""
    BTN_AddCustomer_CSS = (By.CSS_SELECTOR, "button.btn:nth-child(4)")
    INPUT_FirstName_CSS = (By.CSS_SELECTOR, "div.form-group:nth-child(1) > input:nth-child(2)")
    INPUT_PostCode_CSS = (By.CSS_SELECTOR, "div.form-group:nth-child(3) > input:nth-child(2)")
    INPUT_LastName_CSS = (By.CSS_SELECTOR, "div.form-group:nth-child(2) > input:nth-child(2)")

    BTN_AddCustomer_XPATH = (By.XPATH, "//button[contains(@class, 'btn') and position()=4]")
    INPUT_FirstName_XPATH = (By.XPATH, "//div[@class='form-group'][1]//input")
    INPUT_PostCode_XPATH = (By.XPATH, "//div[@class='form-group'][3]//input")
    INPUT_LastName_XPATH = (By.XPATH, "//div[@class='form-group'][2]//input")

class AddCustomerPage(BasePage):
    """Класс для работы со страницей добавления клиента."""

    def __init__(
        self,
        driver,
        url="https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust",
    ):
        """Инициализация страницы добавления клиента."""
        super().__init__(driver)
        self.post_code = self._generate_post_code()
        self.base_url = url
        self.driver.get(self.base_url)

    def _generate_post_code(self) -> str:
        """Генерирует случайный Post Code."""
        return generate_str_digit(10)

    def _generate_first_name(self, post_code: str) -> str:
        """Генерирует FirstName на основе PostCode."""
        digits = []
        for i in range(0, len(post_code) - 1, 2):
            digits.append(post_code[i : i + 2])

        f_name = ""
        for digit in digits:
            f_name += code_to_letter(int(digit))
        return f_name

    def _generate_last_name(self) -> str:
        """Генерирует LastName на основе PostCode."""
        return self._generate_first_name(self._generate_post_code())

    def click_add_customer_button(self) -> None:
        """Нажимает на кнопку добавления клиента."""
        element = self.find_element(AddCustomerPageLocators.BTN_AddCustomer_CSS)
        self.click_on_element(element)

    def fill_post_code(self) -> None:
        """Заполняет поле PostCode сгенерированными данными"""
        element = self.find_element(AddCustomerPageLocators.INPUT_PostCode_XPATH)
        self.fill_element(element, self.post_code)

    def fill_post_code_by_value(self, value:str) -> None:
        """Заполняет поле PostCode, строкой, переданной в функцию"""
        self.post_code = value
        self.fill_post_code()

    def fill_fname_by_post_code(self) -> None:
        """Заполняет поле FirstName сгенерированными данными"""
        element = self.find_element(AddCustomerPageLocators.INPUT_FirstName_CSS)
        first_name = self._generate_first_name(self.post_code)
        self.fill_element(element, first_name)

    def fill_lname_by_post_code(self) -> None:
        """Заполняет поле LastName сгенерированными данными"""
        last_name = self._generate_last_name()
        element = self.find_element(AddCustomerPageLocators.INPUT_LastName_XPATH)
        self.fill_element(element, last_name)

    def fill_lname_by_value(self, value:str) -> None:
        """Заполняет поле Last Name, строкой, переданной в функцию"""
        element = self.find_element(AddCustomerPageLocators.INPUT_LastName_XPATH)
        self.fill_element(element, value)

    def fill_fname_by_value(self, value:str) -> None:
        """Заполняет поле First Name, строкой, переданной в функцию"""
        element = self.find_element(AddCustomerPageLocators.INPUT_FirstName_CSS)
        self.fill_element(element, value)