# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") # [Jose] 1 Syntax error - print was missing the parenthesis.
print("\n") # [Jose] 2 Syntax errors - print was missing the parenthesis and it was indented.

# Variables declaring the user's age, casting the str to an int, and printing the result

age_Str = "24" # [Jose] 1 Syntax error - This was indented. 1 Logical error - It was using == (comparing) instead of = (to asign the value to the variable)
age = int(age_Str) # [Jose] 1 Syntax error - This was indented. 1 Runtime error - The variable age_Str cannot be casted to integer as it contained a number and a string of characters "years old". To fix it, the words years old needed to be removed.
print("I'm " + str(age) + " years old.") # [Jose] 1 Syntax error - This was indented. 1 Runtime error - variable age needs to be casted into a string.

# Variables declaring additional years and printing the total years of age
years_from_now = "3" # [Jose] 1 Syntax error - This was indented.
total_years = age + int(years_from_now) # [Jose] 1 Syntax error - This was indented. 1 Runtime error - variable years_from_now needs to be casted to integer

print("The total number of years: " + str(total_years)) # [Jose] 3 Syntax error - print was missing the parenthesis. Variable was misspelled (should be total_years instead of answer_years) and it should not be between "". 1 runtime error - total_years should be casted to string

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 + 6 # [Jose] 1 syntax error - variable total was misspelled, should have been total_years. 1 Logical error - The formula was missing adding the 6 months.
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old") # [Jose] Syntax error - print was missing the parenthesis. 1 Runtime error - variable total_months needs to be casted to string

#HINT, 330 months is the correct answer

