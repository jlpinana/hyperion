# ==== Program to allow users to register for exam venue ====

print("Welcome to the exam users regitration")
total_users = int(input("Please specify the amount of users that will be registering\n"))
   
with open('reg_form.txt', 'w') as f:
    f.write("STUDENTS REGISTERED FOR THE EXAM:\n")
    for i in range (0, total_users):
        id = input("Please add the ID of the student to be registered:\n")
        f.write(id + "\n" + ".......................\n")




