income_list = ["1.Salary", "2.Business", "3.Bonus", "4.Tip"]
expense_list = ["1.Food", "2.Shopping", "3.Transport", "4.Personal expenses"]
food_= float()
salary_dict = {}
food_dict = {}
expense_dict = {}
def show_menu():
  print("-----SIMPLE TRANSACTION ANALYSER-----")
  print(" ")
  choices = ["1.Income", "2.Expense"]
  for i in choices:
    print(i)
def user_choice():
  print(" ")
  choice =int(input("Choose 1 for income and 2 for Expense: "))
  print(" ")
  if choice == 1:
    print("Welcome to income list")
    print(" ")
    for i in income_list:
      print(i)
    print(" ")
    income_choice = input("choose 1 for salary, 2 for business, 3 for bonus and 4 for Tip: ")
    if income_choice == "1":
      salary()
    elif income_choice == "2":
      business()
    elif income_choice == "3":
      Bonus()
    elif income_choice == "4":
      Tip()
    else:
      print("invalid input")
      
      
        
  elif choice == 2:
    print("Welcome to Expenses list")
    print(" ")
    for i in expense_list:
      print(i)
  else:
    print(" ")
    print("Invalid input: just choose 1 for income and 2 for expense transaction")
def salary():
  while True:
    incom = input("enter your salary amount or enter done to exit: ")
    if incom == "done":
      print(salary_dict)
      break
    else:
      try:
        income_ = float(incom)
      except:
        print("Enter valid numbers,not words or punctuation marks")
        continue
   
    month = input("Enter a month of salary: ")
    try:
      month.lower()
    except:
      print("invalid inputs")
      continue
    month_ = month[:3]
   
    salary_dict[month_] = income_
    
def food():
  while True:
    foodie= input("enter your food expense amount for this month or enter done to exit: ")
    if foodie == "done":
      print(food_dict)
      break
    else:
      try:
        food_ = float(foodie)
      except:
        print("Enter valid numbers,not words or punctuation marks")
        continue
   
    month = input("Enter a month of expense: ").lower()
    month_ = month[:3]
   
    foodie_dict[month_] = food_
    
show_menu()
user_choice()
   
      
      
  
  


