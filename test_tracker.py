import pytest
from tracker import add_expense, get_expenses, get_total, get_by_category


# Финал
@pytest.fixture(autouse=True)
def clear_expenses():
    from tracker import expenses

    expenses.clear()


def test_add_expense():
    """Тестирование добавления расходов."""
    add_expense(100, "Еда", "Обед")
    add_expense(200, "Транспорт")

    expenses = get_expenses()
    assert len(expenses) == 2
    assert expenses[0]["amount"] == 100
    assert expenses[0]["category"] == "Еда"
    assert expenses[0]["description"] == "Обед"
    assert expenses[1]["description"] == ""


def test_add_negative_expense():
    """Тестирование обработки отрицательной суммы."""
    with pytest.raises(ValueError):
        add_expense(-50, "Еда")


def test_get_total():
    """Тестирование подсчета общей суммы."""
    add_expense(300, "Развлечения")
    assert get_total() == 300
    add_expense(150, "Еда")
    assert get_total() == 450


def test_get_by_category():
    """Тестирование фильтрации по категории."""
    add_expense(100, "Еда")
    add_expense(200, "Транспорт")
    add_expense(150, "Еда")

    food_expenses = get_by_category("Еда")
    assert len(food_expenses) == 2
    assert sum(e["amount"] for e in food_expenses) == 250
    assert len(get_by_category("еДа")) == 2


def test_get_expenses_copy():
    """Тестирование, что возвращается копия списка."""
    original = get_expenses()
    original.append({"amount": 999, "category": "Тест"})
    assert len(get_expenses()) == 0
