# Problem Set 1

## Assignment 
For this exercise you will be the database architect for the Uda Country District of Animal Shelters. The shelters need a database for adopting puppies.
<br>
Using SQLAlchemy perform the following queries on your database:
1. Query for all puppies and return the results in ascending alphabetical
order.
2. Query for all puppies that are less than 6 months old organized by the
youngest first.
3. Query all puppies by ascending weight.
4. Query all puppies grouped by the shelter in which they are staying.

## Files
* `puppies.py` - Creates the database
* `puppypopulator.py` - Inserts values into the database
* `queries.py` - Program to query the database


## Requirements
All code was developed on Ubuntu 14.04.2 LTS, Python 2.7 and
[`PostgreSQL 9.3.6`](http://www.postgresql.org/ftp/source/v9.3.6/). In addition
to installing PostgreSQL, you will also need to install the following Python
modules:

* [`sqlalchemy 0.8.4`](https://pypi.python.org/pypi/SQLAlchemy/0.8.4)
* [`dateutil 1.4.1`](http://labix.org/python-dateutil)

Don't forget to start the [postgres daemon][1].


## Run
To create the database and its tables, run this command:

    python puppypopulator.py

To run the `puppyqueries.py` script, run this command:

    python queries.py

Follow directions outputted.

[1]:http://www.postgresql.org/docs/9.3/static/server-start.html