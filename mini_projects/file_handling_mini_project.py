def add_student():
    roll_no= input("enter roll number:")
    name= input("enter name: ")
    marks= input("enter marks: ")

    with open("student.txt","a") as f :
        f.write(roll_no + "," + name + "," + marks + "\n")

    print("student added successfully")

def view_students():
    try:
        with open("students.txt", "r") as f:
            print("\n--- Student Records ---")
            print(f.read())
    except FileNotFoundError:
        print("No records found")

def search_student():
    roll = input("Enter roll to search: ")

    found = False
    with open("students.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == roll:
                print("Found:", line)
                found = True
                break

    if not found:
        print("Student not found")

def delete_student():
    roll = input("Enter roll to delete: ")

    lines = []
    found = False

    with open("students.txt", "r") as f:
        for line in f:
            if not line.startswith(roll + ","):
                lines.append(line)
            else:
                found = True

    with open("students.txt", "w") as f:
        f.writelines(lines)

    if found:
        print("Deleted successfully")
    else:
        print("Student not found")

while True:
    print("\n1 Add student")
    print("2 View students")
    print("3 Search student")
    print("4 Delete student")
    print("5 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Goodbye")
        break
    else:
        print("Invalid choice")