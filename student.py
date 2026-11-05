
from person import Person


class Student(Person):

    def __init__(self, student_id, name, age, mobile,
                 class_name, section, address):

        super().__init__(student_id, name, age, mobile)

        self.class_name = class_name
        self.section = section
        self.address = address

    def display_details(self):

        print("\n========== STUDENT DETAILS ==========")

        super().display_details()

        print("Class:", self.class_name)
        print("Section:", self.section)
        print("Address:", self.address)
