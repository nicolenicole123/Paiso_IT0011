def is_palindrome(n):
    n_str = str(n)  # Convert number to string
    reversed_str = ""  # Initializing

    
    for char in n_str:
        reversed_str = char + reversed_str 

    return n_str == reversed_str  # Check if the original and reversed are the same

# Open the file and read lines
with open("C:/Users/Nicole Paiso/Documents/GitHub/Paiso_IT0011/TECHNICAL_MIDTERM/numbers.txt", "r") as file:
    lines = file.readlines()

# Process each line
for i, line in enumerate(lines):
    numbers = line.strip().split(",")  # Split numbers by comma
    total = 0  

    for num in numbers:  
        num = num.strip()  # Remove any surrounding spaces
        if num.isdigit():  
            total += int(num) 
        else:
            print(f"Skipping invalid value: {num}")  # Debugging message

    # Check if sum is a palindrome
    if is_palindrome(total):
        print(f"Line {i+1}: {line.strip()} (sum {total}) - Palindrome")
    else:
        print(f"Line {i+1}: {line.strip()} (sum {total}) - Not a palindrome")
    


