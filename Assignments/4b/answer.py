students = {}


def add_student():
    name = input("Enter the student's name: ").strip()
    if not name:
        print("Student name cannot be empty.")
        return
    if name in students:
        print("Error: Student already exists.")
        return

    grade_input = input(f"Enter {name}'s grade: ").strip()
    try:
        grade = int(grade_input)
    except ValueError:
        print("Invalid grade. Please enter an integer.")
        return

    students[name] = [grade]

    print(f"{name} added successfully")


def update_grade():
    name = input("Enter the student's name: ").strip()
    if not name:
        print("Student name cannot be empty.")
        return
    if name not in students:
        print("Error: Student not found.")
        return

    grades = students[name]

    if not grades:
        print("This student has no grades to update.")
        return

    print(f"Current grades for {name}: {grades}")

    index_input = input("Enter index of grade to update (starting from 0): ").strip()
    try:
        index = int(index_input)
    except ValueError:
        print("Invalid index. Please enter an integer.")
        return
    try:
        _ = grades[index]
    except IndexError:
        print("Invalid index! Please try again.")
        return
    new_grade_input = input("Enter the new grade: ").strip()
    try:
        new_grade = int(new_grade_input)
    except ValueError:
        print("Invalid grade. Please enter an integer.")
        return
    try:
        students[name][index] = new_grade
        print(f"{name}'s grade updated successfully")
    except IndexError:
        print("Invalid index! Please try again.")


def remove_student():
    name = input("Enter the student's name to remove: ").strip()
    if not name:
        print("Student name cannot be empty.")
        return
    if name in students:
        del students[name]
        print(f"{name} removed successfully!")
    else:
        print("Error: Student not found.")


def display_students():
    if not students:
        print("No students in the system.")
        return
    print("Student Grades:")
    for name, grades in students.items():
        if not grades:
            print(f"{name}: []")
        elif len(grades) == 1:
            print(f"{name}: {grades[0]}")
        else:
            print(f"{name}: {', '.join(str(g) for g in grades)}")


def main():
    while True:
        print("1. Add a new student")
        print("2. Update a grade")
        print("3. Remove a student")
        print("4. Display all students")
        print("5. Quit")

        choice = input("Choose an option: ").strip()
        if not choice.isdigit():
            print("Please enter a number between 1 and 5.")
            continue

        option = int(choice)

        if option == 1:
            add_student()
        elif option == 2:
            update_grade()
        elif option == 3:
            remove_student()
        elif option == 4:
            display_students()
        elif option == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == '__main__':
    main()
