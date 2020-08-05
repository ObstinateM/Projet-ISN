# PROJET ISN 2019/2020

Le github du projet ISN 2019/2020 
 
## Use it locally

### #1 Create a Virtual environment :
`python -m venv env`

Activate it with `source env/bin/activate`

### #2 Download requirements.txt w/
`pip install -r requirements.txt`

### #3 Create the Database
Install xampp or whatever else wich support mysql/phpmyadmin
Create a new db named `isn_bdd`
Migrate the db `./manage.py migrate`

### Launch the server
`./manage.py runserver`
Go to localhost/8000

### In case of an error
https://stackoverflow.com/questions/55657752/django-installing-mysqlclient-error-mysqlclient-1-3-13-or-newer-is-required