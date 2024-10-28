**Personnel Dispatching API**

This is a RESTful API for managing personnel assignments to construction projects. It allows users to create, retrieve, update, and delete personnel assignments for various projects.

**Features**
1) Create a new personnel assignment.
2) Retrieve a list of all assignments or filter assignments by specific project.
3) Retrieve a specific assignment by ID.
4) Update an assignment.
5) Delete an assignment.

**Technology Stack**
Flask - Web framework for Python.
Flask-SQLAlchemy - ORM for database interaction.
SQLite - Database for local data storage.

**Requirements**
Python 3.7 or later
Flask and Flask-SQLAlchemy packages

**Installation**
1) Clone the Repository:

    git clone https://github.com/tabishmomin415/Personnel-Dispatching-API_Task-1.git
    cd Personnel-Dispatching-API_Task-1

2) Set Up Virtual Environment:

    Install Virtual Environment: pip install virtualenv  
    create a virtual environment named env: virtualenv env
    Activate the Virtual Environment: .\env\Scripts\Activate.ps1

3) Install Dependencies:

    pip install -r requirements.txt

4) Create the SQLite Database: The database will be created automatically on the first run.

**Run the Application**
    
    python app.py

**API Endpoints**

1) Create a New Assignment (Post):

    URL: http://127.0.0.1:5000/assignments

    ![Create a new assignment](image1.png)

2) Retrieve All Assignments (Get):
 
    URL: http://127.0.0.1:5000/assignments

    ![Get all the assignment](image2.png)

3) Retrieve Assignments by Project ID:
 
    URL: http://127.0.0.1:5000/assignments/project/102

    ![Get assignment by project Id](image3.png)

4) Retrieve an Assignment by ID:

    URL: http://127.0.0.1:5000/assignments/1

    ![Get assignment by Id](image4.png)

5) Update an Assignment (Put):

    URL: http://127.0.0.1:5000/assignments/1

    ![Update the assignment](image5.png)

6) Delete an Assignment (Delete):

    URL: http://127.0.0.1:5000/assignments/2

    ![Delete an assignment](image6.png)
