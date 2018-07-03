import datetime


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last             # Atributos de la clase
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.set_raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amount = 1.50

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer("Aedel", "Darko", 5000, "Python")
dev_2 = Developer("Kwisatz", "Haderach", 100000, "Java")

mgr_1 = Manager("Sue", "Smith", 9000, [dev_1])
print(mgr_1.email)

mgr_1.add_employee(dev_2)

mgr_1.print_emps()

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.email)
print(dev_1.prog_lang)
emp1 = Employee("Corey", "Schafer", 50000)
emp2 = Employee("Test", "User", 60000)
emp_str_1 = "John-Doe-70000"

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.pay)
print(new_emp_1.fullname())

# print(emp1)
# print(emp2)

print(emp1.email)
print(emp2.pay)

print(Employee.fullname(emp1))
print(emp1.fullname())

print(Employee.fullname(emp2))
print(emp2.fullname())

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

print(Employee.__dict__)

emp1.raise_amount = 1.05
print(emp1.__dict__)

print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)
print(Employee.num_of_emps)

Employee.set_raise_amt(1.05)

print(Employee.set_raise_amt)
print(emp1.set_raise_amt)
print(emp2.set_raise_amt)

my_date = datetime.date(2018, 7, 2)

print(Employee.is_workday(my_date))

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))
