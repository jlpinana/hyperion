# ===== Level 3 - Capstone Project ====
# ===== Budget Tracking App ====
# ===== v1.0 ====== 

# === DESCRIPTION: ===
# Program to manage finances. 
# Through a GUI menu the user can add incomes, expenses, 
# cateogies, budgets, and finance goals. ***

# === NOTES: ===
# User interface created using TKINTER

# === REFERENCES ===
# Tkinter guide: https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/
# Python GUI with Tkinter Playlist: https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d
# Create messages in Tkinter: https://www.tutorialspoint.com/how-to-create-a-tkinter-error-message-box
# Create messages in Tkinter: https://www.geeksforgeeks.org/python-tkinter-messagebox-widget/
# How to create menu buttons: https://www.pythontutorial.net/tkinter/tkinter-menubutton/
# How to create text lists in Tkinter: https://www.tutorialspoint.com/printing-a-list-to-a-tkinter-text-widget
# 1. How to create pie charts in Tkinter: https://www.aimosta.com/Blogt/blogt-1.html (Used as foundation and ChatGPT consulted to polish the output and fix some issues with displaying data).
# 2. How to create pie charts in Tkinter: Above used as foundation and ChatGPT consulted to polish the output and fix some issues with displaying data.


# Import libraries
import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import math


class Category():
    def __init__(self, id, type, name):
        '''Initialise class Category.'''

        self.id = id
        self.type = type
        self.name = name


    def add_category(self): 
        '''Method to add categories into the database.'''

        cursor = db.cursor()
        cursor.execute('''INSERT OR IGNORE INTO categories(id, type, name) VALUES(?,?,?)''',(self.id, self.type, self.name))
        db.commit()
        messagebox.showinfo('Success!', 'Category added succesfully!') # Tkinter message

    def delete_category(self):
        '''Method to delete categories from the database.'''

        cursor = db.cursor()
        cursor.execute('''DELETE FROM categories WHERE type = ? AND name = ? ''', (self.type, self.name))
        db.commit()
        messagebox.showinfo('Success!', 'Category deleted succesfully!')
    

class Expense():
    def __init__(self, id, description, value, category):
        '''Initialise class Expense.'''

        self.id = id
        self.description = description
        self.value = value
        self.category = category


    def add_expense(self):
        '''Method to add expenses into the database.'''

        cursor = db.cursor()
        cursor.execute('''INSERT OR IGNORE INTO expenses(id, description, value, category) VALUES(?,?,?,?)''',(self.id, self.description, self.value, self.category))
        db.commit()
        messagebox.showinfo('Success!', 'Expense added succesfully!')


class Income():
    def __init__(self, id, description, value, category):
        '''Initialise class Income.'''

        self.id = id
        self.description = description
        self.value = value
        self.category = category


    def add_income(self):
        '''Method to add income into the database.'''

        cursor = db.cursor()
        cursor.execute('''INSERT OR IGNORE INTO income(id, description, value, category) VALUES(?,?,?,?)''',(self.id, self.description, self.value, self.category))
        db.commit()
        messagebox.showinfo('Success!', 'Income added succesfully!')


class Budget():
    def __init__(self, id, category, value):
        '''Initialise class budget.'''

        self.id = id
        self.category = category
        self.value = value
        

    def set_budget(self):
        '''Method to add a budget into the database.'''

        cursor = db.cursor()
        cursor.execute('''INSERT OR IGNORE INTO budget(id, category, value) VALUES(?,?,?)''',(self.id, self.category, self.value))
        db.commit()
        messagebox.showinfo('Success!', 'Budget added succesfully!')


class Goal():
    def __init__(self, id, description, selected):
        '''Initialise class Goal.'''

        self.id = id
        self.description = description
        self.selected = selected


    def set_selected_goal(self):
        '''Method to updated current selected goal into database.'''

        # Variable 'selected' is used as a Boolean [0: Goal not selected / 1: Goal selected]
        cursor = db.cursor()
        cursor.execute('''UPDATE goals SET selected = ?''', (0,)) # Sets all goals to '0'.
        cursor.execute('''UPDATE goals SET selected = 1 WHERE description = ?''', (self.description,)) # Set selected goal to 1.
        
        
