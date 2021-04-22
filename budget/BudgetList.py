from . import Expense

class BudgetList:
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []
def append(self, item):
    if self.sum_expenses+item < self.budget:
        append(self.expenses)
    else append(self.overages)

def __len__(self):
    return len(self.expenses, self.overages)
def main():
    myBudgetList = BudgetList(1200)

if __name__ == '__main__':
    main()

expenses = Expense.expenses()
read_expenses('data/spending_data.csv')
for expense in expenses.list:
    append(expense.amount.myBudgetList)
    print("The count of all expenses: " + str(len(myBudgetList)))


