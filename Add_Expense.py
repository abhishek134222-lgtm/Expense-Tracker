def add_expenses():
    print(" ")
    print(" --- Now Entered Add Expense Mode --- ")
    print(" ")
    
    while True:
        print("Choose 1 to Add Expense")
        print("Choose 2 to Exit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            print(" ")
            item = input("Name What you purchased or where did you spend : ")
            amt = input("Enter the Amount you spend For it : ")
            f = open("expenses.txt","a")
            item_amt = item + " - " + amt
            f.write(item_amt)
            f.write("\n")
            
            f.close()

        elif choice == 2:
            print(" ")
            print("All Expense You Added Are Saved")
            break
        else:
            print(" ")
            print("Invalid Input !!!")