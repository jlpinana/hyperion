# ===== Program to output start pattern =====
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# ===== Start of program =====
stars = "*"
n = 4 # Pointer starts at 4 to be used to print the decremental stars.
print("Printing a sequence of stars from 1 to 5 and back down to 1. Enjoy it!")
for i in range (0, 10):
    if i < 5:
        print(stars) # Prints the incremental stars
        stars = stars + "*"
    else:
        print(stars[0:n]) # Prints the decremental stars
        n -= 1

