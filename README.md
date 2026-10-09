\# Multi-Tier Student Management System



\## 1. Project Overview



The Multi-Tier Student Management System is a web application

that allows users to add student records and view them through

a web interface.



The application uses a frontend, a Python Flask backend, and

an SQLite database.



\## 2. Project Objective



The objective is to understand how frontend, backend APIs,

and a database work together in a web application.



\## 3. Technologies Used



\- HTML

\- CSS

\- JavaScript

\- Python

\- Flask

\- REST API

\- SQLite

\- Git and GitHub



\## 4. Architecture



User Browser

&#x20;    |

&#x20;    v

HTML, CSS, JavaScript Frontend

&#x20;    |

&#x20;    v

Python Flask Backend

&#x20;    |

&#x20;    v

SQLite Database



\## 5. Features



\- View student records

\- Add new student records

\- Retrieve student data using a REST API

\- Store student records in SQLite

\- Display database records on the frontend



\## 6. Project Structure



multi-tier-student-app/

|

|-- backend/

|   |-- app.py

|   |-- database.py

|   |-- students.db

|

|-- frontend/

|   |-- index.html

|

|-- README.md



\## 7. Local Setup



\### Prerequisites



\- Python 3

\- Flask



\### Install Flask



Run:



pip install flask



\### Create the Database



Open a terminal in the backend directory and run:



python database.py



\### Start the Application



Run:



python app.py



Open the following address in a browser:



http://127.0.0.1:5000/



\## 8. API Endpoints



\### GET /students



Returns the student records stored in SQLite.



\### POST /students



Adds a student record.



Example JSON request:



{

&#x20; "name": "Priya",

&#x20; "course": "BCA"

}



\## 9. Current Project Status



The application has been tested locally.



The frontend, Flask backend, and SQLite database are integrated.



AWS deployment has not yet been completed.



\## 10. Future Improvements



\- Update student records

\- Delete student records

\- Add input validation

\- Add student search

\- Deploy using suitable cloud services

