class Employee:
    "Comomn base class for all employees"
    empCount = 0


    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1


    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
         print ("Name : ", self.name,  ", Salary: ", self.salary)




# Creating instance Objects
"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
emp2 = Employee("Paul", 2300)

print(emp1.displayEmployee())
print(emp2.displayEmployee())


print("Total Employee %d" % Employee.empCount)

print(hasattr(emp1, "age"))
print(getattr(emp1,"name"))