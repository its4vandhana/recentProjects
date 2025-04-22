class Atm:
  def __init__(self,pin,balance):
    self.pin = pin
    self.__balance = 0

  def get_balance(self):
    print(f"the balance is {self.__balance}")

  def set_balance(self,new_bal):
    
    if type(new_bal) is str:
      print("balance cannot be alphabets")
    elif new_bal < 0:
      print("balance cannot be negative")
    else: 
      self.__balance = new_bal

  def create_pin(self):
    User_pin = int(input("Enter the pin"))
    if User_pin < 0:
      print("PIN cannot be negative")
    else:
      self.pin = User_pin
      print("PIN created")

  def change_pin(self,pin):
    old_pin = int(input("Enter the old pin"))
    if old_pin == self.pin:
      print("Enter the new pin to be changed to")
      new_pin = int(input("Enter pin: "))
      if new_pin < 0:
        print("PIN cannot be negative")
      else:
        self.pin = new_pin
        print("PIN created")

  def check_balance(self):
    print(f"The current balance is {self.__balance}")

  def deposit(self,amount):
    if amount >= 0:
      self.__balance += amount
      print(f"{amount} is deposited to your account")
    else:
      print("Less fund")

  def withdraw_amount(self, w_amount):
    if self.__balance < w_amount:
      print("No sufficient funds")
    elif self.__balance >= w_amount:
      self.__balance -= w_amount
      print(f"The amount withdrawn is {w_amount} and your current balance is {self.__balance}")
    
  def menu(self):
    while True:
      option = int(input("Enter the menu option"))
      if option == 1:
        print("create a pin")
        a.create_pin()
        
      elif option == 2:
        print("Change the pin")
        a.change_pin(self.pin)

      elif option == 3:
        print("Show balance")
        a.check_balance()

      elif option == 4:
        print("Deposit money")
        money = int(input("Enter the money to be deposited"))
        a.deposit(money)
        # print(dep)

      elif option  == 5:
        withdraw_amt = int(input("Enter the amount to be withdrawn"))
        a.withdraw_amount(withdraw_amt)
      else:
        print("Invalid option")
        break

a = Atm(1001,100)
a.get_balance()
a.set_balance('abc')
a.menu()