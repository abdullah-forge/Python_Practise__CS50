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

# challenge 2 (Enumerate and list comprehension)

raw_ips = ["192.168.1.1", "10.0.0.5", "192.168.1.1", "172.16.0.1", "10.0.0.5"]

unique_ips = {*raw_ips}
#print(unique_ips)
local_ips = [u for u in unique_ips if u.startswith("192")]
#print(local_ips)
for i, local_ip in enumerate (local_ips):
    print(i+1,local_ip)

# challenge 3 (*args & kwargs)

def send_to_ai(model_name, *prompts, **configs):
    print("Using model", model_name)
    for item in prompts:
        print(item, end=" ")
    for name, value in configs.items():
        print(f"{name} valued {value}")

send_to_ai("Gemini-3", "Analyze this image", "Summarize this log", temperature=0.7, max_tokens=1000)

# challenge 4 (maps and Filter)

str_amounts = ["500", "1200", "300", "4500", "800"]

int_list = list(map(int, str_amounts))
print(int_list)

result = list(filter(lambda x: x >1000 , int_list))
print(result)

# Challenge 5 (Generators - yield)

def main():
    logs = generate_massive_logs(5)
    for log in logs:
        print(log)

def generate_massive_logs(limit):
    for i in range(limit):
        yield f"Log line {i} processed"

if __name__ == "__main__":
    main()


