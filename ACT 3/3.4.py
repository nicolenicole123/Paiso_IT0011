try:
    with open("students.txt", "r") as file:
        print("\nReading Student Information:")
        print(file.read()) 
except FileNotFoundError:
    print("Error: 'students.txt' file not found.")
