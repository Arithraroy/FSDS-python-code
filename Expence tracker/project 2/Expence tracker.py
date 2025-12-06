print("---welcome to expence tracker---")
expenseslist=[]

while True:
   print("1. add expense")
   print("2. veiw all expenses")
   print("3. veiw  total spending")
   print("4. Exit")

   choice=int(input("Enter  your choice(1-4):"))
   
   if choice==1:
      date=(input("Enter date:"))
      category=input("Enter category(Food,shopping,travel)")
      description=input("Enter description")
      amount=float(input("Enter amount"))
      expense =  {"date":date,
                 "category":category,
                 "description":description,
                 "amount":amount}
                   
      expenseslist.append(expense)
      print("Expense added successfully")

   elif choice ==2 :
      count=1
      for  eachkey in expenseslist:
       print(
                f"Your expense number:{count} -> "
                f"{expense['date']},{expense['category']},{expense['description']},{expense['amount']}"
            )
       count=count+1

   elif choice == 3:
      
      total=0
      for eachkey in expenseslist:
       total+=eachkey["amount"]
       print(total)

   elif choice ==4:
      print("thnaks  for using expense tracker")
      break
   
   else:
      print("invalid choice number:")
      




      
     



      



    
   
