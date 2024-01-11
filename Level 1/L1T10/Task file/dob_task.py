# ==== Program to read from file =====

print("This program reads a file called DOB.txt\nand shows a list with all the names and then all the birthdates\n")

# ****** Read and display NAMES ******
file = open('DOB.txt','r+', encoding='utf-8')

lines = file.readlines()

print("NAME")
for line in lines:
    name = line.split()
    print(name[0] + " " + name[1]) # Prints name and surname

# ****** Read and display birth dates ******
print("\nBirthdate")
for line in lines:
    dob = line.split()
    print(dob[2] + " " + dob[3] + " " + dob[4]) # Prints DOB

file.close()