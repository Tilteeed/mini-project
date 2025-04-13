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


if __name__ == "__main__":
    main()
