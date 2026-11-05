

from person import Person


class Teacher(Person):

    def __init__(self, teacher_id, name, age, mobile,
                 subject, salary):

        super().__init__(teacher_id, name, age, mobile)

        self.subject = subject
        self.salary = salary

    def display_details(self):

        print("\n========== TEACHER DETAILS ==========")

        super().display_details()

        print("Subject:", self.subject)
        print("Salary:", self.salary)
