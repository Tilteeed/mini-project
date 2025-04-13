from tracker import add_expense, get_expenses, get_total, get_by_category


def main():
    print("Калькулятор расходов")

    while True:
        print("\nМеню:")
        print("1. Добавить расход")
        print("2. Показать все расходы")
        print("3. Показать общую сумму")
        print("4. Показать расходы по категории")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            try:
                amount = float(input("Введите сумму: "))
                category = input("Введите категорию: ")
                description = input("Введите описание (необязательно): ")
                add_expense(amount, category, description)
                print("Расход добавлен!")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == "2":
            all_expenses = get_expenses()
            if not all_expenses:
                print("Нет расходов для отображения")
            else:
                for idx, expense in enumerate(all_expenses, 1):
                    print(f"{idx}. {еxpense['category']}: {еxpense['amount']}")
        elif choice == "3":
            total = get_total()
            print(f"Общая сумма расходов: {total:.2f}")
        elif choice == "4":
            category = input("Введите категорию для фильтрации: ")
            category_expenses = get_by_category(category)
            if not category_expenses:
                print(f"Нет расходов в категории '{category}'")
            else:
                for expense in category_expenses:
                    print(
                        f"{expense['category']}: {expense['amount']} - {expense['description']}"
                    )

        elif choice == "5":
            print("До свидания!")
            break

        else:
            print("Неверный ввод, попробуйте еще раз")


if __name__ == "__main__":
    main()
