
class Person:

    def __init__(self, person_id, name, age, mobile):

        self.person_id = person_id
        self.name = name
        self.age = age
        self.mobile = mobile

    def display_details(self):

        print("ID:", self.person_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Mobile:", self.mobile)
