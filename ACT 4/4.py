import json

FILE_NAME = "student_records.json"

def load_records():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_records(records):
    with open(FILE_NAME, "w") as file:
        json.dump(records, file, indent=4)

def calculate_final_grade(class_standing, exam):
    return round((class_standing * 0.6) + (exam * 0.4), 2)

def show_records(records):
    print("\nAll Student Records:")
    print("(Ordered by Last Name or by Grade if specified)")
    for record in records:
        print(f"ID: {record[0]}, Name: {record[1][0]} {record[1][1]}, Standing: {record[2]}, Exam: {record[3]}, Final Grade: {calculate_final_grade(record[2], record[3])}")

def sort_by_last_name(records):
    return sorted(records, key=lambda x: x[1][1])

def sort_by_final_grade(records):
    return sorted(records, key=lambda x: calculate_final_grade(x[2], x[3]), reverse=True)

def find_record(records, student_id):
    for record in records:
        if record[0] == student_id:
            return record
    return None

def add_record(records):
    student_id = input("Enter Student ID (6 digits): ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing Grade: "))
    exam = float(input("Enter Major Exam Grade: "))
    records.append((student_id, (first_name, last_name), class_standing, exam))
    print("Record Added!")

def edit_record(records):
    student_id = input("Enter Student ID to Edit: ")
    for i, record in enumerate(records):
        if record[0] == student_id:
            first_name = input("Enter New First Name: ")
            last_name = input("Enter New Last Name: ")
            class_standing = float(input("Enter New Class Standing Grade: "))
            exam = float(input("Enter New Major Exam Grade: "))
            records[i] = (student_id, (first_name, last_name), class_standing, exam)
            print("Record Updated!")
            return
    print("Student not found.")

def delete_record(records):
    student_id = input("Enter Student ID to Delete: ")
    for record in records:
        if record[0] == student_id:
            records.remove(record)
            print("Record Deleted!")
            return
    print("Student not found.")

def main():
    records = load_records()

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

        choice = input("Enter your choice: ")

        if choice == "1":
            records = load_records()
            print("File loaded successfully.")
        elif choice == "2":
            save_records(records)
            print("Records saved.")
        elif choice == "3":
            new_file = input("Enter new file name: ")
            with open(new_file, "w") as file:
                json.dump(records, file, indent=4)
            print("Records saved as new file.")
        elif choice == "4":
            order = input("Order by (last name/grade/none): ").strip().lower()
            if order == "last name":
                show_records(sort_by_last_name(records))
            elif order == "grade":
                show_records(sort_by_final_grade(records))
            else:
                show_records(records)
        elif choice == "5":
            student_id = input("Enter Student ID: ")
            record = find_record(records, student_id)
            if record:
                print(record)
            else:
                print("Student not found.")
        elif choice == "6":
            add_record(records)
        elif choice == "7":
            edit_record(records)
        elif choice == "8":
            delete_record(records)
        elif choice == "9":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
