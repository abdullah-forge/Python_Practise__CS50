#Challenge 1 (Type Error checking)

def main():
    amount : float = float(input("Enter the amount: "))
    currency : str = input("Enter the currency: ")
    output = process_payment(amount, currency)
    print(output)

def process_payment(amount : float, currency : str) -> bool:
    """summary for process_payment
    Args:
        amount (float): [Amount should be enter in float]
        currency (str): [currency should be enter in string]
    Returns:
        bool: [if amount greater then zero then it will True and vice versa]
    """
    return amount > 0

if __name__ == "__main__":
    main()