def retrieve_goals():
    '''Function to retrieve all goals available.'''

    cursor = db.cursor()
    cursor.execute('''SELECT description FROM goals''')
    goals = cursor.fetchall()

    return(goals)

def read_selected_goal():
    '''Function to retrieve the goal currently selected by the user.'''

    value = 1
    cursor = db.cursor()
    cursor.execute('''SELECT id, description FROM goals WHERE selected = ?''', (value,))
    sel = cursor.fetchone()

    return(sel)


def retrieve_expense_or_income(option):
    '''Function to display all expenses or incomes available in db.'''
    cursor = db.cursor()

    if option == 1:
        cursor.execute('''SELECT id, description, value, category FROM expenses''')

    elif option == 2:
        cursor.execute('''SELECT id, description, value, category FROM income''')

    record = cursor.fetchall()

    return(record)


def list_categories(n):
    '''Retrieve all categories available'''

    cursor.execute('''SELECT id, type, name  FROM categories''')
    current_categories = cursor.fetchall()
    cats = []

    # List categories specific for expenses
    if n == 1: 
        for row in current_categories:
            if row[1] == 'Expenses':
                cats.append(row[2]) # Save categories in table to show to user 

    # List categories specific for income
    elif n == 2: 
        for row in current_categories:
            if row[1] == 'Income':
                cats.append(row[2]) 

    return(cats)


def add_category_menu():
    '''Function to show menu to add expesnes or income categories.'''

    global rad_var

    def submit_category():
        '''Sub-function to retrieve values selected by user, contruct class and submit to db.'''

        category_name = name.get() # Name selected
        category_type = rad_var.get() # Type selected
      
        if category_name == '' or category_type =='': # Display a warning if the user hasn't selected anything.
            messagebox.showwarning('Warning', 'Some fields are empty. Please try again!')

        else:            
            new_category = Category(None, category_type, category_name) # Construct object
            new_category.add_category() # Submit to db
            window_cats.destroy() # Close window. Reference: https://www.geeksforgeeks.org/how-to-close-a-tkinter-window-with-a-button/

    # Create menu window
    window_cats = Tk()
    window_cats.title("Add")
    window_cats.geometry("500x300")
    window_cats.maxsize(500, 300)
    window_cats.config(bg="lightgrey")

    label = Label(window_cats, text="Add Category")
    label.grid(row=0)

    # Add area for user to add category name
    Label(window_cats, text="Category name", bg="lightgrey").grid(row=2, column=1, padx=5, pady=5, sticky=E)
    name = Entry(window_cats, bd=3) # User input
    name.grid(row=2, column=2, padx=5, pady=5)

    rad_var = StringVar(window_cats, value="Expenses") # Default selected value for the radiobutton

    def update_rad_var():
        ''' Sub-function to set the value selected by the user in the radiobutton.'''
        
        # I had some issues with the variables in the radiobuttons hence the reason I created this sub-function.
        if rad_var.get() == "Expenses":
            rad_var.set("Expenses")
        else:
            rad_var.set("Income")

    # Display radiobutton
    Radiobutton(window_cats, text="Expenses",  variable = rad_var, value = "Expenses", command=update_rad_var).grid(row = 3, column = 1, sticky=W)
    Radiobutton(window_cats, text="Income  ", variable = rad_var, value = "Income", command=update_rad_var).grid(row = 4, column = 1, sticky=W)

    # Display other screen buttons
    submit_button = Button(window_cats, text="Submit", command=submit_category)
    submit_button.grid(row=6, column=2, sticky=W)

    cancel_button = Button(window_cats, text="Cancel", command=window_cats.destroy)
    cancel_button.grid(row=6, column=3)

    window_cats.mainloop() # Keeps the window in the screen continuosly until user closes it or until destroy function is called.


