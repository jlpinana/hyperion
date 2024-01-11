# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # 1 Syntax error - Lion was missing symbol "" so Python knows that this is a string.
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" # 1 Logical error, the sentence as it is makes no sense, variables number_of_teeth and animal_type were in the wonrg place, they needed to be swapped

print(full_spec) # 1 Syntax error - print was missing parenthesis

