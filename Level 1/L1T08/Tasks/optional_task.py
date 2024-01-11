# ==== This is an example of a program with a runtime and a logical error ====

# The program checks if a random number entered by the user is in a predefined list

found = False
list_num = [1, 3, 5, 7, 9]

print("Let's check if your number is in my list")

num = input("Enter a random number: ")
for i in range(1, 5):
    if num == list_num[i]:
        found = True
    else:
        found = False

if found == True:
    print("Number" + num + "is in the list" + list_num)
else:
    print("Number" + num + "is not in the list" + list_num)

# Above code has a runtime error in line 18 and 20 as variables are not casted correctly and
# it has 2 logical errors, one in line 11 as the range is incorrect and if the user enters number 1, 
# the prgram will think it is not in the range. 
# The other logical error is in the loop itself as this will not break until the last iteration and will
# only find the last number.

# ==== The correct coding is as it follows: ====

''' found = False
list_num = [1, 3, 5, 7, 9]

print("Let's check if your number is in my list")
num = int(input("Enter a random number: "))

for i in range(0, 5):
   if num == list_num[i]:
       found = True
       break
   else:
       found = False

if found == True:
   print(f"Number {num} is in the list {list_num}")
else:
   print(f"Number {num} is not in the list {list_num}") '''
