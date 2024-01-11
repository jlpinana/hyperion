class Adult():
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    def can_drive(self):
        print(f"\n{self.name} is old enough to drive")

class Child(Adult):
    def can_drive(self):
        print(f"\n{self.name} is too young to drive")


# User inputs
data = True
name = str(input("What is your name? "))

while data:
    try:
        age = int(input("How old are you? "))
        break

    except ValueError:
        print("ERROR - Please enter a number!") # Shows error if input is a string

hair_colour = str(input("What is your hair colour? "))
eye_colour = str(input("What colour are your eyes? "))

# Main logic
if age >= 18:
    driver_1 = Adult(name, age, eye_colour, hair_colour)

else:
    driver_1 = Child(name, age, eye_colour, hair_colour)

driver_1.can_drive()