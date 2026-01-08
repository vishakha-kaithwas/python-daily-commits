class Account:
    bank_name = "YONO"

    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Balance cannot be negative")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Amount should be valid")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0


account = Account("Vishakha", 10000)
account.deposit(99)
account.withdraw(1000)

print("Balance:", account.balance)
print(Account.is_valid_amount(200))

