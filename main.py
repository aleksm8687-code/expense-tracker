"""Консольное приложение «Менеджер личных расходов»."""

from expense_tracker import (
    FILE_NAME,
    add_expense,
    calculate_total,
    category_statistics,
    delete_expense,
    format_expenses,
    load_expenses,
    save_expenses,
)


def show_menu() -> None:
    print("\nМенеджер личных расходов")
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Показать общую сумму расходов")
    print("4. Статистика по категориям")
    print("5. Удалить расход")
    print("6. Выход")


def handle_add_expense() -> None:
    expenses = load_expenses(FILE_NAME)

    category = input("Введите категорию расхода: ")
    description = input("Введите описание расхода: ")

    try:
        amount = float(input("Введите сумму расхода: "))
    except ValueError:
        print("Сумма должна быть числом")
        return

    date = input("Введите дату расхода в формате ГГГГ-ММ-ДД: ")

    try:
        updated_expenses = add_expense(expenses, category, description, amount, date)
    except ValueError as error:
        print(error)
        return

    save_expenses(updated_expenses, FILE_NAME)
    print("Расход добавлен")


def handle_show_expenses() -> None:
    expenses = load_expenses(FILE_NAME)

    if not expenses:
        print("Список расходов пуст")
        return

    for line in format_expenses(expenses):
        print(line)


def handle_show_total() -> None:
    expenses = load_expenses(FILE_NAME)
    total = calculate_total(expenses)
    print(f"Общая сумма расходов: {total} тг")


def handle_category_stats() -> None:
    expenses = load_expenses(FILE_NAME)

    if not expenses:
        print("Нет данных для статистики")
        return

    print("Статистика по категориям:")
    for category, total in category_statistics(expenses).items():
        print(f"{category}: {total} тг")


def handle_delete_expense() -> None:
    print("Удаление пока не реализовано")


def main() -> None:
    save_expenses(load_expenses(FILE_NAME), FILE_NAME)

    while True:
        show_menu()
        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            handle_add_expense()
        elif choice == "2":
            handle_show_expenses()
        elif choice == "3":
            handle_show_total()
        elif choice == "4":
            handle_category_stats()
        elif choice == "5":
            handle_delete_expense()
        elif choice == "6":
            print("Выход из программы")
            break
        else:
            print("Неверный пункт меню")


if __name__ == "__main__":
    main()
