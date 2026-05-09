import Add_Expense
import View_Expenses
import Total_Expense
import Remove_Expense
def main():
    print(" ------ Welcome To Abhishek's Expense Tracking System ------")
    print(" ")
    print(" ")
    while True:
        print("Choose 1 to Add Expense                ")
        print("Choose 2 to View Expense               ")
        print("Choose 3 to Show Total                 ")
        print("Choose 4 to Remove the Existing Expense")
        print("Choose 5 to Exit                       ")

        choice = int(input("Choose the given option : "))

        if choice == 1: 
            Add_Expense.add_expenses()

        elif choice == 2:
            View_Expenses.view_expenses()

        elif choice == 3:
            Total_Expense.total_expense()

        elif choice == 4:
            Remove_Expense.remove_expense()

        elif choice == 5:
            print("---- Thanks For Using Abhishek's Expense Tracker ----")
            break
        
        else:
            print("!!! Invalid Input Choose Again !!!")

main()