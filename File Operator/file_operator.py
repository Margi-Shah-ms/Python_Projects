from datetime import datetime
import os

class JournalManager:
    def __init__(self, files = 'journal.txt'):
        self.files = files
    def addentry(self):
        entry = input("Enter your journal entry:")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.files,"a") as file:
            file.write(f"[{current_time}]\n{entry}")
        print("\nEntry added successfully!")
        
    def view(self):
        try:
            with open(self.files,"r") as file:
                content = file.read()
                if content.strip() == "":
                    print("Output (if the file does not exist):")
                    print("No journal entries found. Start by adding a new entry!")
                else:
                    print("Output (If the file exists):")
                    print("\nYour Journal Entries:")
                    print("----------------------------------")
                    print(content)
        except FileNotFoundError:
            print("Output:")
            print("Error: The journal file does not exist. Please add a new entry first.")
                    
    def search(self):
        kw = input("Enter a keyword or date to search: ")
        try:
            with open(self.files, "r") as file:
                entries = file.readlines()
                print("\n Output (If a match is found):")
                print("Matching Entries:")
                print("----------------------------------")
                count = 0
                for l in entries:
                    if kw.lower() in l.lower():
                        print(l.strip())
                        count += 1
                if count == 0:
                        print(f"\nNo entries were found for the keyword: {kw}")
        except FileNotFoundError:
            print("\nThe journal file does not exist.")
            
    def delete_entry(self):
        confirm = input("Are you sure you want to delete all entries? (yes/no): ")
        if confirm.lower() == "yes":
            try:
                os.remove(self.files)
                print("\nOutput (If the file is deleted successfully):")
                print("All journal entries have been deleted.")

            except FileNotFoundError:
                print("Output (If the file does not exist):")
                print("No journal entries to delete.")
        else:
            print(" Deletion cancelled.") 

j = JournalManager()
print("Welcome to Personal Journal Manager!")
print("Please select an option:")
while True:
    print("\n1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("User Input: ")
    match choice:
        case "1":
            j.addentry()
        case "2":
            j.view()
        case "3":
            j.search()
        case "4":
            j.delete_entry()
        case "5":
            print("Output:")
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break
        case _:
            print("Output:")
            print("Invalid option. Please select a valid option from the menu.")