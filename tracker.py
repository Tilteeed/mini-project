"""
Модуль для учета личных расходов.
Реализует функции добавления, получения и анализа расходов.
"""

# Финал
expenses = []


def add_expense(amount: float, category: str, description: str = "") -> None:
    """
    Добавляет новый расход в список расходов.

    Args:
        amount: Сумма расхода (должна быть положительной)
        category: Категория расхода
        description: Описание расхода (необязательное)

    Raises:
        ValueError: Если сумма не положительная
    """
    if amount <= 0:
        raise ValueError("Сумма должна быть положительной")

    expense = {"amount": amount, "category": category, "description": description}
    expenses.append(expense)


def get_expenses() -> list[dict]:
    """
    Возвращает список всех расходов.

    Returns:
        Список словарей с расходами, каждый содержит:
        amount, category, description
    """
    return expenses.copy()


def get_total() -> float:
    """
    Подсчитывает общую сумму всех расходов.

    Returns:
        Общая сумма расходов
    """
    return sum(expense["amount"] for expense in expenses)


def get_by_category(category: str) -> list[dict]:
    """
    Фильтрует расходы по указанной категории.

    Args:
        category: Категория для фильтрации

    Returns:
        Список расходов в указанной категории
    """
    return [
        expense
        for expense in expenses
        if expense["category"].lower() == category.lower()
    ]
