# FlaskMySQL

## Overview

This is a simple Flask web application that allows users to submit their personal details, view a list of submitted users, and delete user entries. The application uses MySQL to store the data, which includes the user's first name, surname, email, pet preference, and hobby.

## Features

- **Submit User Details:** Users can input their first name, surname, email, pet preference, and hobby.
- **View Users:** Display a list of all submitted users along with their details.
- **Delete User:** Remove a user's entry from the database.

## Technologies Used

- **Flask:** A lightweight WSGI web application framework for Python.
- **Flask-MySQLdb:** An extension for Flask that adds MySQL database support.
- **MySQL:** A relational database management system to store user data.

## Installation

Follow these steps to get the project running locally:

1. Open MySQL and create the database using the provided SQL file.
2. Update the configuration in the Python file:
   - Change `MYSQL_PASSWORD` and `MYSQL_DB` to match your database credentials.

