# ==== Program to manipulate strings ====

# ==== PART 1 ====
# This part of the program changes the characters of a string
# inputed by the user so each even character becomes upper case 
# and each odd character becomes lower case 

print("This program manipulates strings")
user_string = input("Please add a sentence:\n")

new_string = "" # To store the new manipulated string

# Loop each character of the string inputed by the user
for i in range(len(user_string)):
    if i % 2 == 0:
        new_string += user_string[i].upper() # convert to upper case each even character
    else:
        new_string += user_string[i].lower() # convert to lower case each odd character

print("Let's change every even character to upper case and odd character to lower case:")
print(f"Your new sentence is:\n{new_string}")


# ==== PART 2 ====
# This part of the program changes the words of the string
# inputed by the user so each alternative word becomes upper case 
# and the others lower case 

final_string = [] # Holds the final list of words converted

other_string = user_string.split(" ") # Store the string in a list using space as the delimiter

for i in range(len(other_string)):
    if i % 2 == 0:
        final_string.append(other_string[i].upper()) # If even, convert word to upper case
    else:
        final_string.append(other_string[i].lower()) # If odd, convert word to lower case

print("Now let's convert each alternative word to upper case and the others to lower case.\nYour new sentence is:")
print(" ".join(final_string)) # Convert the list to a string separated by blank spaces

