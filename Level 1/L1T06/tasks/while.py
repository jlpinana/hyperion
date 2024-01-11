# Program to calculate average of numbers entered by user

# Initialise variables
# We will use the following variables:
# imp_num to store numbers entered by user
# sum_num to sotre the sum of numbers entered
# st_nums to store the numbers entered by user so we can show them at the end. This is not needed for this program
# but I wanted to challenge myself a bit.
inp_num = 0  
sum_num = 0  
st_nums = []

print("Program to calculate numbers average\n")

while inp_num != -1:
    inp_num = int(input("Please add a random number (-1 to exit):\n"))
    if inp_num != -1: # Condition so the list appends all numbers except -1
        st_nums.append(inp_num) # I needed help from a work coleague to do this as I was not familiar with the append command.
    sum_num = inp_num + sum_num # Better to do: sum_num += inp_num

    if inp_num == -1:
        break
    average = sum_num/len(st_nums) 
print(f"The {len(st_nums)} numbers you entered are:\n {st_nums}")
print(f"The average of these numbers is: {average}")

# NOTE - Initially I used a variable called counter to count the numbers that the user
# has introduced, but after talking to a coleague at work I realised I could use the len() function instead.
