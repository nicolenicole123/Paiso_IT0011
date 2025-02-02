def sum_of_digits(s):
    total = 0
    for char in s:
        if char.isdigit():
            total += int(char)
    print(f"Sum of digits: {total}")

# Example usage
input_str = input("Enter a string containing digits: ")
sum_of_digits(input_str)
