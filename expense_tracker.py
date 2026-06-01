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
    """Заглушка для добавления расхода."""
    raise NotImplementedError("Функция добавления расхода пока не реализована")


def format_expenses(expenses: list[dict[str, Any]]) -> list[str]:
    """Заглушка для форматирования списка расходов."""
    raise NotImplementedError("Вывод списка расходов пока не реализован")


def calculate_total(expenses: list[dict[str, Any]]) -> float:
    """Заглушка для подсчета общей суммы."""
    raise NotImplementedError("Подсчет общей суммы пока не реализован")


def category_statistics(expenses: list[dict[str, Any]]) -> dict[str, float]:
    """Заглушка для статистики по категориям."""
    raise NotImplementedError("Статистика пока не реализована")


def delete_expense(expenses: list[dict[str, Any]], index: int) -> dict[str, Any]:
    """Заглушка для удаления расхода."""
    raise NotImplementedError("Удаление расхода пока не реализовано")
