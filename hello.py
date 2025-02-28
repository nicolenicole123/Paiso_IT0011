import json

FILE_PATH = "records_data.json"

def load_data():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

def compute_final_score(standing, exam_score):
    return round((standing * 0.6) + (exam_score * 0.4), 2)

def display_data(data):
    print("\nShowing all student records:")
    print("- Sorted by last name")
    print("- Sorted by final grade (60% class standing, 40% major exam)")
    for entry in data:
        print(f"ID: {entry[0]}, Name: {entry[1][0]} {entry[1][1]}, Standing: {entry[2]}, Exam: {entry[3]}, Final Grade: {compute_final_score(entry[2], entry[3])}")

def sort_by_surname(data):
    return sorted(data, key=lambda x: x[1][1])

def sort_by_score(data):
    return sorted(data, key=lambda x: compute_final_score(x[2], x[3]), reverse=True)

def locate_entry(data, stud_id):
    for entry in data:
        if entry[0] == stud_id:
            return entry
    return None

def insert_entry(data):
    stud_id = input("Enter Student ID (6 digits): ")
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    standing = float(input("Enter Class Standing Grade: "))
    exam_score = float(input("Enter Major Exam Grade: "))
    data.append((stud_id, (fname, lname), standing, exam_score))
    print("Entry Added!")

def modify_entry(data):
    stud_id = input("Enter Student ID to Edit: ")
    for i, entry in enumerate(data):
        if entry[0] == stud_id:
            fname = input("Enter New First Name: ")
            lname = input("Enter New Last Name: ")
            standing = float(input("Enter New Class Standing Grade: "))
            exam_score = float(input("Enter New Major Exam Grade: "))
            data[i] = (stud_id, (fname, lname), standing, exam_score)
            print("Entry Updated!")
            return
    print("Student not found.")

def remove_entry(data):
    stud_id = input("Enter Student ID to Delete: ")
    for entry in data:
        if entry[0] == stud_id:
            data.remove(entry)
            print("Entry Deleted!")
            return
    print("Student not found.")

def main():
    data = load_data()

    while True:
        print("\nMenu:")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Show Student Record")
        print("6. Add Record")
        print("7. Edit Record")
        print("8. Delete Record")
        print("9. Exit")

        option = input("Enter your choice: ")

        if option == "1":
            data = load_data()
            print("File opened.")
        elif option == "2":
            save_data(data)
            print("File saved.")
        elif option == "3":
            new_file = input("Enter new file name: ")
            with open(new_file, "w") as file:
                json.dump(data, file, indent=4)
            print("File saved as new file.")
        elif option == "4":
            display_data(data)
        elif option == "5":
            stud_id = input("Enter Student ID: ")
            entry = locate_entry(data, stud_id)
            if entry:
                print(entry)
            else:
                print("Student not found.")
        elif option == "6":
            insert_entry(data)
        elif option == "7":
            modify_entry(data)
        elif option == "8":
            remove_entry(data)
        elif option == "9":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
