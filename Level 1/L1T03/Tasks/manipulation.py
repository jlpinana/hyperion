# ===== This is the PSEUDOCODE =====
# Ask user to enter a string
# Calculate and display the length of the string
# Find the last letter of the string and replace every occurrance of the letter with the characeter @
# Show modified sentence on screen
# Print the last 3 characters from the original sentence in reverse order
# Create 5 letter word using the first 3 characters and last 2 characters of the original sentence.
# Print the 5 letter word

# ===== Program starts here =====
str_manip = input("Please add a random sentence with more than 2 words: ")
print(f"The lenght of the sentence '{str_manip}' is: {len(str_manip)}")
len_sentence = len(str_manip)
last_letter = str_manip[-1]
print(f"The last letter of the sentence is: {last_letter}")
mod_sentence = str_manip.replace(last_letter,"@")
print(f"Replacing all instances of the letter '{last_letter}' with '@', the new sentence is:")
print(mod_sentence)
print("The last 3 characters of your sentence in reverse order are:")
print(str_manip[:-4:-1])
print("A 5-letter word using the first 3 characters and last 2 characters of your sentence is:")
print(f"{str_manip[0:3]}{str_manip[-2::]}")