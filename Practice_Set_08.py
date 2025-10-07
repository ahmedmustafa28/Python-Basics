#Q1: Create student class that takes name and marks of 3 subjects
#as arguments in constructor.
# Then create a method to print the average.
#
class Student:
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks

    def print_average (self) :
        sum =0
        for val in self.marks:
            sum += val
        print("Hey",self.name,"your average score is",sum/3)

s1 = Student("Ahmed Mustafa",[78,89,90])
s1.print_average()

#Q2:Create Account class with 2 attributes - balance & account number.
#Create methods for debit, credit, and printing the balance.

class Account:
    def __init__(self,bal,acc_no):
        self.balance = bal
        self.account_number = acc_no

    def debit (self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited.")
        print("Remaining Balance is",self.get_bal())

    def credit (self,amount):
        self.balance += amount
        print("Rs.",amount,"was credited.")
        print("Remaining Balance is",self.get_bal())

    def get_bal (self):
        return self.balance

acc1 = Account(12000,90673521)
acc1.debit(2300)
acc1.credit(3650)