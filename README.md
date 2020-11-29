# EchoForMe

EchoForMe is a Web Application that reads out the latest news to the user.It is designed especially for visually impaired people to help them by reading out the daily news to them.It is a user-friendly application that can be used by people of all generations.It also supports the additional feature of converting any text to audio.

## Prerequisites :
- [Django](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction)
- [CockroachDB](https://www.cockroachlabs.com/docs/stable/build-a-python-app-with-cockroachdb-django.html)
- Web Scraping
- Python programming language
- Front end development tools

## Setting Up virtual Python3 environment
1.Follow the commands to create a environemnt "env" and activate it
```
$sudo apt-get install python3.7-venv
$python3.7 -m venv env
```

2.Activate the environment using the command below
```
$source env/bin/activate
```
3.Install the required libraries in the virtual environment
```
$pip3 install -r requirements.txt
```
4.To deactivate the environment,use
```
$deactivate
```
## Setting up the project
1.Create a 'django_projects' directory within the same directory as the virtual environment

2.Initialise the directory for git and clone the repository

3.Refer the [cockroachDB integration article](https://www.cockroachlabs.com/docs/stable/build-a-python-app-with-cockroachdb-django.html) to set up the database with the required tables.

4.Activate your virtual python3 environment and start the Django server using the below command
```
$python3 manage.py runserver 
```
5.Follow the URL dispalyed and you will be directed to the website
