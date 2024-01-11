# ==== Program CALCULATOR ==== 
# ==== You can perform calculations ====
# ==== You can store the calculations in a file and view them any time ==== 

# Program start
from pathlib import Path # I had to Google this. It is used to check the path of a file and see whether it exists.

# Function to display user menu and ask user to choose option
def show_menu ():
    while data:
        print("---------------")
        print("Calculator Menu")
        print("1: Perform a calculation")
        print("2: View previous calculations")
        print("3: Exit")
        print("---------------")
        try:
            option = int(input("Select an option: "))
            if option < 1 or option > 3:
                raise Exception
            break
        except Exception:
            print("ERROR - Please enter a valid option!\n") # Displays error if user doesn't enter a number or enters wrong number
    return (option)

# Function to check number inputs from user
def input_num ():
    while data:
        try:
            num = float(input("Add a number: ")) 
            break
        except ValueError:
            print("ERROR - Please enter a valid number!") # Shows error if input is a string
    return (num)

# Function to check operator inputed by user
def input_operation (number):
    while data:
        try:
            if number == 0: 
                valid_operations = ['+', '-', '*'] # Does not allow division if 2nd user number is '0'
                operation = input("Add an operation (+, -, or *): ")
            else: 
                valid_operations = ['+', '-', '*', '/']
                operation = input("Add an operation (+, -, *, or /): ")
            if operation in valid_operations:
                break
            else:    
                raise Exception
        except Exception:
            print("ERROR - Please add a valid operation!")
    return (operation)

# Function to perform calculations
def calculate (var1, var2, var3):
    if var3 == '+':
        result = var1 + var2
    elif var3 == '-':
        result = var1 - var2
    elif var3 == '*':
        result = var1 * var2
    else:
        result = round(var1/var2, 2)
    return result

# Main program starts here
data = True
menu_select = 2
while menu_select != 3:
    menu_select = show_menu ()

    if menu_select == 1: # Calculator menu
        x = input_num ()
        y = input_num ()
        operator = input_operation (y)
        eq_result = calculate(x, y, operator) # Perform calculation
        print(f"{x} {operator} {y} = {eq_result}\n")
        with open('equations.txt', 'a') as f:
            f.write(f"{x} {operator} {y} = {eq_result} \n") # Store calculation in file
    
    elif menu_select == 2: # View equations from file
        path = Path('./equations.txt') # I had to Google this in order to use... 
        if path.is_file() == False:    # ...an if statement instead of exception handling with try-except.
            print("ERROR - File does not exist. Use menu 1 to store data first!\n") # Gives error if file doesn'r exist.
        else:
            print("This is the list of equations previously entered:")
            with open('equations.txt', 'r+') as f:
                lines = f.readlines()
                for line in lines:
                    print(line) # Shows previous equations
    else:    
        print("Thanks for using my calculator. Good bye!") # Exit program