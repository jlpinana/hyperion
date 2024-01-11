# ===== Level 2 - Capstone Project ====
# ===== Bookstore Clerk Program ====

import sqlite3

class Book():
    def __init__(self, id, title, author, qty):
        self.id = id
        self.title = title
        self.author = author
        self.qty = qty


    def add_book(self):
        '''Method to add books into the database'''
        cursor = db.cursor()
        cursor.execute('''INSERT OR IGNORE INTO book(id, title, author, qty) VALUES(?,?,?,?)''',(self.id, self.title, self.author, self.qty))
        db.commit()


    def delete_book(self):
        '''Method to delete books from the database'''
        cursor = db.cursor()
        cursor.execute('''DELETE FROM book WHERE id = ? ''', (self.id,))
        db.commit()


def welcome(option):
    '''Displays user welcome message and messages for the menus.'''
    if option == 0:
        print("\n===========================")
        print("+++++++ BOOK STORE ++++++++")
        print("===========================")

    elif option == 1:
        print("\n----------------------------")
        print("====> Menu: Enter book <====")
        print("----------------------------")
        print("")

    elif option == 2:
        print("\n----------------------------")
        print("====> Menu: Update book <====")
        print("-----------------------------")
        print("")

    elif option == 3:
        print("\n------------------------------")
        print("====> Update book details <====")
        print("-------------------------------")
        print("")

    elif option == 4:
        print("\n----------------------------")
        print("====> Menu: Delete Book <====")
        print("-----------------------------")
        print("")

    elif option == 5:
        print("\n----------------------------")
        print("====> Menu: Search Book <====")
        print("-----------------------------")
        print("")


def create_object(row_id):
    '''Creates a Book Object with data entered by user.'''
    data = True
    title = str(input("Add book title: "))
    author = str(input("Add book author: "))

    while data:
        try:
            qty = int(input("Add book stock: "))
            break

        except ValueError:
            print("ERROR - Please enter a number!") # Shows error if input is a string

    new_object = Book(row_id, title, author, qty) # Create object

    return(new_object)


def search_book():
    '''Prints all records matching author/title entered by user.'''
    ids = []
    info_query = str(input("Enter the title or author of a book to start the search:\n"))
    info_query = '%' + info_query + '%' #Add wildcards to be able to search partial words.
    '''I had to do some research on how to run database searches with partial words, so the user does not need
    to add a full book title or author.
    Found some useful information in:
    https://www.sqlitetutorial.net/sqlite-like/'''

    cursor.execute('''SELECT id, title, author, qty FROM book WHERE title LIKE ? OR author LIKE ?''', (info_query, info_query))
    record = cursor.fetchall()

    if record == []: # No books found. Use to give user error message.
        return(-1) 

    else:
        print("\n====> BOOKS FOUND <====") 
        print("-------------------------------------------------------------------------")

        for row in record: # Lists all books found.
            ids.append(row[0])
            print('Id: {0} - Title: {1}, Author: {2}, qty: {3}'.format(row[0], row[1], row[2], row[3]))

        print("-------------------------------------------------------------------------")
        
        return(ids)
  

def id_check(records, id):
    '''Checks if id selected by user is within records found during search'''
    if id in records:
        valid = True

    else:
        print("Wrong id #!")
        valid = False

    return(valid)


# ==== PROGRAM STARTS HERE ==== #
         
db = sqlite3.connect('data/ebookstore')

cursor = db.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, qty INTEGER)
''')

db.commit()

# Popultate databese table with initial stock
cursor = db.cursor()
initial_stock = [(3001, 'A Tale of Two Cities', 'Charles Dickens', 30), (3002, 'Harry Potter and the Philosopher\'s Stone','J.K. Rowling', 40),
    (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25), (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37),
    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)]

cursor.executemany('''INSERT OR IGNORE INTO book(id, title, author, qty) VALUES(?,?,?,?)''', initial_stock)

db.commit()

welcome(0)

while True:
    # Present the menu to the user
    try:
        menu = int(input('''\nPlease select one of the following options:
1 - Enter book
2 - Update book
3 - Delete book
4 - Search books
0 - exit
: '''))
        
        if menu == 1: # Enter book
            welcome(1)

            row = cursor.lastrowid
            new_book = create_object(row)
            new_book.add_book()
            
            print("\n ===> Book succesfully added to the database!")
        

        elif menu == 2: # Update book
            welcome(2)
            found = False

            '''Check that the book exists in the database'''
            while found == False:
                records_found = search_book()

                if records_found == -1:
                    print("No results found! Please try again\n")

                else:
                    break

            valid_id = False

            '''Check that the id selected is within the ones returned from the search'''
            while valid_id == False:
                record_id = int(input("Select the id # of the book you want to update: "))
                valid_id = id_check(records_found, record_id)

            welcome(3)

            book_update = create_object(record_id)
            book_update.add_book()

            print("\n ===> Book succesfully updated!")
                

        elif menu == 3: # Delete book
            welcome(4)
            found = False

            '''Check that the book exists in the database'''
            while found == False:
                records_found = search_book()

                if records_found == -1:
                    print("No results found! Please try again\n")

                else:
                    break

            valid_id = False

            '''Check that the id selected is within the ones returned from the search'''
            while valid_id == False:
                record_id = int(input("Select the id # of the book you want to delete: "))
                valid_id = id_check(records_found, record_id)

            confirm = str(input("Are you sure you want to delete the book? [Y/N]: ")).lower()
            confirmation = False

            while confirmation == False:
                if confirm == 'y':
                    cursor.execute('''SELECT id, title, author, qty FROM book WHERE id = ?''', (record_id,))
                    record = cursor.fetchone()
                    book_delete = Book(record[0], record[1], record[2], record[3])
                    book_delete.delete_book()
                    confirmation = True

                    print("\n ===> Book succesfully deleted!")
            
                elif confirm == 'n':
                    break

                else:
                    print("Wrong option! Please select Y/N")

        elif menu == 4: # Search books
            welcome(5)
            found = False

            while found == False:
                if search_book() == -1:
                    print("No results found! Please try again\n")

                else:
                    break

        
        elif menu == 0: # Exit program
            db.close()
            print('\nGoodbye!!!')
            exit()

        else:
            print("\nYou have made entered an invalid input! Please try again")

    except ValueError:
        print("\nERROR - Please enter a number!") # Shows error if input is a string:
