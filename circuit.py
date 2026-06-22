def main():
    x = int(input("Enter the value of current : "))
    y = int(input("Enter the value of resistance :"))
    output = calc_voltage(x,y)
    print(f"Value of the voltage is {output}v")

# circuit.py
def calc_voltage(current, resistance):
    return current * resistance


if __name__ == "__main__":
    main()