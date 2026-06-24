#Problem 1

class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self,balance):
        if balance < 0:
            raise ValueError ("Invalid Transaction: Fraud Detected!")
        self._balance = balance
        print("Valid Transaction!!")


def main():
    bankAccount = getBalance()
    print(f"Current Balance in Vault: {bankAccount.balance}")

def getBalance():
    balance = int(input("Enter the balance : "))
    return BankAccount(balance) 


if __name__ == "__main__":
    main()
