**Project overview**

&#x09;The Todo Management system is a Web Application Developed using Python, Django REST Framework(DRF).it allows users to create, view, update, and delete todo tasks using a simple Bootstrap5 interface.



**Features**

* create new todo tasks.
* view all todo records in a table.
* update existing tasks.
* Delete tasks.
* Manage task status: Pending, In progress, and Completed.
* Use DRF serializers for data validation and database operations.
* Responsive user interface using Bootstrap 5.3.8.
* CSRF protection for HTML form submissions.
* No JavaScript required.



**software requirements**



operating system: Windows 11

program language: Python

Backend framework: Django

API framework: Django Rest framework

frontend: HTML5,CSS3,BOOTSTRAP 5.3.8

database: MySQL

code editor: VS Code

browser: google chrome





**Technologies Used**

* Python
* Django
* Django REST Framework
* MYSQL
* HTML5
* CSS3
* BOOTSTRAP 5.3.8



**Installation and Setup**



1.create a virtual Environment

python -m venv venv

Activate it on Windows

venv/Scripts/activate



2.install dependencies

pip install Django

pip install djangorestframework

pip install django-bootstrap5

pip install mysqlclient



3.apply database Migrations

python manage.py make migrations

python manage.py migrate



4.Start the Development server

python manage.py runserver



5.open the application

visit:

http://127.0.0.1:8000/



**Database Model**

&#x09;The todo model contains the following fields.

|Field	<br />|Type|Description|
|-|-|-|
|id|<br />Auto field<br />|unique task identifier|
|task|charfield|taskname|
|due\_at|DataTimeField|task due date and time|
|status|charfield|current task status|





**Available Status**



* Pending
* In progress
* Completed



**CRUD OPERATIONS**

|**operation**|**description**|
|-|-|
|create|add a new task|
|read|display all task|
|update|Edit an existing task|
|Delete|Remove a task|





**Application URLS**



|**URL**|**Method**|**Purpose**|
|-|-|-|
|/|GET|Display todo list|
|todo\_add/|POST|create a task|
|todo\_update/[int:id](int:id)/|GET,POST|display and update the task|
|todo\_delete/[int:id](int:id)/|POST|Delete a task|



**Serializer**



The application uses TodoSerializers, which is based on

serializers.ModelSerializer.



The serializer convert model data into API-friendly representations and validates incoming values before saving them.





**Feature Improvements**



* Add user registration and login
* implement session-cookies authentication.
* Create separate REST API endpoint returning JSON.
* Add search and filtering.
* Add pagination.
* Add task completion statistics.



**Learning Objectives**



This project demonstrations:

* Django models and ORM.
* Django URL routing and views.
* Django template and forms.
* DRF serializers and validation.
* CRUD operations.
* Database migrations.
* Bootstrap responsive Design.
* CSRF Protection.



Project overview

The Todo Management system is a Web Application Developed using Python, Django REST Framework(DRF).it allows users to create, view, update, and delete todo tasks using a simple Bootstrap5 interface.

Features
create new todo tasks.
view all todo records in a table.
update existing tasks.
Delete tasks.
Manage task status: Pending, In progress, and Completed.
Use DRF serializers for data validation and database operations.
Responsive user interface using Bootstrap 5.3.8.
CSRF protection for HTML form submissions.
No JavaScript required.

Technologies Used

