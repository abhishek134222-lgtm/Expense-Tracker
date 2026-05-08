def total_expense():
    print(" ")
    print("--- Entered into Total Expense Mode ---")
    total = 0
    f = open("expenses.txt","r")
    for line in f:
        exp = line.strip().split(" - ")
        total += int(exp[1])
    print("Total expenses till now are :",total)
    print(" ")