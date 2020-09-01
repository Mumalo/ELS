# ELS (Electronic Learning System)

This project is a basic ELS where students and students can interact for learning purposes.

## Description

Instructors can create courses, create modules and add content for each module
content can be files (uploaded), videos (provided by embedding links), and simple text
Students can browse and enrol for courses. 

## Getting Started

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing

1. Clone the project from github, into a desired source folder
2. Make sure python3 and pip3 are installed on your system 
3. Before installing django and other dependencies, set up virtulenv 
4. create a virtual environment as below
  type python3 -m venv myvenv in the terminal (myvenv is the name of your virtual evnironment)
5. Install requirements from the requirements.txt file by:
   i. Navigating to the directory containing requirements.txt and 
   ii. Type pip3 install -r requirements.txt in the terminal


### Executing program

1. After the above, set up a local mysql db and connect to the app
2. Run migrations against your local db by: 
    typing **python3 manage.py makemigrations** and **python3 manage.py migrate**
3. Finally, run the app by typing python3 manage.py runserver
  PS: Make sure you are in the directory containing manage.py when typing these commands
  
  
[Check app here](https://django-els.herokuapp.com/course/)