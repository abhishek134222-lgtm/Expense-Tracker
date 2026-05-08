def view_expenses():
    f = open("expenses.txt","r")
    data = f.read()
    
    print(" ")
    print("--- Your Expenses Till Now Are ---")
    print(" ")
    print(data)
    print(" ")

    f.close()