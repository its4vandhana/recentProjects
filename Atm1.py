class Atm:
    def __init__(self):
        self.pin=''
        self.__balance= 50000
        self.menu()

    def get_balance(self):
        print(f"Your balance is {self.__balance}")


    def set_balance(self,new_bal):

      if type(new_bal) is str:
        print("balance cannot be alphabets")

      elif new_bal < 0:
        print("balance cannot be negative")

      elif type(new_bal) == float:
        print('balance can not be decimal')

      else:
        self.__balance = new_bal




    def menu(self):

      user_input = int(input("""

            Enter your choice :

            1. press 1 to create pin
            2. press 2 to change pin
            3. press 3 to check balance
            4. press 4 to withdraw money
            5. press 5 to exit


            """))

      if user_input == 1:
        self.create_pin()

      elif user_input == 2:
        self.change_pin()

      elif user_input == 3:
        self.check_balance()

      elif user_input == 4:
        self.withdraw_money()

      elif user_input == 5:
        exit()

      else:
        print("Invalid input")


    def create_pin(self):

      user_pin = int(input("Enter the new pin:"))

      if user_pin < 0:
          print("Pin cannot be negative")

      else:
          self.pin = user_pin

      print("New pin has been set successfully.")

      self.menu()


    def change_pin(self):
      old_pin = int(input('Enter your old pin : '))

      if old_pin == self.pin:
        new_pin = input('Enter your new pin : ')

        self.pin = new_pin
        print('pin has been changed successfully')

      else:
        print('you entered the wrong pin')

      self.menu()

    def check_balance(self):

      user_input = int(input('Enter your pin :'))

      if user_input == self.pin:
        self.get_balance()

      else:
        print('hey thief..... you dont have the right pin')

      self.menu()

    def withdraw_money(self):

      user_input=int(input("Enter your pin for validation:"))

      if user_input==self.pin:

          entered_amt= int(input("Enter the required amount to be withdrawn"))

          if entered_amt > self.__balance:
              print("Insufficient Balance")

          else:
              self.__balance =  self.__balance - entered_amt
              self.get_balance()
      else:
          print("Hey thief get a job")

      self.menu()



