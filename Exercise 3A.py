from functools import reduce

def get_expense():
    expenses = []
    while True:
        expense_type = input("Enter the type of expense (or 'done' if finished): ").strip()
        if expense_type.lower() == 'done':
            break
        while True:
            try:
                expense_amount = float(input(f"Enter the amount for {expense_type}: "))
                expenses.append((expense_type, expense_amount))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    return expenses

def calculate_expense_totals(expenses):
    total_expense = reduce(lambda acc, expense: acc + expense[1], expenses, 0)
    highest_expense = reduce(lambda acc, expense: max(acc, expense[1]), expenses, float('-inf'))
    lowest_expense = reduce(lambda acc, expense: min(acc, expense[1]), expenses, float('inf'))

    return total_expense, highest_expense, lowest_expense

def analyze_expenses(expenses):
    total_expense, highest_expense, lowest_expense = calculate_expense_totals(expenses)

    print("\nExpense Analysis:")
    print("-----------------")
    print(f"Total Expense: ${total_expense:.2f}")

    highest_expense_type = [expense[0] for expense in expenses if expense[1] == highest_expense]
    lowest_expense_type = [expense[0] for expense in expenses if expense[1] == lowest_expense]

    print(f"Highest Expense: ${highest_expense:.2f} (for {', '.join(highest_expense_type)})")
    print(f"Lowest Expense: ${lowest_expense:.2f} (for {', '.join(lowest_expense_type)})")

def main():
    print("Welcome to the Expense Analyzer")
    print("------------------------------------")
    expense = get_expense()
    analyze_expenses(expense)

if __name__ == "__main__":
    main()