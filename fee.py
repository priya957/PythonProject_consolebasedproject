
class Fee:

    def __init__(self, student_id, student_name, total_fee):

        self.student_id = student_id
        self.student_name = student_name
        self.total_fee = total_fee
        self.paid_fee = 0

    def pay_fee(self, amount):

        if amount > 0 and amount <= self.total_fee - self.paid_fee:

            self.paid_fee = self.paid_fee + amount

            print("Fee paid successfully!")

        else:

            print("Invalid fee amount!")

    def show_fee(self):

        remaining_fee = self.total_fee - self.paid_fee

        print("\n========== FEE DETAILS ==========")
        print("Student ID:", self.student_id)
        print("Student Name:", self.student_name)
        print("Total Fee:", self.total_fee)
        print("Paid Fee:", self.paid_fee)
        print("Remaining Fee:", remaining_fee)
