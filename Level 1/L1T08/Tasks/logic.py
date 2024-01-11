# ===== This is a program to demonstrate a logical error =====
# The program calculates the age in months of the user

# To make it easy, current month will be a constant.
current_month = 9

# User inputs age and month he/she was born.
print("Let's calculate your age in months!")
age = int(input("How old are you?\n"))
month = int(input("In which month were you born (add a number (e.g. 6 for June))?\n"))

total_months = age * 12
print(f"You are {total_months} months old")

# Above program has a logical error as the total number of months are not calculated correctly
# the program should also add to the total months the difference betwen the current month and the
# month the user was born. So the formula should be as this:
# total_months = (age * 12) + (current_month - month)