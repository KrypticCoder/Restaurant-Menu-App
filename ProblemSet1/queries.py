# The assignment is to use SQLAlchemy to perform the following queries on 
# your database:
# 1. Query all of the puppies and return the results in ascending 
#    alphabetical order.
# 2. Query all of the puppies that are less than 6 months old organized by 
#    the youngest first.
# 3. Query all puppies by ascending weight.
# 4. Query all puppies grouped by the shelter in which they are staying.

# SqlAlchemy throws a warning which we can ignore for now
import warnings
from sqlalchemy.exc import SAWarning
warnings.filterwarnings('ignore',
 r"^Dialect sqlite\+pysqlite does \*not\* support Decimal objects natively\, "
 "and SQLAlchemy must convert from floating point - rounding errors and other "
 "issues may occur\. Please consider storing Decimal numbers as strings or "
 "integers on this platform for lossless storage\.$")

# Dependencies
import datetime
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import *
from sqlalchemy.sql import *

# Existing db
from puppies import Base, Shelter, Puppy

# Lets program know which db to communicate with
engine = create_engine('sqlite:///puppyshelter.db')

# Connects class connections to tables in db
Base.metadata.bind = engine

# Establishes link of communication b/w code executions and engine
DBSession = sessionmaker(bind = engine)

# Session object
session = DBSession()


def Query1():
    """
    Query the Puppy table and print the puppy names in alphabetical order
    """

    # find all puppies and order them by name
    puppies = session.query(Puppy).order_by(Puppy.name).all()

    for puppy in puppies:
        print puppy.name


def Query2():
    """
    Query the Puppy table for all puppies < 6 months old. Then print the puppy 
    names and dateOfBirth, sorted by youngest first.
    """

    # Calculate today's date
    today = datetime.date.today()

    # Calculate date six months from current
    # http://stackoverflow.com/questions/546321/how-do-i-calculate-the-date-six-months-from-the-current-date-using-the-datetime
    sixmonthsago = today + datetime.timedelta(6*365/12)

    # Find puppies that match given criteria
    puppies = session.query(Puppy).\
                    filter(Puppy.dateOfBirth < sixmonthsago).\
                        order_by(desc(Puppy.dateOfBirth)).all()


    # print name and dateOfBirth of each puppy
    for puppy in puppies:
        print puppy.name, str(puppy.dateOfBirth)

def Query3():
    """
    Query the Puppy table for all names and weights, sorted by ascending weight. 
    """

    puppies = session.query(Puppy).order_by(Puppy.weight).all()

    for puppy in puppies:
        print puppy.name, str(puppy.weight)[:3]


def Query4():
    """
    Query the database for all puppy names and shelter names, printing each 
    shelter name once and indenting puppy names below their respective shelters.
    """

    # Shelter.id is a foreign key for Puppy.shelter_id so we can join the two tables
    # on that attribute and order by the shelter name to get tuples of puppies and 
    # their respective shelter
    tuples = session.query(Puppy, Shelter).\
                filter(Puppy.shelter_id == Shelter.id).\
                        order_by(Shelter.name).all()

    # keep track of the last shelter we came across. Every time we come across a new one, we
    # know that the previous tuples are for the last new shelter we came across
    last_shelter = ''
    
    # Loop through each tuple and print the shelter name only when we come across a new one
    for tup in tuples:
        shelter = str(tup.Shelter.name).strip()
        if shelter != last_shelter:
            print('\n')
            print (shelter)
            last_shelter = shelter
        print('\t' + tup.Puppy.name)

        

    


def main():
    while(True):
        print(""" 
        Please select from the following options: 
            1) Show all puppy names in alphabetical order.

            2) Show all puppies under six months old, youngest to oldest.

            3) Show all puppies by ascending weight.

            4) Show all puppies grouped by their shelters.

            5) Exit.
        """)
        query = raw_input('Select menu item: ')
        print('\n')
        if not query.isdigit():
            if query == 'exit':
                exit()
            else:
                print ('That is an invalid selection')
        else:
            query = int(query)
            if query == 1:
                Query1()
            elif query == 2:
                Query2()
            elif query == 3:
                Query3()
            elif query == 4:
                Query4()
            elif query == 5:
                exit()
            else: 
                print ('Please input a number from 1 - 5')

        

    

   
if __name__ == '__main__':
    main()