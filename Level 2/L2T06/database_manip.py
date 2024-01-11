# ==== Program to manipulate tables in database ===

import sqlite3
db = sqlite3.connect('data/exercise_db')
cursor = db.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS python_programming(id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)
''')

db.commit()

# Insert all table records
cursor = db.cursor()
student_grades = [(55, 'Carl Davis', 61),(66, 'Dennis Fredrickson', 88), (77, 'Jane Richards', 78), 
                  (12, 'Peyton Sawyer', 45), (2, 'Lucas Brooke', 99)]

cursor.executemany('''INSERT OR IGNORE INTO python_programming(id, name, grade) VALUES(?,?,?)''',student_grades)
'''I had to add the "OR IGNORE" here because when executing the program a 2nd time, 
I was getting an error: sqlite3, IntegrityError: UNIQUE constraint failed when inserting a value.
I understand this is because I was trying to add values to the table that already existed.
reference: https://stackoverflow.com/questions/36518628/sqlite3-integrityerror-unique-constraint-failed-when-inserting-a-value'''

db.commit()

# Select specific records
print("\nRecords with a grade between 60 and 80:")
cursor.execute('''SELECT id, name, grade FROM python_programming WHERE grade >= 60 AND grade <= 80''')
record = cursor.fetchall()

for row in record:
    print('Id: {0} - {1}, grade {2}'.format(row[0], row[1], row[2]))

db.commit()

# Change record
id = 55
grade = 65
cursor.execute('''UPDATE python_programming SET grade = ? WHERE id = ? ''', (grade, id))
print('\nCarl Davis grade changed to %d' %grade)

db.commit()

# Delete record
id = 66
name = 'Dennis Fredrickson'
cursor.execute('''DELETE FROM python_programming WHERE id = ? ''', (id,)) 
print('%s deleted' %name)

db.commit()

# Change records 
grade = 0
cursor.execute('''UPDATE python_programming SET grade = ? WHERE id < 55''', (grade,))
print('Grades for ids < 55 updated to %d ' %grade)

db.commit()
db.close()



