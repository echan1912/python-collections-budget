from . import Expense
import matplotlib.pyplot as plt

def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    

    
        
    print("Sets are NOT equal by subset test")




if __name__ == "__main__":
    main()