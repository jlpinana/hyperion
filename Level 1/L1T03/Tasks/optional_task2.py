string_fav = input("Add the name of your favourite restaurant: ")
int_fav = int(input("What is your favourite number? "))
print(string_fav)
print(int_fav)

# Now casting string_fav to integer
string_fav = int(string_fav)
print(string_fav)

# If I cast the variable string_fav to an interger, an error occurs when the user adds a string 
# of characters as the name of the restaurant. 
# I believe this is because you cannot cast a string of non numerical characters into an integer.  
# I have also noticed that the way the code is currently written,
# if you add a decimal number as the favourite number, there will be an error.
# I am not sure why this happens but having read in the link: https://stackoverflow.com/questions/1094717/convert-a-string-to-integer-with-decimal-in-python
# it seems that you need to cast the number as float before casting it as integer,
# so the code would be:
# int_fav = int(float(input("What is your favourite number? ")))