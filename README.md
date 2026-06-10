# User Management System

A simple full-stack User Management System built using FastAPI, HTML, CSS, and JavaScript. This project demonstrates CRUD (Create, Read, Update, Delete) operations with a clean user interface and dynamic frontend-backend interaction.

## Features

* View all users
* Add new users
* Update existing users
* Delete users with confirmation
* Search users by name
* Display total number of users
* Responsive dark-themed UI
* FastAPI backend with REST APIs
* Frontend built using HTML, CSS, and JavaScript Fetch API

## Tech Stack

### Backend

* FastAPI
* Uvicorn
* Jinja2 Templates

### Frontend

* HTML
* CSS
* JavaScript

## Project Structure

```text
User-Management-System/
│
├── main.py
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── requirements.txt
│
└── README.md
```

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd User-Management-System
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

#### Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
uvicorn main:app --reload
```

Open your browser and visit:

```text
http://127.0.0.1:8000
```

## API Endpoints

| Method | Endpoint                                    | Description         |
| ------ | ------------------------------------------- | ------------------- |
| GET    | /                                           | Home Page           |
| GET    | /all-users                                  | Get all users       |
| GET    | /users/{user_id}                            | Get a specific user |
| POST   | /users-entry/{user_id}/{user_name}/{gender} | Create a user       |
| PUT    | /users-update/{user_id}/{user_name}         | Update user name    |
| DELETE | /users-delete/{user_id}                     | Delete user         |

## Learning Outcomes

Through this project, I learned:

* Building REST APIs using FastAPI
* Serving static files and templates
* Using Jinja2 Templates
* Connecting frontend and backend using Fetch API
* Performing CRUD operations
* Managing project structure and virtual environments
* Using Git and GitHub for version control

## Future Improvements

* Database integration using PostgreSQL or SQLite
* User authentication and authorization
* Dashboard analytics
* User profile management
* Better form validation

## Author

Poojitha Baddigam

Computer Science Engineering (AI & ML)
Frontend Development | UI/UX Design | FastAPI Learning