def delete_category_menu(select):
    '''Function to show delete categories menu'''

    # Create window
    window_cats1 = Tk()
    window_cats1.title("Delete")
    window_cats1.geometry("500x300")
    window_cats1.maxsize(500, 300)
    window_cats1.config(bg="lightgrey")

    del_cat = StringVar(window_cats1, value="Groceries") # Default value for the radiobutton

    def confirm_delete():
        '''Sub-function to request user confirmation before deleting a category'''

        option = messagebox.askyesno('Confirm', 'Are you sure you want to delete it?')

        if option: # User selects YES
            selected_cat_name = del_cat.get()

            if select == 1: # Expense
                category_to_delete = Category(None, "Expenses", selected_cat_name) 

            elif select == 2: # Income
                category_to_delete = Category(None, "Income", selected_cat_name)

            category_to_delete.delete_category() # Delete the category selected
            window_cats1.destroy() # Close the window

    def update_del_cat_value(selected_value):
        '''Sub-function to set in a variable the radiobutton selected by user.'''

        del_cat.set(selected_value)

    # Window labels
    label = Label(window_cats1, text="Delete Category")
    label.grid(row=0)

    Label(window_cats1, text="Select Category to delete:", bg="lightgrey").grid(row=2, column=1, padx=5, pady=5)

    # Display label and retrieves categories specific to expenses
    if select == 1: # Expenses
        Label(window_cats1, text="Expenses:", bg="lightgrey").grid(row=3, column=2, padx=5, pady=5)
        categories = list_categories(1) # Categories specific for expenses

    # Displays label and retrieves categories specific to income
    elif select == 2: # Income
        Label(window_cats1, text="Income:", bg="lightgrey").grid(row=3, column=2, padx=5, pady=5)
        categories = list_categories(2) # Categories specific for income

    # Displays radiobutton with the categories selected
    # I required some assistance here from ChatGPT to work out how to populate a radiobutton from a list of options. The index variable is used for that.
    for index, cat in enumerate(categories):
        Radiobutton(window_cats1, text=cat, variable=del_cat, value=cat, command=lambda value=cat: update_del_cat_value(value)).grid(row=4+index, column=2, padx=5, pady=5, sticky=W)
  
    # Display buttons
    submit_button = Button(window_cats1, text="Delete", command=confirm_delete)
    submit_button.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    cancel_button = Button(window_cats1, text="Cancel", command=window_cats1.destroy)
    cancel_button.grid(row=5, column=1, padx=5, pady=5, sticky=W)

    window_cats1.mainloop() # keep window on screen


def add_expense_income_menu(option):
    '''Function to show menu to add expenses or income.'''

    def submit_expense():
        '''Sub-function to retrieve values selected by user, construct object and submit to db.'''

        # Show warning if no input from user
        if description.get() == '' or value.get() == '' or selected_category.get() == '':
            messagebox.showwarning('Warning', 'Some fields are empty. Please try again!')

        else:  
            # Build expense object and submit to db
            if option == 1: 
                new_expense = Expense(None, description.get(), float(value.get()), selected_category.get())
                new_expense.add_expense()

            elif option == 2:
                # Build income object and submit to db
                new_income = Income(None, description.get(), float(value.get()), selected_category.get())
                new_income.add_income()
    
            window.destroy() # Close window

    # Display window
    window = Tk()
    window.title("Add")
    window.geometry("500x300")
    window.maxsize(500, 300)
    window.config(bg="lightgrey")

    # Display labels
    label = Label(window, text="Add")
    label.grid(row=0)

    Label(window, text="Description", bg="lightgrey").grid(row=2, column=1, padx=5, pady=5, sticky=E)
    description = Entry(window, bd=3)
    description.grid(row=2, column=2, padx=5, pady=5)

    Label(window, text="Value £", bg="lightgrey").grid(row=3, column=1, padx=5, pady=5, sticky=E)
    value = Entry(window, bd=3)
    value.grid(row=3, column=2, padx=5, pady=5)

    # Create dropdown menu for categories
    global selected_category
    selected_category = StringVar(window)

    category = Menubutton(window, text="Category", indicatoron=1)
    category.grid(row=4, column=1, padx=5, pady=5, sticky=E)
    category.menu = Menu(category, tearoff=0)
    category["menu"] = category.menu

    # Retrieve categories available for expenses
    if option == 1:
        categories = list_categories(1) # Categories for expenses

    else: 
        # Retrieve categories for income
        categories = list_categories(2) # Categories for income

    # Display button for dropdown
    for cat in categories:
        category.menu.add_radiobutton(label=cat, variable=selected_category, value=cat)

    # Display other buttons
    submit_button = Button(window, text="Submit", command=submit_expense)
    submit_button.grid(row=6, column=2, sticky=W)

    cancel_button = Button(window, text="Cancel", command=window.destroy)
    cancel_button.grid(row=6, column=3)

    window.mainloop() # Keep window on screen

