
"""try:
    name = input("Enter student name: ")
    marks = input("Enter student marks: ")

    # save data
    file = open("students.txt", "a")
    file.write("Name: " + name + ", Marks: " + marks + "\n")
    file.close()

    print("Student record saved successfully!\n")

    # read and display data
    print("--- All Student Records ---")
    file = open("students.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File not found.")

except IOError:
    print("File error occurred.")"""

try:
    # Add expense
    date = input("Date: ")
    category = input("Category: ")
    amount = input("Amount: ")

    file = open("expenses.csv", "a")
    file.write(date + "," + category + "," + amount + "\n")
    file.close()

    print("Expense saved\n")

    # View expenses
    file = open("expenses.csv", "r")
    print("--- Expenses ---")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File not found")

except IOError:
    print("File error")
       
