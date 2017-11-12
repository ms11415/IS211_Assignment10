#!/usr/env/bin python
# ! -*- coding: utf-8 -*-
"""IS211 Assignment 10, queries and displays pets.db data"""

import sqlite3
import sys

# set connection and cursor as global variables so that all functions can use
connection = sqlite3.connect('pets.db')
# use row factory to access values by column name instead of index
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

def showUser(userid):
    cursor.execute('SELECT * from person where id = ?', userid)
    row = cursor.fetchone()
    print row['first_name'], row['last_name'], 'is', row['age'], 'years old.'

def showPets(userid):
    #join the tables to correlate person and pet data
    cursor.execute('SELECT pp.person_id, person.first_name, person.last_name,'
                   'p.name, p.breed, p.age, p.dead '
                   'FROM person_pet as pp '
                   'INNER JOIN pet as p '
                   'ON pp.pet_id = p.id '
                   'INNER JOIN person '
                   'ON pp.person_id = person.id'
                   )
    for row in cursor.fetchall():
        # must cast userid as int because person_id is int
        if row['person_id'] == int(userid) and row['dead'] == 1:
            print row['first_name'], row['last_name'], 'owned', row['name'] + ',' ,\
                'a', row['breed'] + ',', 'who was', row['age'], 'year(s) old.'
        elif row['person_id'] == int(userid) and row['dead'] == 0:
            print row['first_name'], row['last_name'], "owns", row['name'] + ",",\
                'a', row['breed'] + ',', 'who is', row['age'], 'year(s) old.'

def getUserID():

    userid = raw_input('Please enter a person ID to retrieve their personal and'
                       'pet data.  Enter -1 to exit:   ')
    return userid


def main():
    # initialize userid
    userid = 0
    # while loop to accept and process user input
    while int(userid) != -1:
        userid = getUserID()
        # logic to process user input
        if 1 <= int(userid) <= 4:
            print '-' * 80
            showUser(userid)
            showPets(userid)
            print '-' * 80
        elif int(userid) == -1:
            print '-' * 80
            print 'Program exit. Goodbye.'
            print '-' * 80
            break
        else:
            print '-' * 80
            print 'User does not exist.  Please choose an ID between 1 and 4.'
            print '-' * 80
            continue

    connection.close()
    sys.exit()

if __name__ == '__main__':
    main()