def view_expense_income_menu(value):
    '''Function to show view expenses or income menu.'''

    # Create window
    window = Tk()
    window.title("View")
    window.geometry("500x300")
    window.maxsize(500, 300)
    window.config(bg="lightgrey")

    # Show label
    label = Label(window, text="View", padx=5, pady=5)
    label.grid(row=0, column=1)

    record = retrieve_expense_or_income(value) # Get data from db

    total = 0.0
    for row in record: # Calculate total of all expenses or income.
        total += row[2]

    # Display totals on screen
    if value == 1: # Expenses
        label = Label(window, text=f"The total of all your expenses is: £{total}", padx=5, pady=5)

    elif value == 2:
        label = Label(window, text=f"The total of all your income is: £{total}", padx=5, pady=5)

    label.grid(row=2, column=1)

    # Display a text window list with all expenses or income
    txt_output = Text(window, wrap="word", height=20, width=50)
    txt_output.grid(row=3, column=1, padx=5, pady=5)

    txt_output.insert(END, "Description \t Value \t Category\n")
    for item in record:
        txt_output.insert(END, f"{item[1]} \t £{item[2]} \t {item[3]}\n") # List items

    window.mainloop() # Keep window on screen

def expenses_income_by_category(query):
    '''Function to retrieve from db the sum of each category.'''

    # I needes some help to figure out how to sum all values of a column grouped by category.
    # Reference: https://www.sqlitetutorial.net/sqlite-sum/
    if query == 1: # Expenses
        cursor.execute('''SELECT category, SUM(value) FROM expenses GROUP BY category''')
        data = cursor.fetchall()

    elif query == 2: # Income
        cursor.execute('''SELECT category, SUM(value) FROM income GROUP BY category''')
        data = cursor.fetchall()

    elif query == 3: # Budget
        cursor.execute('''SELECT category, SUM(value) FROM budget GROUP BY category''')
        data = cursor.fetchall()

    return data

def random_color():
    '''Function to generate a random color in hexadecimal format. This is used to build the pie charts.'''
    
    # Reference: https://stackoverflow.com/questions/13998901/generating-a-random-hex-color-in-python
    r = lambda: random.randint(0, 255)
    return '#{:02x}{:02x}{:02x}'.format(r(), r(), r())


