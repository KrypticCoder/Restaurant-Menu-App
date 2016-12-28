# Restaurant Menu App

##Description
This repository contains the code used in the Udacity course Full-Stack Foundations. This code is intended to be a supplement to the course material and runs in the vagrant environment provided in the course

##Why This Project?
Modern web applications perform a variety of functions and provide amazing features and utilities to their users; but deep down, it’s really all just creating, reading, updating and deleting data. In this project, you’ll combine your knowledge of building dynamic websites with persistent data storage to create a web application that provides a compelling service to your users.

##What Will I Learn?
You will learn how to develop a RESTful web application using the Python framework Flask along with implementing third-party OAuth authentication. You will then learn when to properly use the various HTTP methods available to you and how these methods relate to CRUD (create, read, update and delete) operations.

##How Does This Help My Career?
Efficiently interacting with data is the backbone upon which performant web applications are built
Properly implementing authentication mechanisms and appropriately mapping HTTP methods to CRUD operations are core features of a properly secured web application

##Requirements
- [Vagrant](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/)
- [Python ~2.7](https://www.python.org/)


##Set Up
For an initial set up please follow these 2 steps:

1. Download or clone the [fullstack-nanodegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm).

2. Find the *catalog* folder and replace it with the content of this current repository, by either downloading it or cloning it.

##Files
- database_setup.py: initialize database tables and attributes
- database_run.py: Preliminary insertion, update, and deletion of attributes of database
- lotsofmenus.py: Fills up database with Restaurants and MenuItems
- webserver.py: Web server that displays restaurants and allows users to credit, edit, and delete restauarants
- project.py: same idea as webserver.py but built using Flask framework

##Folders
Folders for webserver.py and project.py 
- templates: .html pages that are rendered by webserverapp.py and project.py
- static: holds our css stylesheet for customizing the app

Standalone folders. View contents to see description
- ProblemSet1: Beginning to work with SQLAlchemy and ORM (Object Relational Mapping)
- finalproject: Final project of Restaurant Menu App. 


##Usage

Launch the Vagrant VM from inside the *vagrant* folder with:

`vagrant up`

`vagrant ssh`

Then move inside the catalog folder:

`cd /vagrant/catalog` or `cd ../../vagrant/catalog`

Initialize database:

`python database_setup.py`

Run through preliminary setup to make sure it is working:

`python database_run.py`

Fill up database: 

`python lotsofmenus.py`

Run application:

`python webserver.py` or `python project.py`

After the last command you are able to browse the application at this URL:

`http://localhost:5000/`

It is important you use *localhost* instead of *0.0.0.0* inside the URL address. That will prevent OAuth from failing.
