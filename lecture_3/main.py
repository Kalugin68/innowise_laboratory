def calculate_average(grades):
    """Return the average of a grade list or None if division by zero occurs."""
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        return None


def add_student(students):
    """Add a new student to the students list if they do not already exist."""
    name = input("Enter student name: ").strip()

    # Check if the student already exists
    exists = any(s["name"].lower() == name.lower() for s in students)
    if exists:
        print("This student already exists.")
        return

    # Add a new student with empty grade list
    students.append({"name": name, "grades": []})


def add_grades(students):
    """Add grade values to an existing student's grade list."""
    name = input("Enter student name: ").strip()

    # Locate the student in the list
    student = None
    for s in students:
        if s["name"].lower() == name.lower():
            student = s
            break

    if not student:
        print("Student not found.")
        return

    # Continuously accept grades until 'done' is entered
    while True:
        grade_input = input("Enter a grade (or 'done' to finish): ").strip().lower()

        if grade_input == "done":
            break

        try:
            grade = int(grade_input)

            # Validate grade boundaries
            if 0 <= grade <= 100:
                student["grades"].append(grade)
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def show_report(students):
    """Display a full report of all students and calculate summary statistics."""
    if not students:
        print("No students available.")
        return

    print("\n--- Student Report ---")
    averages = []

    # Iterate over students and compute averages
    for s in students:
        avg = calculate_average(s["grades"])

        if avg is None:
            print(f"{s['name']}'s average grade is N/A.")
        else:
            print(f"{s['name']}'s average grade is {avg:.1f}.")
            averages.append(avg)

    print("-----------------------------------")

    # Display summary stats only if valid averages exist
    if averages:
        print(f"Max Average: {max(averages):.1f}")
        print(f"Min Average: {min(averages):.1f}")
        print(f"Overall Average: {(sum(averages) / len(averages)):.1f}")
    else:
        print("No valid grades were entered.")


def find_top_student(students):
    """Identify and display the student with the highest average grade."""
    if not students:
        print("No students available.")
        return

    valid_students = []

    # Build list of (student, average) for those with valid averages
    for s in students:
        avg = calculate_average(s["grades"])
        if avg is not None:
            valid_students.append((s, avg))

    if not valid_students:
        print("No students with valid grades.")
        return

    # Find the student with the maximum average
    top_student, top_avg = max(valid_students, key=lambda x: x[1])
    print(f"The student with the highest average is {top_student['name']} with a grade of {top_avg:.1f}.")


def main():
    """Main program loop handling the menu and user interaction."""
    students = []

    while True:
        print("\n--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit program")

        choice = input("Enter your choice: ")

        # Call the function corresponding to the user's choice
        if choice == "1":
            add_student(students)

        elif choice == "2":
            add_grades(students)

        elif choice == "3":
            show_report(students)

        elif choice == "4":
            find_top_student(students)

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


main()
