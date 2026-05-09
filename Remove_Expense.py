import View_Expenses
def remove_expense():
    View_Expenses.view_expenses()
    rem = input("Name Expense to be removed : ")
    f = open("expenses.txt","r")
    lines = f.readlines()
    f.close()
    
    f = open("expenses.txt","w")
    for i in lines:
        temp = i.split(" - ")
        if temp[0].lower().strip() != rem.lower().strip():
            f.write(i)
        if temp[0].lower().strip() == rem.lower().strip():
            print(temp[0]," - ",temp[1].strip(),"is now removed ")

    f.close()
    print(" ")