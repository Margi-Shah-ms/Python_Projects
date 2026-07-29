Click here for the video: https://drive.google.com/file/d/18lFyelWh0Qt53y2wBwRM7BYz2v7pZUzZ/view?usp=sharing

# 👨‍💼 Employee Management System

> A Python Object-Oriented Programming (OOP) project that demonstrates the implementation of **Encapsulation**, **Inheritance**, **Polymorphism**, **Method Overriding**, and **Menu-Driven Programming**.

---

## 📌 Project Overview

The **Employee Management System** is a console-based Python application designed to manage different types of individuals within an organization.

Using this system, users can:

✅ Create a Person
✅ Create an Employee
✅ Create a Manager
✅ Create a Developer
✅ View stored details
✅ Explore core OOP concepts in action

This project serves as a practical demonstration of Object-Oriented Programming principles in Python.

---

## 🚀 Features

✨ Create and manage multiple types of entities

* 👤 Person
* 💼 Employee
* 👨‍💼 Manager
* 👨‍💻 Developer

✨ Display detailed information for each entity

✨ Encapsulate sensitive employee data

✨ Demonstrate inheritance and method overriding

✨ User-friendly menu-driven interface

✨ Validate object creation before displaying details

---

## 🏗️ OOP Concepts Implemented

### 🔒 Encapsulation

Employee ID and Salary are declared as private attributes:

```python
self.__employee_id
self.__salary
```

Access is provided through getter methods:

```python
get_emp()
get_sal()
```

---

### 🧬 Inheritance

Both Manager and Developer inherit from the Employee class.

```python
class Manager(Employee):
```

```python
class Developer(Employee):
```

This helps in code reusability and hierarchical design.

---

### 🔄 Method Overriding

The `display()` method is overridden in:

* Manager Class
* Developer Class

This allows each class to provide its own customized output.

---

### ⚡ Constructors

Every class uses the `__init__()` constructor to initialize object attributes.

---

### 🎭 Polymorphism

The overridden `display()` methods demonstrate runtime polymorphism.

---

### ⬆️ super() Function

The parent class constructor is called using:

```python
super().__init__(employee_id, name, age, salary)
```

This avoids code duplication and improves maintainability.

---

## 📂 Class Structure

### 👤 Person

**Attributes**

* Name
* Age

**Methods**

* `display()`
* `person_details()`

---

### 💼 Employee

**Attributes**

* Employee ID (Private)
* Name
* Age
* Salary (Private)

**Methods**

* `get_emp()`
* `get_sal()`
* `display()`
* `emp_details()`

---

### 👨‍💼 Manager (Inherited from Employee)

**Additional Attribute**

* Department

**Methods**

* `display()`
* `manager_details()`

---

### 👨‍💻 Developer (Inherited from Employee)

**Additional Attribute**

* Programming Language

**Methods**

* `display()`
* `developer_details()`

---

## 🖥️ Menu Interface

```text
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit
```

---

## 🎯 Learning Outcomes

Through this project, I gained hands-on experience with:

* ✅ Classes & Objects
* ✅ Encapsulation
* ✅ Inheritance
* ✅ Polymorphism
* ✅ Method Overriding
* ✅ Constructors
* ✅ Getter Methods
* ✅ Match-Case Statements
* ✅ Menu-Driven Programming
* ✅ Object Validation

---

## 🛠️ Technologies Used

| Technology      | Purpose                 |
| --------------- | ----------------------- |
| 🐍 Python 3     | Application Development |
| 💡 OOP Concepts | Program Design          |
| 🖥️ VS Code     | Development Environment |

---


## 📸 Sample Output
<img width="549" height="727" alt="image" src="https://github.com/user-attachments/assets/84556304-108a-4d81-afb6-bef8b840bb53" /> 
<img width="605" height="761" alt="image" src="https://github.com/user-attachments/assets/f8484417-4787-4bf4-9ff1-b31097a00c43" />




---

Python OOP Practice Project 🚀
