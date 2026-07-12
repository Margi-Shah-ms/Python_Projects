print("Welcome to the Student Data Organizer!")
all_student = [] # stores data of all student 

while True: 
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Sujbects Offered")
    print("6. Exit")
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            s_id = int(input("Student ID: "))
            for s in all_student:
                if s["Student ID"] == s_id:
                    print("Student already exists!")
                    break  
            else:
                name = input("Name: ") # Student's name
                age = int(input("Age: ")) # Student's age
                grade = input("Grade: ") # Student's grade 
                dob = input("Date of Birth (YYYY-MM-DD): ")  # Student's Birth date
                sub = set(map(str.strip, input("Subjects (comma-separated): ").split(",")))
                t = (s_id, dob) # tuple 
                stu_dict = {
                    "Student ID": t[0],
                    "Name": name,
                    "Age": age,
                    "Grade": grade,
                    "Date of Birth": t[1],
                    "Subjects": sub
                }
                all_student.append(stu_dict)
                print("\nStudent added successfully!")
        case "2":
            print("\n--- Display All Students ---")
            if len(all_student) == 0:
                print("No Student exist")
            else:
                for student in all_student:
                    print(
                        f"Student ID: {student['Student ID']} | "
                        f"Name: {student['Name']} | "
                        f"Age: {student['Age']} | "
                        f"Grade: {student['Grade']} | "
                        f"Subjects: {', '.join(student['Subjects'])}")
        case "3":
            print("\n--- Update Student Information ---")
            s_id = int(input("Enter Student ID to update: "))
            for s in all_student:
                print("1. Update Age")
                print("2. Update Subject")
                c = int(input("enter choice: ")) 
                if c==1:
                    new_age = int(input("Enter New Age: "))
                    s["Age"] = new_age
                    print("New Age updated!")
                elif c==2:
                    new_sub = set(map(str.strip, input("Subjects (comma-separated): ").split(",")))
                    s["Subjects"].update(new_sub)
                    print("New Subject updated!") 
                else:
                    print("Invalid choice!")
                break
            else: 
                print("Student ID not found!") 
        case "4":
            print("\n--- Delete Student ---")
            s_id = int(input("Enter Student ID to delete: "))
            for s in all_student:
                if s["Student ID"] == s_id:
                    all_student.remove(s)
                    print("Student deleted successfully!")
                    break
<<<<<<< HEAD
=======
                
>>>>>>> 2a92ccf (Added Functional Treat project and updated Collection Manipulator)
            else:
                print("Student ID not found!")
        case "5": 
            print("\n--- Display Subjects Offered ---")
            s_id = int(input("Enter ID to see subjects: "))
            for s in all_student:
                if s["Student ID"]== s_id:
                    print(f" Subjects: {s['Name']} ")
                    print("Subjects Offered:")
                    print(", ".join(s["Subjects"])) 
                    break
        case "6":
            print("\nThank you for using the Student Data Organizer!")
            break
        
        case _:
            print("Invalid choice. Please try again.")
