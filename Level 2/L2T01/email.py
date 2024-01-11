### --- OOP Email Simulator --- ###

# --- Email Class --- #
class Email():
# Create the class, constructor and methods to create a new Email object.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Declare the class variable, with default value, for emails. 
    has_been_read = False 
    is_spam = False

    # Initialise the instance variables for emails.
    
 
    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        if self.has_been_read == False:
            self.has_been_read = True

        return(self.has_been_read)


    def mark_as_unread(self):
        '''Marks an email as unread'''
        if self.has_been_read == True:
            self.has_been_read = False

        return(self.has_been_read)
    

    def mark_as_spam(self):
        if self.is_spam == False:
            self.is_spam = True

        return(self.is_spam)
    

# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []


# --- Functions --- #
# Build out the required functions for your program.
def populate_inbox(new_email):
    # Create 3 sample emails and add it to the Inbox list. 
    inbox.append(new_email)


def list_emails():
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    print(num, inbox[num].subject_line)


def read_email(obj):
    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    print("\nEmail")

    print("===================================")
    print(f"From: {inbox[obj].email_address}")  
    print(f"Subject: {inbox[obj].subject_line}")
    print("-----------------------------------------------------------------------------------")
    print("U ==> Mark as unread | D ==> Delete email | S ==> Mark as Spam | E ==> Back to menu")
    print("===================================================================================\n")

    print(inbox[obj].email_content)
    print("\n-----------------------------------")

    inbox[obj].mark_as_read()
    email_options(obj)


def email_options(obj):
    '''User actions for email'''
    option = True

    while option == True:
        user_option = str(input("\nChoose an email action: ").lower())

        if user_option == 'u':
            # marks the email as unread
            inbox[obj].mark_as_unread()
            print(f"Email from '{inbox[obj].email_address}' with subject '{inbox[obj].subject_line}' marked as UNREAD.")
            option = False

        elif user_option == 'd':
            # deletes the email after user confirmation
            confirm = str(input("Are you sure you want to delete the email? [Y/N]: ").lower())

            if confirm == 'y':
                print(f"Email from '{inbox[obj].email_address}' with subject '{inbox[obj].subject_line}' DELETED.")
                inbox.pop(obj) # deleted the email
                option = False

        elif user_option == 's':
            # mark the email as spam
            inbox[obj].mark_as_spam()
            print(f"Email from '{inbox[obj].email_address}' with subject '{inbox[obj].subject_line}' marked as SPAM.")
            option = False
              
        elif user_option == 'e':
            # goes back to main user menu
            break
        
        else:
            print("Wrong option! Please try again.\n")


# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
email_1 = Email("example@email.com", "Welcome to Hyperion Bootcamp", "This is an example of an email 1")
email_2 = Email("example@email.com", "Great work on the bootcamp", "This is an example of an email 2")
email_3 = Email("example@email.com", "Your excellent marks!", "This is an example of an email 3")

populate_inbox(email_1)
populate_inbox(email_2)
populate_inbox(email_3)

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        if len(inbox) == 0: 
            print("No emails in the inbox")

        else: 
            # Display emails in the inbox
            print("\nInbox")
            print("----------------------------------")
            for num, ind in enumerate(inbox): 
                if inbox[num].is_spam == False: # Displays the list of emails that are not SPAM
                    list_emails()
            print("----------------------------------")

        selection_ok = False

        while selection_ok == False:
            email_num = int(input("Please select the email you want to read: "))
            
            if email_num < 0 or email_num >= len(inbox): # Shows error if user selects an email not listed.
                print("Error! Email number not listed\n")

            elif inbox[email_num].is_spam == True: # Shows error if user selects an email marked as spam. 
                print("Error! Email number not in the list\n")
            
            else:
                read_email(email_num)
                selection_ok = True
        
    elif user_choice == 2:
        # add logic here to view unread emails
        if len(inbox) == 0:
            print("\nNo email in your inbox")

        else:
            print("\nUnread emails")
            print("-------------------------")

            for num, ind in enumerate(inbox):
                if inbox[num].has_been_read == False:
                    list_emails()

            print("-------------------------")
               
    elif user_choice == 3:
        # add logic here to quit appplication
        print("Good bye")
        break

    else:
        print("Oops - incorrect input.")

