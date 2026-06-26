# Welcome message
print("Welcome to the Pattern Generator and Number Analyzer!")
print()

# Asking user to enter the choice
    # Printing options for user to choose
while True:
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    choice = input("Enter your choice: ")
    match choice:
        case "1": # star pattern
            row=0
            positive = int(input("Enter the number of rows for the pattern:"))
            if positive>0:
                row=positive
            else:
                print("Invalid! Please try again.")
            if row>0:
                for i in range(1,row+1):
                    for j in range(1,i+1):
                        print("*", end="")
                    print()

        case "2": # even or odd
            while True:
                # Asking user to enter start and end
                start = int(input("Enter the start of the range: "))
                end = int(input("Enter the end of the range: ")) 
                if start <= 0 or end <= 0:
                    print("Invalid! Numbers must be positive (> 0). Please try again.\n")
                else:
                    break
            total_sum = 0 
            for i in range(start, end + 1):
                if i % 2 == 0:
                    print(f"Number {i} is Even")
                else:
                    print(f"Number {i} is Odd")
                total_sum += i # sum of all numbers.
            print(f"Sum of all numbers from {start} to {end} is: {total_sum}")
            
        case "3":
            print("Exiting the Program. Goodbye!") # good bye message
            break
        
        case _:
            print("Invalid Choice. Please enter 1,2 or 3.")