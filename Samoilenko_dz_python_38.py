# 1

class BankAccount:
    """
        Simple bank account with balance management
        and operation history.
    """
    def __init__(self, account_name, account_balance=0):
        self.account_name = account_name
        self.__account_balance = account_balance
        self.__history =[]

    def set_replenishment(self, balance):
        self.__account_balance += balance
        self.__history.append(f"Deposit: {balance}")

    def set_withdraw(self, balance):
        self.__validate_balance(balance)
        self.__account_balance -= balance
        self.__history.append(f"Withdraw: {balance}")

    def __validate_balance(self,value):
        if value > self.__account_balance:
            raise ValueError("Insufficient funds")

    @property
    def get_balance(self):
        return self.__account_balance

    @property
    def property_history(self):
        return self.__history.copy()




try:
    bank = BankAccount("Adam", 5)
    print(f"Balance: ", bank.get_balance)
    bank.set_replenishment(100)
    print(f"Balance: ", bank.get_balance)
    bank.set_withdraw(73)
    print("Operation history:")
    for item in bank.property_history:
        print("\t",item)
    print(f"Balance: ", bank.get_balance)
    bank.set_withdraw(100)
except ValueError as e:
    print(e)
