# FastAPI Authentication and Role-Based Access Control (RBAC)
## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Introduction
This is a FastAPI project that demonstrates the implementation of Authentication, Authorization, and Role-Based Access Control (RBAC) using SQLAlchemy and SQLite. The project includes a user registration system, login functionality with JWT token generation, and role-based access control to secure endpoints based on user roles (Admin, User, Moderator).

## Installation
To install the project, clone the repository and install the dependencies:
```bash
git clone https://github.com/sujanmidatani7/vrv-assignment.git
cd vrv-assignment
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Usage
To start the development server, run:
```bash
uvicorn main:app --reload
```
Open your browser and navigate to `http://localhost:3000` to see the application in action.

## Features
- User registration with hashed password storage.
- Login functionality with JWT token generation.
- Role-Based Access Control (RBAC) to restrict access to specific routes based on user roles.
- In-memory SQLite database for user storage.
- Secure authentication and authorization using JWT tokens.

## Tech Stack
- **FastAPI**: Framework for building APIs with Python.
- **SQLAlchemy**: ORM for interacting with SQLite database.
- **SQLite**: Database for storing user credentials.
- **JWT (JSON Web Tokens)**: Secure token-based authentication.
