income_list = ["1.Salary", "2.Business", "3.Bonus", "4.Tip"]
expense_list = ["1.Food", "2.Shopping", "3.Transport", "4.Personal expenses"]
def show_menu():
  print("-----SIMPLE TRANSACTION ANALYSER-----")
  print(" ")
  choices = ["1.Income", "2.Expense"]
  for i in choices:
    print(i)
def user_choice():
  print(" ")
  choice =int(input("Choose 1 for income and 2 for Expense"))
  print(" ")
  if choice == 1:
    print("Welcome to income list")
    print(" ")
    for i in income_list:
      print(i)
  else:
    print("Welcome to Expenses list")
    print(" ")
    for i in expense_list:
      print(i)
show_menu()
user_choice()
