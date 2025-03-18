def div(a, b):
    if b == 0:
        print("Error! Denominator must not be equal to zero.")
        return None
    return a / b

def exp(a, b):
    return a ** b

def rem(a, b):
    if b == 0:
        print("Error! Denominator must not be equal to zero.")
        return None
    return a % b

def sum_range(a, b):
    if a >= b:
        print("Error! Invalid input, the second number must be greater than the first number.")
        return None
    return sum(range(a, b + 1))

def main():
    while True:
        print("\n==MATHEMATICAL OPERATION MENU <3==")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Enter your choice: ").upper()
        
        if choice == 'Q':
            print("Exiting the program. Goodbye!<3")
            break
        
        if choice in ['D', 'E', 'R', 'F']:
            try:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter integers only.")
                continue
            
            if choice == 'D':
                result = div(a, b)
            elif choice == 'E':
                result = exp(a, b)
            elif choice == 'R':
                result = rem(a, b)
            elif choice == 'F':
                result = sum_range(a, b)
            
            if result is not None:
                print("Result:", result)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

