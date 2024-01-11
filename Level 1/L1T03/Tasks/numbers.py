# ===== This is the PSEUDOCODE =====
# Ask user to enter 3 integers
# Print the sum of all numbers
# Print the first number minus the second number
# Print 3rd number multiplied by 1st number
# Print sum of all numbers divided by the 3rd number

# ==== Program STARTS HERE ====
num_one = int(input("Please add an integer (non-decimal) number: "))
num_two = int(input("Please add another integer number: "))
num_three = int(input("Please add a 3rd integer number: "))
sum_nums = num_one + num_two + num_three
print(f"LET'S DO SOME CALCULATIONS WITH YOUR NUMBERS: {num_one}, {num_two} & {num_three}")
print(f"Sum: {num_one} + {num_two} + {num_three} = {sum_nums}")
sub_nums = num_one - num_two
print(f"Substraction: {num_one} - {num_two} = {sub_nums}")
mult_nums = num_one * num_three
print(f"Multiplication: {num_three} * {num_one} = {mult_nums}")
div_nums = sum_nums/num_three
print(f"Division: ({num_one} + {num_two} + {num_three})/{num_three}= {div_nums}")
