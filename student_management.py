# Student Management System
# This project stores basic student information and allows the user
# to add, update, delete and search students. 

students = []   # list to store student data


def add_student():
    print("\n--- Add New Student ---")
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Course: ")

    student = {
        "id": sid,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    print("\n--- All Students ---")
    if len(students) == 0:
        print("No records found.")
    else:
        for s in students:
            print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")


def search_student():
    print("\n--- Search Student ---")
    sid = input("Enter Student ID to search: ")

    found = False
    for s in students:
        if s["id"] == sid:
            print("Record Found:")
            print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")
            found = True
            break

    if not found:
        print("No student found with that ID.")


def update_student():
    print("\n--- Update Student ---")
    sid = input("Enter Student ID to update: ")

    for s in students:
        if s["id"] == sid:
            print("Enter new details (leave blank to keep old value):")

            new_name = input(f"New Name ({s['name']}): ")
            new_age = input(f"New Age ({s['age']}): ")
            new_course = input(f"New Course ({s['course']}): ")

            if new_name != "":
                s["name"] = new_name
            if new_age != "":
                s["age"] = new_age
            if new_course != "":
                s["course"] = new_course

            print("Student record updated successfully!")
            return

    print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")
    sid = input("Enter Student ID to delete: ")

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def main_menu():
    while True:
        print("\n==== Student Management System ====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


# start program
main_menu()