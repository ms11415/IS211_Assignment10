import sqlite3

connection = sqlite3.connect('pets.db')
cursor = connection.cursor()

print 'Please enter a person ID to retrieve their personal and pet data'
print 'Enter -1 to exit'

cursor.execute('SELECT * from person')
print cursor.fetchall()
cursor.execute('SELECT * from pet')
print cursor.fetchall()
cursor.execute('SELECT * from person_pet')
print cursor.fetchall()

connection.close()