# Student Database Management System

- This Python application provides a simple Student Database Management System using MySQL and the pymysql library. It allows users to create a table, add students, view all students, update student GPAs, and increment student ages.

## Requirements

- Python 3.x
- pymysql library (install using pip install pymysql)
- MySQL database

## Usage

### 1. Create a Table:

    - Users can create a new table by providing a table name. The table will have columns ID, NAME, AGE, and GPA.

### 2. Add Student:

    - Users can add students to the specified table. They need to provide the student's name, age, and GPA.

### 3. View All Students:

    - Users can view all students in the specified table. The application will display the students' IDs, names, ages, and GPAs.

### 4. Update Student GPA:

    - Users can update a student's GPA by providing the student's ID and the new GPA value.

### 5. Increment Student Age:

    - Users can increment a student's age by providing the student's ID and the increment value.

### 6. Exit:

    - Users can exit the application.

## How to Run

### 1. Database Configuration:

    - Modify the database connection details in the Python script (host, user, password, database) to match your MySQL server configuration.

### 2. Run the Script:

    - Run the Python script using python script_name.py.
    - Follow the on-screen menu to perform various operations on the student database.
