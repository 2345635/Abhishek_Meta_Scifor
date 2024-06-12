class Bank:
    def __init__(self, pin, balance):
        self._pin = pin
        self._balance = balance
    def verify_pin(self, pin):
        return self._pin == pin
    def get_balance(self):
        return self._balance
    def _update_balance(self, amount):
        self._balance += amount
        print(f"Updated balance: {self._balance}")
    def withdraw(self, pin, amount):
        if self.verify_pin(pin):
            if self._balance >= amount:
                self._update_balance(-amount)
                print(f"Withdrawal successful. Withdrawn amount: {amount}")
            else:
                print("Insufficient balance")
        else:
            print("Invalid pin")
    def deposit(self, pin, amount):
        if self.verify_pin(pin):
            self._update_balance(amount)
            print(f"Deposit successful. Deposited amount: {amount}")
        else:
            print("Invalid pin")

pin = int(input("Enter your PIN: "))
initial_balance = float(input("Enter your initial balance: "))
bank_account = Bank(pin, initial_balance)

"""
  Enter your PIN: 123
Enter your initial balance: 4000
"""
while True:
    action = input("Enter 'withdraw' to withdraw money or 'deposit' to deposit money (or 'exit' to exit): ").lower()
    if action == 'withdraw':
        pin_input = int(input("Enter your PIN: "))
        amount = float(input("Enter the amount to withdraw: "))
        bank_account.withdraw(pin_input, amount)
    elif action == 'deposit':
        pin_input = int(input("Enter your PIN: "))
        amount = float(input("Enter the amount to deposit: "))
        bank_account.deposit(pin_input, amount)
    elif action == 'exit':
        break
    else:
        print("Invalid action")
"""
Enter 'withdraw' to withdraw money or 'deposit' to deposit money (or 'exit' to exit): withdraw
Enter your PIN: 123
Enter the amount to withdraw: 1000
Updated balance: 3000.0
Withdrawal successful. Withdrawn amount: 1000.0
Enter 'withdraw' to withdraw money or 'deposit' to deposit money (or 'exit' to exit): deposit
Enter your PIN: 123
Enter the amount to deposit: 250
Updated balance: 3250.0
Deposit successful. Deposited amount: 250.0
Enter 'withdraw' to withdraw money or 'deposit' to deposit money (or 'exit' to exit): exit
"""
  
