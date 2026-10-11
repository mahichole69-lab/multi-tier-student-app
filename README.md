# 🎓 Multi-Tier Student Management System

A web-based Student Management System developed using Python Flask, HTML, CSS, JavaScript, and SQLite. This project demonstrates how the frontend, backend, REST APIs, and database work together in a multi-tier web application.

---

## 📌 1. Project Overview

The Multi-Tier Student Management System is a web application designed to manage student records through a simple web interface.

The application allows users to add student records and view existing records. The Flask backend processes requests and communicates with an SQLite database to store and retrieve student information.

This project demonstrates the fundamentals of web development, backend API integration, database management, and multi-tier application architecture.

## 🎯 2. Project Objectives

- Understand multi-tier application architecture.
- Develop a frontend using HTML, CSS, and JavaScript.
- Build backend functionality using Python and Flask.
- Implement REST API endpoints.
- Store and retrieve student records using SQLite.
- Integrate the frontend, backend, and database.
- Practice source code management using Git and GitHub.

## 🛠️ 3. Technologies Used

| Technology | Purpose |
|---|---|
| HTML5 | Web page structure |
| CSS3 | Styling and layout |
| JavaScript | Frontend functionality and API requests |
| Python | Backend programming |
| Flask | Backend web framework |
| REST API | Communication between frontend and backend |
| SQLite | Database for student records |
| Git | Version control |
| GitHub | Source code hosting |

## 🏗️ 4. System Architecture

This project follows a three-tier architecture.

```text
              +----------------------+
              |      User Browser    |
              +----------------------+
                         |
                         v
              +----------------------+
              |  Presentation Tier   |
              |                      |
              | HTML, CSS, JavaScript|
              +----------------------+
                         |
                  HTTP / REST API
                         |
                         v
              +----------------------+
              |  Application Tier    |
              |                      |
              | Python Flask Backend |
              | Request Processing   |
              +----------------------+
                         |
                    SQL Queries
                         |
                         v
              +----------------------+
              |       Data Tier      |
              |                      |
              |   SQLite Database    |
              |    Student Records   |
              +----------------------+
```

### Architecture Workflow

1. The user opens the application in a web browser.
2. The frontend displays the student management interface.
3. JavaScript sends requests to the Flask backend.
4. Flask processes the requests.
5. The backend interacts with the SQLite database.
6. The database returns the requested information or stores a new record.
7. The backend sends a response to the frontend.
8. The frontend displays the student records.

### Architecture Diagram

The project also includes an architecture diagram in PDF format.

**File:** `architecture/Architecture-diagram.pdf`

## ✨ 5. Key Features

- **View Student Records:** Retrieve and display student information.
- **Add Student Records:** Add new student details through the application.
- **REST API Integration:** Exchange data between the frontend and backend.
- **SQLite Database:** Store and retrieve student records.
- **Frontend and Backend Integration:** Connect the user interface with backend functionality.
- **Local Application Execution:** Run and test the application on a local computer.

## 📂 6. Project Structure

```text
multi-tier-student-app/
│
├── backend/
│   ├── app.py
│   ├── database.py
│   └── students.db
│
├── frontend/
│   └── index.html
│
├── architecture/
│   └── Architecture-diagram.pdf
│
└── README.md
```

Note: This structure shows the main project files. Additional CSS, JavaScript, configuration, or dependency files may also exist in the repository.

## ⚙️ 7. Prerequisites

Before running the application, install:

- Python 3
- pip package manager
- A modern web browser

Basic knowledge of Python, HTML, and SQL is helpful.

## 🚀 8. Installation and Setup

### Step 1: Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/mahichole69-lab/multi-tier-student-app.git
```

### Step 2: Open the Project Directory

```bash
cd multi-tier-student-app
```

### Step 3: Install Flask

```bash
pip install flask
```

If a `requirements.txt` file is available, install the project's dependencies with:

```bash
pip install -r requirements.txt
```

### Step 4: Initialize the Database

Navigate to the backend directory:

```bash
cd backend
```

Run the database initialization script:

```bash
python database.py
```

Run this command only when database initialization is required. Check the database script before running it against an existing database.

### Step 5: Start the Application

From the backend directory, run:

```bash
python app.py
```

Wait until the Flask server starts successfully.

### Step 6: Open the Application

Open your web browser and visit:

http://127.0.0.1:5000/

The student management interface should appear if the application starts successfully.

## 🔌 9. REST API Endpoints

The following endpoints describe the intended API functionality. Confirm the actual routes and request format in `backend/app.py`.

### GET /students

**Purpose:** Retrieve student records from the database.

Example response:

```json
[
  {
    "name": "Priya",
    "course": "BCA"
  }
]
```

The response fields depend on the actual database schema and backend implementation.

### POST /students

**Purpose:** Add a new student record.

Example JSON request:

```json
{
  "name": "Priya",
  "course": "BCA"
}
```

The backend processes the request and stores the record if the request is valid and the endpoint supports this format.

## 🗄️ 10. Database Management

The application uses SQLite as its database.

SQLite is a lightweight relational database that stores data in a local database file.

The database layer is responsible for database operations, while Flask handles incoming HTTP requests and sends responses to the frontend.

**Database file:** `backend/students.db`

**Database initialization file:** `backend/database.py`

The actual table names and columns are defined by the project's database implementation.

## 🧪 11. Testing and Verification

The application can be tested locally using these checks:

- Start the Flask application without errors.
- Open the application in a browser.
- Verify that existing student records are displayed.
- Add a new student record.
- Verify that the new record appears in the interface.
- Check that the backend returns appropriate API responses.
- Restart the application and verify that saved records remain available.

Mark these tests as completed only after verifying the application.

## 📊 12. Current Project Status

| Component | Status |
|---|---|
| Frontend development | Implemented |
| Flask backend | Implemented |
| SQLite integration | Implemented |
| Student record operations | Implemented as supported by the application |
| Architecture documentation | Included in the project |
| Local application testing | Reported as completed |
| Git and GitHub | Repository configured |
| AWS deployment | Not yet completed |

## ☁️ 13. Future Enhancements

The project can be extended with the following features:

- Update existing student records.
- Delete student records.
- Add student search and filtering.
- Improve form validation and error handling.
- Add user authentication and authorization.
- Improve the user interface and mobile responsiveness.
- Add automated unit and integration tests.
- Containerize the application using Docker.
- Deploy the application using suitable AWS services.
- Explore a managed database for a future cloud deployment.

## 📚 14. Learning Outcomes

This project provides practical experience with:

- Three-tier application architecture.
- Frontend and backend integration.
- Python Flask application development.
- REST API communication.
- SQLite database operations.
- Git version control.
- GitHub repository management.
- Local application testing.
- Basic cloud deployment concepts.

## 👨‍💻 15. Author

**Mahesh Shivaji Chole**

GitHub Profile: [mahichole69-lab](https://github.com/mahichole69-lab)

## 🔗 16. Project Repository

[Multi-Tier Student Management System on GitHub](https://github.com/mahichole69-lab/multi-tier-student-app)

---

**Project Type:** Web Application  
**Backend:** Python Flask  
**Database:** SQLite  
**Architecture:** Three-Tier Architecture  
**Deployment:** Local Development
