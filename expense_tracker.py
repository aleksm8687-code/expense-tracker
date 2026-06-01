"""Логика консольного приложения для учета личных расходов."""

import json
import os
from typing import Any

FILE_NAME = "expenses.json"


def load_expenses(file_name: str = FILE_NAME) -> list[dict[str, Any]]:
    """Загружает расходы из JSON-файла."""
    if not os.path.exists(file_name):
        return []

    with open(file_name, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            return data if isinstance(data, list) else []
        except json.JSONDecodeError:
            return []


def save_expenses(expenses: list[dict[str, Any]], file_name: str = FILE_NAME) -> None:
    """Сохраняет расходы в JSON-файл."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(expenses, file, ensure_ascii=False, indent=4)


def add_expense(expenses: list[dict[str, Any]], category: str, description: str, amount: float, date: str) -> list[dict[str, Any]]:
    """Добавляет новый расход в список и возвращает обновленный список."""
    category = category.strip()
    description = description.strip()
    date = date.strip()

    if not category or not description or not date:
        raise ValueError("Категория, описание и дата не должны быть пустыми")

    if amount <= 0:
        raise ValueError("Сумма должна быть больше нуля")

    expense = {
        "category": category,
        "description": description,
        "amount": float(amount),
        "date": date,
    }

    expenses.append(expense)
    return expenses


def format_expenses(expenses: list[dict[str, Any]]) -> list[str]:
    """Возвращает список строк для вывода расходов."""
    result = []

    for index, expense in enumerate(expenses, start=1):
        result.append(
            f"{index}. {expense['date']} | "
            f"{expense['category']} | "
            f"{expense['description']} | "
            f"{expense['amount']} тг"
        )

    return result


def calculate_total(expenses: list[dict[str, Any]]) -> float:
    """Считает общую сумму расходов."""
    return sum(float(expense["amount"]) for expense in expenses)


def category_statistics(expenses: list[dict[str, Any]]) -> dict[str, float]:
    """Считает сумму расходов по каждой категории."""
    stats: dict[str, float] = {}

    for expense in expenses:
        category = expense["category"]
        stats[category] = stats.get(category, 0) + float(expense["amount"])

    return stats


def delete_expense(expenses: list[dict[str, Any]], index: int) -> dict[str, Any]:
    """Заглушка для удаления расхода."""
    raise NotImplementedError("Удаление расхода пока не реализовано")
