# Data Analyzer and Transformer Program
print("Welcome to the Data Analyzer and Transformer Program")

arr =[] # 1D array 
while True:
    print("\nMenu:")  # displaying menu 
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")
    
# Menu Driven Interface 
    choice = input("Please enter your choice: ")
    match choice:
        case "1":
            print("\nEnter data for a 1D array (separated by spaces): ")
            n = input()
            separated = n.split()
            for i in separated:  
                a = int(i)
                arr.append(a)
            print("\nData has been stored successfully!") 
        
        case "2":
            def function(**kwargs):
                print("\nData Summary:")
                for key,value in kwargs.items():
                    print("-",key + ":",value)
            if len(arr) == 0:
                print("Please enter the array first.") 
            else:
                t = len(arr)
                mn = min(arr)
                mx = max(arr)
                sm = sum(arr)
                avg = sm / t
                
                function(Total_elements=t,Minimum_Value=mn,Maximum_Value=mx,
                         Sum= sm, Average = f"{avg:.2f}")
           
        case "3":
            def factorial(n):
                if n<0:
                    return "Invalid Input"
                if n==0 or n==1:
                    return 1
                return n * factorial(n-1)
            num = int(input("\nEnter a number to calculate its factorial: "))
            a = factorial(num)
            print(f"\nFactorial of {num} is: {a}")
            
        case "4":
            if len(arr) == 0:
                print("Enter array first!")
            else:
                threshold = int(input("\nEnter a threshold value to filter out data above this value:"))
                print(f"\nFiltered Data (values >= {threshold})")
                a = filter(lambda x: x>=threshold,arr)
                b = list(map(lambda x:x,a))
            print(" ".join(map(str, b))) 
            
        case "5":
            print("\nChoose sorting option:")
            print("1. Ascending")
            print("2. Descending")
            user = input("Enter your choice:")
            match user:
                case "1":
                    print("\nSorted Data in Ascending Order:")
                    arr.sort(reverse=False)
                    print(arr)
                case "2":
                    print("\nSorted Data in Descending Order:")
                    arr.sort(reverse=True)
                    print(arr)
            
        case "6":
            def stats():
                m_n = min(arr)
                m_x = max(arr)
                s_m = sum(arr)
                avg = s_m/len(arr)
                return m_n, m_x, s_m, avg # return multiple values
            
            def display_stats(*args):
                print("\nDataset Statistics:")
                m_in, m_ax, s_um, average = args  
                print("- Minimum value:", m_in)
                print("- Maximum value:", m_ax)
                print("- Sum of all values:", s_um)
                print(f"- Average value: {average:.2f}")
            
            if len(arr) == 0:
                print("Enter array first!")
            else:
                a,b,c,d = stats() 
                display_stats(a,b,c,d)
        case "7":
            print("\nThankyou for using the Data Analyzer and Transformer Program. Goodbye!")
            break