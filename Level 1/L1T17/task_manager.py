#=====importing libraries===========
import time
from datetime import date, datetime
import os
from pathlib import Path


#====Login Section====
def login():
    '''Allows a user to log into the program.'''      
    names, passwords = read_users_file()
    log_user = False
    attempts = 0

    while log_user == False:
        if attempts < 3:
            # Only 3 consecutive login attemps are allowed
            username = input("Username: ")
            password = input("Password: ")

            if username in names:
                index = names.index(username)

                if password == passwords[index]: # Password can only be the one of the user trying to log in
                    log_user = True
                    print("----------------------------")
                    print("Login susscessful! Welcome!!")
                    print("----------------------------")

                else:
                    print('Invalid password! Please try again\n')
                    attempts += 1

            else:
                print('Username not found! Please try again\n')
                attempts += 1

        else:
            attempts = 0
            countdown(5)

    return(username)


def read_users_file():
    '''Reads data from user file and stores usernames and passwords in 2 different lists'''
    names = []
    passwords = []

    with open('user.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        users = line.split() # removes spaces

    for i in range(len(users)):
        users[i] = users[i].replace(",","") # removes comas

        if i % 2 == 0:
            names.append(users[i]) # even index numbers are stored as names

        else:
            passwords.append(users[i]) # odd index numbers are stored as passwords
            
    return names, passwords


def welcome():
    '''Displays user welcome message.'''
    print("===========================")
    print("++++++ TASK MANAGER +++++++")
    print("===========================")
    print("")
    print("LOGIN")
    print("----------------------------------------------------")
    print("Enter your login details below to access the system:")
    print("----------------------------------------------------")
   

'''I had to Google how to create a countdown timer in Python. 
Found this in: https://www.programiz.com/python-programming/examples/countdown-timer'''
def countdown(time_sec):
    '''Displays error message and shows countdown timer'''
    print("Too many attempts! Try again in...")
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    welcome()


'''I Googled this and found a useful article in: 
https://ioflood.com/blog/python-get-current-date/#:~:
text=To%20get%20the%20current%20date%20in%20Python%2C%20you%20can%20use,%2DMM%2DDD'%20format.'''
def calc_date():
    '''Calculates todays date in format dd Mmm yyyy'''
    today = date.today()
    formatted_date = today.strftime('%d %b %Y')
    return(formatted_date)


def check_tasks():
    '''Checks whether file is empty or doesn't exist
    source: https://pythonhow.com/how/check-if-a-text-file-is-empty/'''
    path = Path('./tasks.txt')
    if os.path.getsize('tasks.txt') == 0 or path.is_file() == False:
        return(False)
    else:
        return(True)


#==== Main program starts here ====    
welcome()
logged_user = login()
while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    if logged_user == 'admin':
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
st - show statistics
e - exit
: ''').lower()
    else:
        menu = input('''Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    if menu == 'r' and logged_user == 'admin':
        '''This code block will add a new user to the user.txt file'''
        print('------------------------------------')
        print('Register a new user into the system:')
        print('------------------------------------')
        names, passwords = read_users_file()
        user_added = False

        while user_added == False:
            user_name = input('Enter user name: ')

            if user_name.isalpha() == False: # Checks that name contains only letters
                '''Source: https://careerkarma.com/blog/python-isalpha-isnumeric-isalnum/#:~:text=The%20Python%20isalpha()%20method,contains%20alphanumeric%20characters%2C%20without%20symbols.'''
                print("No numbers allowed! Please add a correct name")

            elif user_name in names:
                print("This user name already exists! Please try again")

            else:
                pass1 = input('Enter password: ')
                pass2 = input("repeat password: ")

                if pass2 != pass1:
                    print("Passwords don't match! Please try again\n")

                else:
                    with open('user.txt', 'a+') as f:
                        f.write(" " + user_name + ", " + pass2)
                    user_added = True
                    print('-------------------------')
                    print('User added succesfully!\n')
                    print('-------------------------')

    elif menu == 'a':
        '''This code block will allow a user to add a new task to task.txt file'''
        print('------------------------------------')
        print('Assign a new task:')
        print('------------------------------------')
        print('Please add the following task details:')

        t_owner_exists = False
        names, passwords = read_users_file()

        while t_owner_exists == False:
            print(f"Assign task to: {names}") # Shows available users registered
            t_owner = input("Select task owner: ")

            if t_owner in names:
                t_owner_exists = True

            else:
                print("Task owner does not exist in the system! Please try again")


        title_ok = False

        while title_ok == False:
            t_title = input("Task name: ")

            if len(t_title) > 25:
                print("Too long! Please add a title less than 25 characters")

            else:
                title_ok = True

        descrip_ok = False

        while descrip_ok == False:
            t_descrip = input("Task description:\n")

            if len(t_descrip) > 100:
                print("Too long! Please add a description less than 100 characters!")

            else:
                descrip_ok = True

        '''This code block checks that the date is entered in the right format
        I had to Google this - source: https://www.geeksforgeeks.org/python-validate-string-date-format/'''
        date_ok = False

        while date_ok == False:
            format = "%d %b %Y"
            t_due_date = input("Due date (dd mmm yyyy): ")

            try:
                date_ok = bool(datetime.strptime(t_due_date, format)) 

            except ValueError:
                print("Wrong date format! Please add a correct date in the format (dd Mmm yyyy)")

            if t_due_date < calc_date():
                print("Due date cannot be in the past! Please add another date.")
                date_ok = False

        with open('tasks.txt', 'a+') as file:
            file.write('\n')
            file.write(t_owner + ", " + t_title + ", " + t_descrip + ", " + t_due_date + ", " + calc_date() + ", No")
        print('-------------------------')
        print(f"Task '{t_title}' saved!")
        print('-------------------------\n')
        

    elif menu == 'va':
        '''This code block will read the tasks from task.txt file and
         show them on the terminal'''
        if check_tasks() == False: #Checks if file is empty or doesn't exist
            print("No tasks stored! Please add a task first\n")

        else:
            with open('tasks.txt', 'r') as f:
                lines = f.readlines()

            for line in lines:
                task = line.split(", ")
                print("__________________________________________________________\n")
                print(f"Task:\t\t\t {task[1]}")
                print(f"Assigned to:\t\t {task[0]}")
                print(f"Date assigned:\t\t {task[4]}")
                print(f"Due date:\t\t {task[3]}")
                print(f"Task complete?:\t\t No")
                print(f"Task description: \n {task[2]}\n")
                print("__________________________________________________________\n")


    elif menu == 'vm':
        '''This code block will read the tasks from task.txt file and
        show the ones assigned to the logged in user on the terminal'''
        if check_tasks() == False:
            print("No tasks stored! Please add a task first\n") #Checks if file is empty or doesn't exist

        else:
            with open('tasks.txt', 'r') as f:
                lines = f.readlines()
       
        t_count = 0

        for line in lines:
            task = line.split(", ")

            if task[0] == logged_user:
                t_count += 1
                print("__________________________________________________________\n")
                print(f"Task:\t\t\t {task[1]}")
                print(f"Assigned to:\t\t {task[0]}")
                print(f"Date assigned:\t\t {task[4]}")
                print(f"Due date:\t\t {task[3]}")
                print(f"Task complete?:\t\t No")
                print(f"Task description: \n {task[2]}\n")
                print("__________________________________________________________\n")

        if t_count == 0:
            print(f"No tasks assigned to {logged_user}!\n")

    elif menu == 'st':
        names, passwords = read_users_file()

        with open('tasks.txt', 'r+') as f:
            lines = f.readlines()
        print('------------------------------------')
        print('System statistics:')
        print('------------------------------------')
        print('\t Users \t Tasks')
        print(f'Total \t {len(names)} \t {len(lines)}')
        print('------------------------------------\n')

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made entered an invalid input. Please try again")