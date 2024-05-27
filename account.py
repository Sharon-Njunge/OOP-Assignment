class Account:
    def __init__(self, number, pin, owner_name="Unknown"):
        self.number = number
        self.__pin = pin
        self.__owner_name = owner_name
        self.__balance = 0
        self.__overdraft_limit = None
        self.__minimum_balance = None
        self.__is_frozen = False
        self.__transaction_history = []
    def view_details(self, pin):
        if pin == self.__pin:
            return f"Account Number: {self.number}\nOwner Name: {self.__owner_name}\nCurrent Balance: {self.__balance}"
        else:
            return "Wrong PIN"
    def change_owner(self, new_owner_name, pin):
        if pin == self.__pin:
            self.__owner_name = new_owner_name
            return f"Account owner changed to {new_owner_name}."
        else:
            return "Wrong PIN"
    def account_statement(self, pin):
        if pin == self.__pin:
            transactions = ["Deposit 900", "Withdrawal $300"]
            return "\n".join(transactions)
        else:
            return "Wrong PIN"
    def overdraft_limit(self, limit, pin):
        if pin == self.__pin:
            self.__overdraft_limit = limit
            return f"Overdraft limit set to ${limit}."
        else:
            return "Wrong PIN"
    def calculate_interest(self, rate, pin):
        if pin == self.__pin:
            interest_amount = self.__balance * rate / 100
            self.__balance += interest_amount
            return f"Interest calculated. New balance: ${self.__balance}"
        else:
            return "Wrong PIN"
    def freeze_account(self, pin):
        if pin == self.__pin:
            self.__is_frozen = True
            return "Account frozen."
        else:
            return "Wrong PIN"
    def unfreeze_account(self, pin):
        if pin == self.__pin:
            self.__is_frozen = False
            return "Account unfrozen."
        else:
            return "Wrong PIN"
    def transaction_history(self, pin):
        if pin == self.__pin:
            return "\n".join(self.__transaction_history)
        else:
            return "Wrong PIN"
    def minimum_balance(self, min_balance, pin):
        if pin == self.__pin:
            self.__minimum_balance = min_balance
            return f"Minimum balance requirement set to ${min_balance}."
        else:
            return "Wrong PIN"
    def transfer_funds(self, amount, recipient_number, pin):
        if pin == self.__pin:
            if self.__balance >= amount:
                self.__balance -= amount
                self.__transaction_history.append(f"Withdrawal: ${amount} to {recipient_number}")
                return f"Funds transferred successfully. New balance: ${self.__balance}"
            else:
                return "Insufficient funds."
        else:
            return "Wrong PIN"
    def close_account(self, pin):
        if pin == self.__pin:
            return "Account closed."
        else:
            return "Wrong PIN"







