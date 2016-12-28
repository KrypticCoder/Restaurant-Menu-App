#Final Project

##Description
This is the final version of the Restaurant Menu App. Users can go to the homepage at 'localhost:5000/' and view a list of restaurants 
and menu items by clicking on a particular restaurant. Users can log in through 3rd party oauth system using Facebook or Google.
If a user is logged in, they can create, edit, and delete their own restaurants and menu items. 

## Requirements
- [Vagrant](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/)
- [Python ~2.7](https://www.python.org/)

##Setup
1. Download or clone the [fullstack-nanodegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm).

2. Find the *catalog* folder and replace it with the content of this current repository, by either downloading it or cloning it - [Github Link](https://github.com/iliketomatoes/tournament).

## Usage 
This is the same sequence of steps as before but must be done again.
- Launch Vagrant VM from inside *vagrant* folder: `vagrant up`
- Login to Vagrant: `vagrant ssh`
- Move to catalog folder: `cd /vagrant/catalog`
- Initialize database: `python database_setup.py`
- Fill up database: `python lotsofmenus.py`
- Run project: `python project.py`
- View project: visit `localhost:5000/`

## API Endpoints
|Request | What you get |
|--------------|:-----------:|
| /restaurant | Show all restaurants |
| /restaurant/new | Create new restaurant|
| /restaurant/<int:restaurant_id>/edit | Edit restaurant |
| /restaurant/<int:restaurant_id>/delete | Delete restaurant |
| /restaurant/<int:restaurant_id>/menu/ | Display menu for a restaurant |
| /restaurant/<int:restaurant_id>/menu/new/ | Create new menu item |
| /restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit | Edit menu item |
| /restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit | Delete menu item|
| /login | Login to Facebook or Google |
| /fbconnect | Connect with Facebook |
| /gconnect | Connect with Google |
| /disconnect | Disconnect based on provider |
| /fbdisconnect | Disconnect with Facebook |
| /gdisconnect | Disconnect with Google |