def menu_exp_inc_by_category(sel):
    '''Function to display pie chart window to show expenses or income by category.'''

    # Buils window
    window_catb = Tk()
    window_catb.title("Pie Chart")
    window_catb.geometry("520x520+300+200")
    window_catb.config(bg="lightgrey")

    # Add label
    label = Label(window_catb, text="View by Category", padx=5, pady=5)
    label.grid(row=0, column=1)

    # Create a canvas to display pie chart
    canvas = Canvas(window_catb, width=600, height=600)
    canvas.place(x=50, y=50)

    def create_pie_chart(data):
        '''Sub-function to create pie chart.'''

        total = sum(entry[1] for entry in data) # Calculates total for chart values
        start_angle = 0

        # Draw pie slices and labels
        for category, value in data:
            percentage = (value / total) * 360
            canvas.create_arc(50, 50, 390, 390, start=start_angle, extent=percentage, fill=random_color())

            # Calculate position for category label
            angle = math.radians(start_angle + percentage / 2)
            x = 250 + math.cos(angle) * 200
            y = 250 + math.sin(angle) * 200

            # Draw category label
            canvas.create_text(x, y, text=category, font=("Helvetica", 10), anchor="center")

            # Calculate position for total expenses or income label
            total_angle = math.radians(start_angle + percentage / 2)
            total_x = 250 + math.cos(total_angle) * 150
            total_y = 250 + math.sin(total_angle) * 200

            # Draw total expenses label
            canvas.create_text(total_x, total_y, text=f"£{value}", font=("Helvetica", 8), anchor="center")

            start_angle += percentage

        # Add axis titles
        if sel == 1: # Expenses
            canvas.create_text(250, 20, text="Expenses by Category", font=("Helvetica", 16, "bold"), anchor="center")
    
        elif sel ==2: # Income
            canvas.create_text(250, 20, text="Income by Category", font=("Helvetica", 16, "bold"), anchor="center")

    if sel == 1:
        data = expenses_income_by_category(1) # Retrieves the sum of each category of expenses

    elif sel == 2:
        data = expenses_income_by_category(2) # Retrieves the sum of each category of income

    create_pie_chart(data) 
       
    window_catb.mainloop() # Keep window on screen


def budget_menu():
    '''Function to display menu to view/set budget.'''

    def submit_budget():
        '''Sub-function to create a budget object and submit it to db.'''

        # Show warning if nothing selected
        if selected_category.get() == ''or value.get() == '':
            messagebox.showwarning('Warning', 'Some fields are empty. Please try again!')

        else:   
            new_budget = Budget(None, selected_category.get(), float(value.get())) # Build object
            new_budget.set_budget() # Submit to db

    # Display budget menu window       
    window_b = Tk()
    window_b.title("Budget")
    window_b.geometry("600x500")
    window_b.maxsize(600, 500)
    window_b.config(bg="lightgrey")

    # Display window title
    label = Label(window_b, text="View/Set Budget", padx=5, pady=5)
    label.grid(row=0, column=1)

    # Calculate total income
    record = expenses_income_by_category(2)
    total_income = sum(entry[1] for entry in record)

    # Display total income
    label = Label(window_b, text=f"Total income\n (What you earn)\n £{total_income}")
    label.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    # Calculate total spend
    record_1 = expenses_income_by_category(1)
    total_spend = sum(entry[1] for entry in record_1)

    # Display total spend
    label = Label(window_b, text=f"Total expenses\n (What you spend)\n £{total_spend}")
    label.grid(row=2, column=2, padx=5, pady=5, sticky=W)

    # Calculate total budget
    record_2 = expenses_income_by_category(3)
    budget = sum(entry[1] for entry in record_2)

    # Display total budget
    label = Label(window_b, text=f"Total budget\n\n £{budget}")
    label.grid(row=2, column=3, padx=5, pady=5, sticky=W)

    # Show a column with all budget categories
    txt_output = Text(window_b, wrap="word", height=20, width=15)
    txt_output.grid(row=4, column=1, padx=5, pady=5)

    txt_output.insert(END, "Category\n\n")
    for item in record_1:
        txt_output.insert(END, f"{item[0]}\n")

    # Show a column with all expenses
    txt_output = Text(window_b, wrap="word", height=20, width=15)
    txt_output.grid(row=4, column=2, padx=2, pady=5)

    txt_output.insert(END, "Spend\n\n")
    for item in record_1:
        txt_output.insert(END, f"{item[1]}\n")

    # Show a column with all budgets
    txt_output = Text(window_b, wrap="word", height=20, width=15)
    txt_output.grid(row=4, column=3, padx=2, pady=5)

    txt_output.insert(END, "Budget\n\n")
    for item in record_2:
        txt_output.insert(END, f"{item[1]}\n")

    # Display commands to set new budget 
    Label(window_b, text="Set budget", bg="lightgrey").grid(row=1, column=8, padx=5, pady=5, sticky=S)

    Label(window_b, text="Value £", bg="lightgrey").grid(row=2, column=7, padx=5, pady=5, sticky=N)
    value = Entry(window_b, bd=3)
    value.grid(row=2, column=8, padx=5, pady=5, sticky=N)

    global selected_category
    selected_category = StringVar(window_b)

    # Display expense categories to select
    category = Menubutton(window_b, text="Category", indicatoron=1)
    category.grid(row=3, column=8, padx=5, pady=5, sticky=E)
    category.menu = Menu(category, tearoff=0)
    category["menu"] = category.menu

    categories = list_categories(1) # Categories for expenses

    for cat in categories:
        category.menu.add_radiobutton(label=cat, variable=selected_category, value=cat)

    # Display set budget and cancel buttons
    submit_button = Button(window_b, text="Set Budget", command=submit_budget)
    submit_button.grid(row=3, column=7, sticky=E)

    cancel_button = Button(window_b, text="Cancel", command=window_b.destroy)
    cancel_button.grid(row=3, column=8, sticky=W)

    window_b.mainloop() # Keep window on screen


