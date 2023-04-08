class Person(object):
    def __init__(self, name,age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Name: ",self.name)
        print("Age :",self.age)

class Employee(Person):
    def __init__(self,name,age, employee_id):
        super().__init__(name,age)
        self.employee_id = employee_id
    def display(self):
        super().display()
        print("Employee ID :",self.employee_id)

person = Employee("Rahidul", 34, 2345)
person.display()