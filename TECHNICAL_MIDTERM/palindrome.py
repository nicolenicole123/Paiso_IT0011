def is_palindrome(n):
    n_str = str(n)  # Convert number to string
    reversed_str = ""  # Initialize an empty string

    # Loop through the string and build the reversed version manually
    for char in n_str:
        reversed_str = char + reversed_str  # Add characters in reverse order

    return n_str == reversed_str  # Check if the original and reversed are the same

# Open the file and read lines
with open("numbers.txt", "r") as file:
    lines = file.readlines()

# Process each line
for i, line in enumerate(lines):
    numbers = line.strip().split(",")  # Split numbers by comma
    total = 0  # Initialize sum
    for num in numbers:
        total += int(num)  # Convert each to integer and add

    # Check if sum is a palindrome
    if is_palindrome(total):
        print(f"Line {i+1}: {line.strip()} (sum {total}) - Palindrome")
    else:
        print(f"Line {i+1}: {line.strip()} (sum {total}) - Not a palindrome")
        import os

