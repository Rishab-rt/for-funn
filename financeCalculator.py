incomelist = []
expenselist = []
expenseamt = []
transactions  = 0
balance = 0 

def trackerRun():
    global balance, transactions
    while True:
        type = input("Enter transaction type (Income/Expense) or 'exit': ")
        if type == "exit":
           exit()
        elif type == "Expense":
           addTransaction()
           continue
        elif type == "Income":
           addIncome()
           continue
        else:
           trackerRun()
    
    check = input("Would you like to view previous transactions?: ")
    if check == "yes":
      viewTransactionHistory()
    
      
def addIncome():
  amount = int(input("Please enter the amount that you have earned: $"))
  balance += amount
  type = input("What is the category?: ")
  incomeList.append(type)

def addTransaction():
  amount = int(input("Please enter the amount that you have spent: $"))
  balance -= amount 
  expenseamt.append(amount)
  type = input("What is the category?: ")
  expenseList.append(type)
  transactions+=1

def viewBalance():
  view = input("Would you like to view balance?: ")
  if view == "yes":
    print("You have a balance of $", balance)
    


def viewTransactionHistory():
  for i in range (transactions):
    print(expenseList[i],"$",expenseamt[i])
  

trackerRun()
