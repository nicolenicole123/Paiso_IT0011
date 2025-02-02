input_string = input("Enter a string of digits: ")

digit_sum = 0

for char in input_string:
    if char >= '0' and char <= '9':  # Check if the character is a digit
        digit_sum += int(char)

print(f"Sum of digits: {digit_sum}")