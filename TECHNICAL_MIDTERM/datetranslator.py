# Dictionary for month names
months = {
    "01": "January", "02": "February", "03": "March", "04": "April",
    "05": "May", "06": "June", "07": "July", "08": "August",
    "09": "September", "10": "October", "11": "November", "12": "December"
}

# Get user input
date_input = input("Enter the date (mm/dd/yyyy): ")

# Split the date into parts
month, day, year = date_input.split("/")

# Convert day to integer to remove leading zeros
day = str(int(day))

# Format and display
print("Date Output:", f"{months[month]} {day}, {year}")
