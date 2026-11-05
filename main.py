from school import School
from student import Student
from teacher import Teacher
from fee import Fee


school = School()

while True:

    print("\n========== SCHOOL MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Add Teacher")
    print("7. View Teachers")
    print("8. Search Teacher")
    print("9. Add Student Fee")
    print("10. View Fee Details")
    print("11. Pay Student Fee")
    print("12. Update Teacher")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        mobile = input("Enter Mobile: ")
        class_name = input("Enter Class: ")
        section = input("Enter Section: ")
        address = input("Enter Address: ")

        student = Student(student_id, name, age, mobile,
                          class_name, section, address)
        school.add_student(student)

    elif choice == "2":
        school.view_students()

    elif choice == "3":
        student_id = input("Enter Student ID: ")
        school.search_student(student_id)

    elif choice == "4":
        student_id = input("Enter Student ID: ")
        school.update_student(student_id)

    elif choice == "5":
        student_id = input("Enter Student ID: ")
        school.delete_student(student_id)

    elif choice == "6":
        teacher_id = input("Enter Teacher ID: ")
        name = input("Enter Teacher Name: ")
        age = int(input("Enter Age: "))
        mobile = input("Enter Mobile: ")
        subject = input("Enter Subject: ")
        salary = float(input("Enter Salary: "))

        teacher = Teacher(teacher_id, name, age, mobile,
                          subject, salary)
        school.add_teacher(teacher)

    elif choice == "7":
        school.view_teachers()

    elif choice == "8":
        teacher_id = input("Enter Teacher ID: ")
        school.search_teacher(teacher_id)

    elif choice == "9":
        student_id = input("Enter Student ID: ")
        student_name = input("Enter Student Name: ")
        total_fee = float(input("Enter Total Fee: "))

        fee = Fee(student_id, student_name, total_fee)
        school.add_fee(fee)

    elif choice == "10":
        school.view_fees()

    elif choice == "11":
        student_id = input("Enter Student ID: ")
        amount = float(input("Enter Fee Amount: "))
        school.pay_student_fee(student_id, amount)

    elif choice == "12":
        teacher_id = input("Enter Teacher ID: ")
        school.update_teacher(teacher_id)

    elif choice == "0":
        print("Thank you for using School Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