def goals_menu():
    '''Function to display goals menu window'''

    def select_goal():
        '''Sub-function to select the goal selected by user, construct object and save in db.'''
        
        selected_goal = set_goal.get() # Get user input
      
        if selected_goal == '': # Show warning if nothing selected
            messagebox.showwarning('Warning', 'Some fields are empty. Please try again!')

        else:
            goal_set = Goal(None, selected_goal, 1) # Construct object
            goal_set.set_selected_goal() # Add to db

            messagebox.showinfo('Success!', 'Goal set succesfully!')
            win_goal.destroy() # Close window


    # Display goals menu window       
    win_goal = Tk()
    win_goal.title("Goals")
    win_goal.geometry("500x300")
    win_goal.maxsize(500, 300)
    win_goal.config(bg="lightgrey")

    # Display commands to select goal 
    Label(win_goal, text="Set your financial goal", bg="lightgrey").grid(row=1, column=1, padx=5, pady=5, sticky=W)

    set_goal = StringVar(win_goal, value="No specific goal") # Initialise radiobutton with default value.
    
    def update_set_goal_value(selected_value):
        '''Sub-function to update the value of the variable inside the radiobutton.'''

        set_goal.set(selected_value)

    goals = retrieve_goals() # Get all goals stored in db

    # Display radiobutton with goals
    for index, goal in enumerate(goals):
        Radiobutton(win_goal, text=goal[0], variable=set_goal, value=goal[0], command=lambda value=goal[0]: update_set_goal_value(value)).grid(row=4+index, column=1, padx=5, pady=5, sticky=W)

    # Display set goal and cancel buttons
    submit_button = Button(win_goal, text="Set Goal", command=select_goal)
    submit_button.grid(row=1, column=8, sticky=E)

    cancel_button = Button(win_goal, text="Cancel", command=win_goal.destroy)
    cancel_button.grid(row=1, column=9, sticky=W)

    win_goal.mainloop() # keep window on screen
   

