def process_student_data(student_data):
    if not student_data:
        print("There is no data found")
        return

    total_grades = 0
    num_students = 0
    failed_students = []

    for name, grade in student_data:
        try:
            grade = float(grade)
            total_grades += grade
            num_students += 1

            if grade < 50:
                failed_students.append(name)

        except ValueError:
            print(f"wrong grade value for {name}")

    if num_students > 0:
        average_grade = total_grades / num_students
        print(f"Average Grade: {average_grade:.2f}")

        if failed_students:
            print("Failed Students:")
            for student in failed_students:
                print(student)
        else:
            print("No students have failed.")

    else:
        print("No valid student data found.")
