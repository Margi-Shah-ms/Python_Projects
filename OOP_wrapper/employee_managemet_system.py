print("--- Python OOP Project: Employee Management System ---")
class Person:
    def __init__(self,name,age):  # Constructor
        self.name = name   # self represent current object
        self.age = age
    def display(self):
        print(f"\nPerson created with name: {self.name} and age: {self.age}.")
    def person_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        
class Employee:
    def __init__(self,employee_id,name,age,salary):
        self.__employee_id = employee_id  # Encapsulation
        self.name = name
        self.age = age
        self.__salary = salary
    def get_emp(self):
        return self.__employee_id
    def get_sal(self):
        return self.__salary
    def display(self):
        print(f"\nEmployee created with name: {self.name}, age: {self.age}, ID: {self.__employee_id},and salary: ${self.__salary}.")
    def emp_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.__employee_id}")
        print(f"Salary: ${self.__salary}")

class Manager(Employee):
    def __init__(self, employee_id, name, age, salary, department):
        super().__init__(employee_id, name, age, salary)
        self.department = department

    def display(self):  # Method Overriding 
        print(f"\nManager created with name: {self.name}, age: {self.age}, ID: {self.get_emp()}, salary: ${self.get_sal()}, and department: {self.department}.")

    def manager_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.get_emp()}")
        print(f"Salary: ${self.get_sal()}")
        print(f"Department: {self.department}")

class Developer(Employee):
    def __init__(self, employee_id, name, age, salary, programming_language):
        super().__init__(employee_id, name, age, salary)
        self.programming_language = programming_language 

    def display(self):
        print(f"\nDeveloper created with name: {self.name}, age: {self.age}, ID: {self.get_emp()}, salary: ${self.get_sal()}, and Programming Language: {self.programming_language}.")

    def developer_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.get_emp()}")
        print(f"Salary: ${self.get_sal()}")
        print(f"Programming Language: {self.programming_language}")

p = None
e = None
m = None
d = None
while True:
    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Create a Developer")
    print("5. Show Details")
    print("6. Exit")
    choice = input("\nEnter your choice: ")
    match choice:
        case "1":
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            p = Person(name, age)
            p.display()
            print("\n--- Choose another operation ---")
            
        case "2":
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            employee_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            e = Employee(employee_id,name,age,salary)
            e.get_emp()
            e.get_sal()
            e.display()
            print("\n--- Choose another operation ---")
            
        case "3":
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            employee_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            department = input("Enter Department: ")
            m = Manager(employee_id,name,age,salary,department)
            m.display()
            print("Manager is sublcass of Employee: ",issubclass(Manager,Employee))
            print("\n--- Choose another operation ---")  
            
        case "4":
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            employee_id = input("Enter Developer ID: ")
            salary = float(input("Enter Salary: "))
            language = input("Enter Programming Language: ")
            d = Developer(employee_id,name,age,salary,language)
            d.display()
            print("Developer is sublcass of Employee: ",issubclass(Developer,Employee))
            print("\n--- Choose another operation ---") 
                        
        case "5":
            print("\nChoose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            print("4. Developer")
            c = input("Enter your choice: ")
            match c:
                case "1":
                    if p != None:
                        print("\nPerson Details:")
                        p.person_details()
                    else:
                        print("\nPerson not created yet!")
                case "2":
                    if e != None:
                        print("\nEmployee Details:")
                        e.emp_details() 
                    else:
                        print("\nEmployee not created yet!")
                case "3":
                    if m != None:
                        print("\nManager Details:")
                        m.manager_details()
                    else:
                        print("\nManager not created yet!")
                case "4":
                    if d != None:
                        print("\nDeveloper Details:")
                        d.developer_details()
                    else:
                        print("\nDeveloper not created yet!")
                        
            print("\n--- Choose another operation ---")
                               
        case "6":
            print("\nExiting the system. All resources have been freed.")
            print("\nGoodbye!")
            break
        
        case _:
            print("Invalid choice. Please try again!")
            
            
            