def goals_progress_menu():
    '''Function to show finance progress menu.'''

    # Display menu window       
    win_prog = Tk()
    win_prog.title("Progress")
    win_prog.geometry("500x400")
    win_prog.maxsize(500, 300)
    win_prog.config(bg="lightgrey")

    Label(win_prog, text="Your current goal is:", bg="lightgrey").grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky=NSEW)

    # Display current goal selected by user.
    goal = read_selected_goal()
    Label(win_prog, text=goal[1], bg="lightgrey").grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky=NSEW)

    # Calculate total spend
    record_1 = expenses_income_by_category(1)
    total_spend = sum(entry[1] for entry in record_1)

    # Calculate total budget
    record_2 = expenses_income_by_category(3)
    budget = sum(entry[1] for entry in record_2)

    # Display total spend
    label = Label(win_prog, text=f"Total expenses\n (What you spend)\n £{total_spend}")
    label.grid(row=2, column=0, columnspan=1, padx=5, pady=5, sticky=E)

    # Display total budget
    label = Label(win_prog, text=f"Total budget\n\n £{budget}")
    label.grid(row=2, column=2, columnspan=1, padx=5, pady=5, sticky=W)


    if goal[0] == 2: # Spend less than total budget
        if total_spend <= (budget):
            label = Label(win_prog, text="Your total spend is less than your budget.\n You are on track to achieve your goal of spending less than the total budget.")
            label.grid(row=3, column=0, columnspan=3, rowspan=2, padx=5, pady=5, sticky=NSEW)

        else:
            label = Label(win_prog, text="Your total spend is above your budget.\n You are not on track to achieve your goal and spend less than you total budget.")
            label.grid(row=3, column=0, columnspan=3, rowspan=2, padx=5, pady=5, sticky=NSEW)

    if goal[0] == 3: # Save at least 10% of total budget
        
        if total_spend <= (budget*0.9):
            label = Label(win_prog, text="Your total spend is less than 90%' of your budget.\n You are on track to achieve your goal and save 10''%'' of your total budget.")
            label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        else:
            label = Label(win_prog, text="Your total spend is above 90%' of your budget.\n You are not on track to achieve your goal and save 10''%'' of you total budget.")
            label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

    if goal[0] == 4: # Save at least 20% of total budget
        
        if total_spend <= (budget*0.8):
            label = Label(win_prog, text="Your total spend is less than 80%' of your budget.\n You are on track to achieve your goal and save 20%' of your total budget.")
            label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        else:
            label = Label(win_prog, text="Your total spend is above 80%' of your budget.\n You are not on track to achieve your goal and save 20%' of you total budget.")
            label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
           


# ==== PROGRAM STARTS HERE ==== #
         
db = sqlite3.connect('data/budget_tracker')

cursor = db.cursor()

# Table for categories
cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories(id INTEGER PRIMARY KEY, type TEXT, name TEXT)
''')

# Table for expenses
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses(id INTEGER PRIMARY KEY, description TEXT, value REAL, category TEXT)
''')

# Table for income
cursor.execute('''
    CREATE TABLE IF NOT EXISTS income(id INTEGER PRIMARY KEY, description TEXT, value REAL, category TEXT)
''')

# Table for goals
cursor.execute('''
    CREATE TABLE IF NOT EXISTS goals(id INTEGER PRIMARY KEY, description TEXT, selected INTEGER)
''')

# Table for budget
cursor.execute('''
    CREATE TABLE IF NOT EXISTS budget(id INTEGER PRIMARY KEY, category TEXT, value REAL)
''')

db.commit()


# Popultate database tables with some default values
cursor = db.cursor()
default_categories = [(1, 'Expenses', 'Groceries'), (2, 'Income', 'Salary')]
default_goals = [(1, 'No specific goal', 1), (2, 'Spend less than total budget', 0), (3, 'Save min 10''%'' of total budget', 0), (4, 'Save min 20''%'' of total budget', 0)]

cursor.executemany('''INSERT OR IGNORE INTO categories(id, type, name) VALUES(?,?,?)''', (default_categories))
cursor.executemany('''INSERT OR IGNORE INTO goals(id, description, selected) VALUES(?,?,?)''', (default_goals))

db.commit()


# *** MAIN GUI WINDOW ***

# Create main GUI window for UI Menu
root = Tk()
root.title("Budget Tracker")
root.geometry("1000x400")
main_label = Label(root, text="Budget Tracker App V1.0")
main_label.grid(row=0, column=5, padx=5, pady=5)

# Horizontal separator
# source: https://stackoverflow.com/questions/17013890/tkinter-ttk-separator-wont-display
ttk.Separator(root, orient='horizontal').grid(row=1, pady=5, columnspan=12, sticky=EW)

# *** EXPENSES SECTION ***
expenses_menu_label = Label(root, text="EXPENSES MENU")
expenses_menu_label.grid(row=2, column=1, columnspan=1, padx=5, pady=5)

