"""
Модуль для учета личных расходов.
Реализует функции добавления, получения и анализа расходов.
"""

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
