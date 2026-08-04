from datetime import datetime
import time
import math
import random
import uuid   # universally unique identifier
import file_ops

print("========================")
print("Welcome to Multi-Utility Toolkit")
print("========================")
print("Choose an option:")
while True:
    print("\n1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    print("==========================")
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            print("\nDatetime and Time Operations:")
            print("1. Display current date and time")
            print("2. Calculate difference between two dates/times")
            print("3. Format date into custom format")
            print("4. Stopwatch")
            print("5. Countdown Timer")
            print("6. Back to Main Menu")
            while True:
                subchoice = input("Enter your choice: ")
                match subchoice:
                    case "1":
                        print("\nCurrent Date and Time:", datetime.now().date(), datetime.now().time())
                        print("============================")
                    case "2":
                        a = input(f"\nEnter the first date (YYYY-MM-DD): ")
                        b = input(f"Enter the second date (YYYY-MM-DD): ")
                        time_1 = datetime.strptime(a,"%Y-%m-%d") # convert a string into a datetime object
                        time_2 = datetime.strptime(b,"%Y-%m-%d")
                        c = abs(time_1-time_2)
                        print(f"Difference: {c.days} days")
                        print("============================")
                    case "3":
                        user_input = input("\nEnter date (DD/MM/YYYY): ")
                        a = datetime.strptime(user_input, "%d/%m/%Y") # converts a datetime, date, or time object into a formatted string
                        formatted_date = datetime.strftime(a, "%d-%m-%Y")
                        print("Formatted Date:", formatted_date)
                        print("=============================")
                    case "4":
                        input("\nPress ENTER to START...")
                        start_time = datetime.now()
                        input("Press ENTER to STOP...")
                        end_time = datetime.now()

                        stopwatch = end_time - start_time
                        print("Total Time:", stopwatch)
                        print("============================")
                    case "5":
                        seconds = int(input("\nEnter countdown time in seconds: "))
                        while seconds >= 0:
                            mins = seconds//60
                            secs = seconds%60
                            print(f"\nTime Remaining: {mins:02d}:{secs:02d}", end="")
                            time.sleep(1)   # it will stop the program for one second
                            seconds -= 1
                        print("\nTime up!")
                        print("=============================")
                    case "6":
                        break
                    case _:
                        print("Invalid Choice")
        case "2":
            print("\nMathematical Operations:")
            print("1. Calculate Factorial")
            print("2. Solve Compound Interest")
            print("3. Trigonometric Calculations")
            print("4. Area of Geometric Shapes")
            print("5. Back to Main Menu")
            while True:
                subchoice = input("Enter your choice: ")
                match subchoice:
                    case "1":
                        a = int(input("\nEnter a number: "))
                        c = math.factorial(a)
                        print(f"Factorial: {c}")
                        print("=========================")
                    case "2":
                        principal = int(input("\nEnter principal amount: "))
                        rate = int(input("Enter rate of interest (in %): "))
                        time = int(input("Enter time (in years): "))
                        amount = principal * ((1 + (rate / 100)) ** time)
                        print(f"Compound Interest: {amount:.2f}")
                        print("===========================")
                    case "3":
                        number_sin = int(input("\nEnter a number (Sine): "))
                        number_cos = int(input("Enter a number (Cosine): "))
                        number_tan = int(input("Enter a number (Tangent): "))
                        print("Sine: ",math.sin(math.radians(number_sin)))  
                        print("Cosine: ",math.cos(math.radians(number_cos)))  
                        print("Tangent: ",math.tan(math.radians(number_tan)))  
                        print("===============================")
                    case "4":
                        print("\nArea of Geometric Shapes:")
                        print("1. Circle")
                        print("2. Rectangle")
                        print("3. Triangle")
                        shape_choice = input("Enter your choice: ")
                        if shape_choice == "1":
                            radius = float(input("Enter radius of the circle: "))
                            area = math.pi * (radius ** 2)
                            print(f"Area of Circle: {area:.2f}")                            
                        elif shape_choice == "2":
                            length = float(input("Enter length of the rectangle: "))
                            width = float(input("Enter width of the rectangle: "))
                            area = length * width
                            print(f"Area of Rectangle: {area:.2f}")                   
                        elif shape_choice == "3":
                            base = float(input("Enter base of the triangle: "))
                            height = float(input("Enter height of the triangle: "))
                            area = 0.5 * base * height
                            print(f"Area of Triangle: {area:.2f}")        
                        else:
                            print("Invalid shape choice!")
                        print("====================================")
                    case "5":
                        break
                    case _:
                        print("Invalid Choice.")
                        
        case "3":
            print("\nRandom Data Generation:")
            print("1. Generate Random Number")
            print("2. Generate Random List")
            print("3. Create Random Password")
            print("4. Generate Random OTP")
            print("5. Back to Main Menu")
            while True:
                subchoice = input("Enter your choice: ")
                match subchoice:
                    case "1":
                        starts = int(input("\nEnter First Number: "))
                        ends = int(input("Enter Last number: "))
                        number = random.randint(starts,ends)
                        print("Generated Random Number is: ",number)
                        print("===============================")
                    case "2":
                        a = int(input("\nEnter: "))
                        l_ist = []
                        for i in range(a):
                            l_ist.append(random.randint(1,100))
                        print("Generated Random List: ",l_ist)
                        print("================================")                        
                    case "3":
                        pswrd = int(input("\nEnter password length: "))
                        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_"
                        a = random.choices(chars,k=pswrd)
                        b = "".join(a)
                        print("Generated Password:", b)
                        print("================================")
                    case "4":
                        otp = int(input("\nEnter OTP length (e.g., 4 or 6): "))
                        num = "0123456789"
                        gen_otp = "".join(random.choices(num, k=otp))
                        print("Generated Random OTP:",gen_otp)
                        print("====================================")
                    case "5":
                        break
                    case _:
                        print("Invalid chocie. Please try again.")
                        
        case "4": 
            print("Generate Unique Identifiers:")
            print("1. Generate Random UUID (UUID4)")
            print("2. Generate UUID for Specific Records, Files, or Sessions")
            print("3. Back to Main Menu")
            while True:
                subchoice = input("Enter your choice: ")
                match subchoice:
                    case "1":
                        print("\nGenerated UUID: ", uuid.uuid4())
                        print("=============================")
                    case "2":
                        record_name = input("\nEnter Record Name: ")
                        print(f"Record '{record_name}' linked with UUID: {uuid.uuid4()}")
                        print("=============================")
                    case "3":
                        break
                    case _:
                        print("Invalid Choice. Please try again!")
                                      
        case "5":
            print("\nFile Operations:")
            print("1. Create a new file")
            print("2. Write to a file")
            print("3. Read from a file")
            print("4. Append to a file")
            print("5. Back to Main Menu")
            while True:
                subchoice = input("Enter your choice: ")
                match subchoice:
                    case "1":
                        a = input("\nEnter file name: ")
                        file_ops.create_file(a)
                        print("File created successfully!")
                        print("=========================")
                    case "2":
                        a = input("\nEnter file name: ")
                        b = input("Enter data to write: ")
                        file_ops.write_file(a,b)
                        print("Data written successfully!")
                        print("==========================")
                    case "3":
                        a = input("\nEnter file name: ")
                        print("File Content:")
                        print(file_ops.read_file(a))
                        print("==============================")
                    case "4":
                        a = input("\nEnter file name: ")
                        b = input("Enter data to append: ")
                        file_ops.append_file(a,b)
                        print("File Content: ")
                        print("==============================")
                    case "5":
                        break
        case "6":
            print("\nExplore Module Attributes: ")
            a = input("Enter module name to explore: ")
            print(f"Available Attributes {a} module:")
            print(dir(a))
                        
        case "7":
            print("===================")
            print("Thank you for using the Multi-Utility Toolkit!")
            print("===================")
            break
        case _:
            print("Invalid Choice. Please try again!")