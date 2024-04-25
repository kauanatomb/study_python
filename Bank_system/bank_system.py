menu = """"
[1] Deposit
[2] Withdraw
[3] Check Balance
[4] Quit
"""

balance = 0
limite = 500
check_balance = ""
WITHDRAW_LIMIT = 3

while True:
  option = input(menu)

  if option == "1":
    print("Insert the amount to deposit")
    deposit = float(input())
    balance += deposit
    print(f"Your balance is {balance}")
  
  elif option == "2":
    print("Insert the amount to withdraw")
    withdraw = float(input())
    if WITHDRAW_LIMIT > 0 and withdraw <= limite:
      if withdraw <= balance:
        balance -= withdraw
        WITHDRAW_LIMIT -= 1
        check_balance += f"Withdrawn value: {withdraw}\n Balance at the time: {balance}\n"
        print(f"Withdrawn done with success. Your balance is {balance}")
      else:
        print("You don't have enough money")
    else:
      print("You don't have withdraws left or the value is higher than the limit")

  
  elif option == "3":
    if not check_balance:
      check_balance = "No operations yet"
    print("Your balance now is:", balance, "\n Operations:", check_balance)
  
  elif option == "4":
    print("Au revoir, muchacho!")
    break

  else:
    print("Invalid option, check the menu again")