# Vertical separator
ttk.Separator(root, orient=VERTICAL).grid(column=1, row=3, pady=20, rowspan=4, sticky=NS)


# Create buttons and labels for the expenses categories section
cats_label = Label(root, text="Categories")
cats_label.grid(row=3, column=0, columnspan=1,sticky=NSEW)
Button(root,text="Add Category", command=add_category_menu).grid(row=4, column=0, columnspan=1, padx=20, pady=5, sticky=NSEW)
Button(root, text="Delete Category", command=lambda value=1: delete_category_menu(value)).grid(row=5, column=0, padx=20, pady=5, sticky=NSEW)

# Create buttons and labels for the expenses section
expense_label = Label(root, text="Expenses")
expense_label.grid(row=3, column=3, columnspan=2, sticky=NSEW)
Button(root,text="Add Expense", command=lambda value=1: add_expense_income_menu(value)).grid(row=4, column=3, columnspan=1, padx=5, pady=5, sticky=W)
Button(root, text="View Expenses", command=lambda value=1: view_expense_income_menu(value)).grid(row=4, column=4, columnspan=1, padx=5, pady=5, sticky=E)
Button(root, text="View Expenses by Category", command=lambda value=1: menu_exp_inc_by_category(value)).grid(row=5, column=3, columnspan=2, padx=5, pady=5, sticky=NSEW)
# Vertical separator
ttk.Separator(root, orient=VERTICAL).grid(column=5, row=1, pady=20, rowspan=16, sticky=NS)

# *** INCOME SECTION ***
income_menu_label = Label(root, text="INCOME MENU")
income_menu_label.grid(row=2, column=7, columnspan=1, padx=5, pady=5)

# Create buttons and labels for the income categories section
cats1_label = Label(root, text="Categories")
cats1_label.grid(row=3, column=6, columnspan=1, sticky=NSEW)
Button(root,text="Add Category", command=add_category_menu).grid(row=4, column=6, columnspan=1, padx=5, pady=5, sticky=NSEW)
Button(root, text="Delete Category", command=lambda value=2: delete_category_menu(value)).grid(row=5, column=6, columnspan=1, padx=5, pady=5, sticky=NSEW)

# Create buttons and labels for the income section
expense_label = Label(root, text="Income")
expense_label.grid(row=3, column=8, columnspan=2, sticky=NSEW)
Button(root,text="Add Income", command=lambda value=2: add_expense_income_menu(value)).grid(row=4, column=8, columnspan=1, padx=5, pady=5, sticky=W)
Button(root, text="View Income", command=lambda value=2: view_expense_income_menu(value)).grid(row=4, column=9, columnspan=1, padx=5, pady=5, sticky=E)
Button(root, text="View Income by Category", command=lambda value=2: menu_exp_inc_by_category(value)).grid(row=5, column=8, columnspan=2, padx=5, pady=5, sticky=NSEW)
# Vertical separator
ttk.Separator(root, orient=VERTICAL).grid(column=7, row=3, pady=20, rowspan=4, sticky=NS)

# Horizontal separator
ttk.Separator(root, orient=HORIZONTAL).grid(row=6, pady=20, columnspan=12, sticky=EW)

# *** BUDGET SECTION ***

# Create title
expenses_menu_label = Label(root, text="BUDGET MENU")
expenses_menu_label.grid(row=7, column=1, padx=5, pady=5)

# Create button
Button(root,text="Set/View Budget", command= budget_menu).grid(row=8, column=1, padx=5, pady=5)

# *** GOALS SECTION ***

# Create title
goals_menu_label = Label(root, text="FINANCIALS MENU")
goals_menu_label.grid(row=7, column=7, columnspan=2, padx=5, pady=5, sticky=NSEW)

# Create buttons
Button(root,text="Set Goals", command= goals_menu).grid(row=8, column=7, columnspan=1, padx=5, pady=5, sticky=NSEW)
Button(root,text="View Progress", command= goals_progress_menu).grid(row=8, column=8, columnspan=1, padx=5, pady=5, sticky=W)

root.mainloop() # Keep window on screen









           

