# Документация для модуля CustomersPage

## Описание
Модуль `CustomersPage` предназначен для работы со страницей взаимодействия с клиентами. Он содержит локаторы для элементов страницы и методы для выполнения различных операций, таких как сортировка клиентов и удаление клиентов по имени.

## Импортируемые модули
- `average_str_len`: Функция для вычисления средней длины строк.
- `find_closest_el_by_len`: Функция для нахождения элемента, длина которого близка к заданной.
- `By`: Класс из библиотеки Selenium для определения локаторов.
- `WebElement`: Класс для представления веб-элемента.
- `BasePage`: Базовый класс для страниц, содержащий общие методы.

## Классы

### `CustomersPageLocators`
Класс, содержащий локаторы для элементов на странице взаимодействия с клиентами.
- `BTN_FirstName_CSS`: Локатор кнопки для сортировки по имени (CSS).
- `Customers_Table_CSS`: Локатор таблицы клиентов (CSS).
- `BTN_FirstName_XPATH`: Локатор кнопки для сортировки по имени (XPath).
- `Customers_Table_XPATH`: Локатор таблицы клиентов (XPath).

### `CustomersPage`
Класс для работы со страницей взаимодействия с клиентами, наследующий `BasePage`.

#### Методы
- `__init__(driver)`: Инициализация страницы взаимодействия с клиентами. Загружает URL страницы.
  
- `sort_by_fname()`: 
  Сортирует клиентов по имени (First Name).
  
- `_get_table_rows() -> list[WebElement]`: 
  Получает строки таблицы клиентов.
  - **Возвращает**: Список строк таблицы.

- `get_fnames() -> list[str]`: 
  Получает имена (First Name) клиентов из таблицы.
  - **Возвращает**: Список имен (First Name) клиентов.

- `remove_customer(first_name: str) -> None`: 
  Удаляет клиента по имени (First Name).
  - **Аргументы**:
    - `first_name`: Имя клиента для удаления.

- `remove_customer_with_avg_fname_len()`: 
  Удаляет клиента с именем, длина которого близка к средней длине имен. Выводит сообщение о удалении клиента.

## Примечания
- Убедитесь, что все необходимые зависимости установлены для корректной работы модуля.
- Модуль использует Selenium для автоматизации взаимодействия с веб-страницей и включает функции для работы с данными клиентов.