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

#Challenge 3 Threat log

class ThreatLog:
    def __init__(self,ip_address,timestamp):
        self.ip_address = ip_address
        self.timestamp = timestamp
    def print_log(self):
        print(f"{self.ip_address} is in {self.timestamp}")

class PhishingAttack(ThreatLog):
    def __init__(self,ip_address, timestamp,malicious_url):
        super().__init__(ip_address, timestamp)
        #super().__init__(timestamp)
        self.malicious_url = malicious_url
    def print_log(self):
        super().print_log()
        print(f"Action: Blocked malicious URL -> {self.malicious_url}")

def main():
    threatLog = ThreatLog("192.168.1.50", "2026-06-24 15:00:00")
    print("--Basic Log--")
    threatLog.print_log()

    phishingAttack = PhishingAttack("10.0.0.5", "2026-06-24 15:05:00", "http://fake-bank-login.com")
    print("\n--- Phishing Log ---")
    phishingAttack.print_log()

if __name__ == "__main__":
    main()

# task 4 using operator overloading 

class ServerLogs:
    def __init__(self, ip_tuple):
        self.ip_tuple = ip_tuple
    def __add__(self,other):
        combined_tuples = self.ip_tuple + other.ip_tuple
        return ServerLogs(combined_tuples)
    
    def __str__(self):
        return f"Aggregated IPs: {self.ip_tuple}"
    
def main():
    serverlogs1 = ServerLogs(("192.168.1.1", "10.0.0.5"))
    serverlogs2 = ServerLogs(("172.16.0.1",))
    combined = serverlogs1 + serverlogs2
    print(combined)

if __name__ == "__main__":
    main()
