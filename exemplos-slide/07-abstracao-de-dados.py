class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self) -> float:
        return self.__balance

if __name__ == "__main__":
    acc = BankAccount("Alice", 100.0)
    acc.deposit(50.0)
    acc.withdraw(30.0)
    print(acc.get_balance())

    