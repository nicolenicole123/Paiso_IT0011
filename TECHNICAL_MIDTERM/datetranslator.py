# Dictionary for months
months = {
    "01": "January", "02": "February", "03": "March", "04": "April",
    "05": "May", "06": "June", "07": "July", "08": "August",
    "09": "September", "10": "October", "11": "November", "12": "December"
}

# Get user input
date_input = input("Enter the date (mm/dd/yyyy): ")

month, day, year = date_input.split("/")

day = str(int(day))

# Format and display
print("Date Output:", f"{months[month]} {day}, {year}")