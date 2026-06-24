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

#Color Palette Problem 2:

class  DashboardConfig:
    def __init__(self,color):
        self.primary_color = color

    @classmethod
    def default_palette(cls):
        theme = ("ElectricPurple", "#000000", "Grey", "#FFFFFF")
        return theme 
    @property
    def primary_color(self):
        return self._color
    @primary_color.setter
    def primary_color(self,color):
        if color not in ("ElectricPurple", "#000000", "Grey", "#FFFFFF"):
            raise ValueError("Invalid color")
        self._color = color




def main():
    print("Standard Palette: ", DashboardConfig.default_palette())
    theme1 = DashboardConfig("ElectricPurple")
    print(f"Theme1 is using : {theme1.primary_color}")
    theme2 = DashboardConfig("Phlox Purple")


if __name__ == "__main__":
    main()
