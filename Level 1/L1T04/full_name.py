name = input("Please input your full name:\n")
if len(name) == 0:
    print("You haven't enetered anything.\nPlease enter your full name")
elif len(name) < 4:
    print("You have entered less than 4 characters.\nPlease make sure that you have entered your name and surname:")
elif len(name) > 25:
    print("You have entered more than 25 characters.\nPlease make sure that you have only entered your full name")
else:
    print("Thank you for entering your name")