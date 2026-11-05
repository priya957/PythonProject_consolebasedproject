


from student import Student
from teacher import Teacher


class School:

    def __init__(self):
        self.students = []
        self.teachers = []
        self.fees = []

    # ================= STUDENT METHODS =================

    def add_student(self, student):
        for s in self.students:
            if s.person_id == student.person_id:
                print("Student ID already exists!")
                return

        self.students.append(student)
        print("Student added successfully!")

    def view_students(self):
        if len(self.students) == 0:
            print("No students available!")
        else:
            for student in self.students:
                student.display_details()

    def search_student(self, student_id):
        for student in self.students:
            if student.person_id == student_id:
                student.display_details()
                return

        print("Student not found!")

    def update_student(self, student_id):
        for student in self.students:
            if student.person_id == student_id:

                print("\n1. Update Name")
                print("2. Update Age")
                print("3. Update Mobile")
                print("4. Update Class")
                print("5. Update Section")
                print("6. Update Address")

                choice = input("Enter choice: ")

                if choice == "1":
                    student.name = input("Enter new name: ")

                elif choice == "2":
                    student.age = int(input("Enter new age: "))

                elif choice == "3":
                    student.mobile = input("Enter new mobile: ")

                elif choice == "4":
                    student.class_name = input("Enter new class: ")

                elif choice == "5":
                    student.section = input("Enter new section: ")

                elif choice == "6":
                    student.address = input("Enter new address: ")

                else:
                    print("Invalid choice!")
                    return

                print("Student updated successfully!")
                return

        print("Student not found!")

    def delete_student(self, student_id):
        for student in self.students:
            if student.person_id == student_id:
                self.students.remove(student)
                print("Student deleted successfully!")
                return

        print("Student not found!")

    # ================= TEACHER METHODS =================

    def add_teacher(self, teacher):
        for t in self.teachers:
            if t.person_id == teacher.person_id:
                print("Teacher ID already exists!")
                return

        self.teachers.append(teacher)
        print("Teacher added successfully!")

    def view_teachers(self):
        if len(self.teachers) == 0:
            print("No teachers available!")
        else:
            for teacher in self.teachers:
                teacher.display_details()

    def search_teacher(self, teacher_id):
        for teacher in self.teachers:
            if teacher.person_id == teacher_id:
                teacher.display_details()
                return

        print("Teacher not found!")

    # NEW FEATURE: UPDATE TEACHER

    def update_teacher(self, teacher_id):
        for teacher in self.teachers:

            if teacher.person_id == teacher_id:

                print("\n========== UPDATE TEACHER ==========")
                print("1. Update Name")
                print("2. Update Age")
                print("3. Update Mobile")
                print("4. Update Subject")
                print("5. Update Salary")

                choice = input("Enter your choice: ")

                if choice == "1":
                    teacher.name = input("Enter new name: ")

                elif choice == "2":
                    teacher.age = int(input("Enter new age: "))

                elif choice == "3":
                    teacher.mobile = input("Enter new mobile: ")

                elif choice == "4":
                    teacher.subject = input("Enter new subject: ")

                elif choice == "5":
                    teacher.salary = float(input("Enter new salary: "))

                else:
                    print("Invalid choice!")
                    return

                print("Teacher details updated successfully!")
                return

        print("Teacher not found!")

    # ================= FEE METHODS =================

    def add_fee(self, fee):
        self.fees.append(fee)
        print("Fee record added successfully!")

    def view_fees(self):
        if len(self.fees) == 0:
            print("No fee records found!")
        else:
            for fee in self.fees:
                fee.show_fee()

    def pay_student_fee(self, student_id, amount):
        for fee in self.fees:
            if fee.student_id == student_id:
                fee.pay_fee(amount)
                return

        print("Fee record not found!")
