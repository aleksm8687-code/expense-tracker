import pytest

from expense_tracker import add_expense, calculate_total, category_statistics, delete_expense


def test_add_expense():
    expenses = []

    updated = add_expense(expenses, "Еда", "Обед", 2500, "2026-06-01")

    assert len(updated) == 1
    assert updated[0]["category"] == "Еда"
    assert updated[0]["amount"] == 2500


def test_add_expense_rejects_empty_fields():
    with pytest.raises(ValueError):
        add_expense([], "", "Обед", 2500, "2026-06-01")


def test_add_expense_rejects_negative_amount():
    with pytest.raises(ValueError):
        add_expense([], "Еда", "Обед", -100, "2026-06-01")


def test_calculate_total():
    expenses = [
        {"category": "Еда", "description": "Обед", "amount": 2500, "date": "2026-06-01"},
        {"category": "Транспорт", "description": "Автобус", "amount": 120, "date": "2026-06-01"},
    ]

    assert calculate_total(expenses) == 2620


def test_category_statistics():
    expenses = [
        {"category": "Еда", "description": "Обед", "amount": 2500, "date": "2026-06-01"},
        {"category": "Еда", "description": "Кофе", "amount": 800, "date": "2026-06-02"},
        {"category": "Транспорт", "description": "Автобус", "amount": 120, "date": "2026-06-01"},
    ]

    assert category_statistics(expenses) == {"Еда": 3300, "Транспорт": 120}


def test_delete_expense():
    expenses = [
        {"category": "Еда", "description": "Обед", "amount": 2500, "date": "2026-06-01"},
        {"category": "Транспорт", "description": "Автобус", "amount": 120, "date": "2026-06-01"},
    ]

    removed = delete_expense(expenses, 2)

    assert removed["description"] == "Автобус"
    assert len(expenses) == 1


def test_delete_expense_invalid_index():
    with pytest.raises(IndexError):
        delete_expense([], 1)
