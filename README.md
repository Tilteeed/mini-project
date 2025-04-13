# Калькулятор расходов

Простой консольный калькулятор для учета личных расходов. Он будет позволять добавлять траты , выводить список, считать общую сумму и фильтровать по категории

## Функциональность

- Добавление расходов с указанием суммы, категории и описания
- Просмотр всех расходов
- Подсчет общей суммы расходов
- Фильтрация расходов по категории

## Запуск программы

1. Запустите файл main.py.

## Примеры использования

1. Добавление расхода:
Выберите действие: 1
Введите сумму: 1500
Введите категорию: Продукты
Введите описание (необязательно): Покупки на неделю

2. Просмотр всех расходов:
Выберите действие: 2
Продукты: 1500 - Покупки на неделю
Транспорт: 500 - Такси

3. Просмотр общей суммы:
Выберите действие: 3
Общая сумма расходов: 2000.00

4. Фильтрация по категории:
Выберите действие: 4
Введите категорию для фильтрации: продукты
Продукты: 1500 - Покупки на неделю

## Описание функций

### `add_expense(amount, category, description)`
Добавляет новый расход в список.  
Параметры:
- `amount` - сумма расхода (должна быть положительной)
- `category` - категория расхода
- `description` - необязательное описание

### `get_expenses()`
Возвращает список всех расходов в виде словарей.

### `get_total()`
Возвращает общую сумму всех расходов.

### `get_by_category(category)`
Возвращает расходы только из указанной категории (регистронезависимо).
