This README provides an overview and setup instructions for the Library Management System (LMS), a Python-based application integrated with a MySQL database. This system is designed to manage books and resources within a library efficiently, allowing users to browse, borrow, return, and explore a collection of books.
Project Overview

The Library Management System is an advanced command-line application that leverages Python and MySQL to facilitate the management of library operations. This project builds upon the object-oriented programming foundations laid in a previous module, extending its capabilities to include database interactions.
Features

Book Operations: Add, borrow, return, search, and display books.
User Operations: Add new users, view user details, and display all users.
Author Operations: Add new authors, view author details, and display all authors.
Database Integration: Utilizes MySQL to store and manage data about books, users, authors, and genres.
Getting Started

Prerequisites

Python 3.6 or higher
MySQL Server
mysql-connector-python
Installation

Clone the repository:
bash


git clone https://github.com/yourusername/library-management-system.git
cd library-management-system
Set up a virtual environment (optional but recommended):
bash


python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install required Python packages:
bash


pip install -r requirements.txt
Create and configure the MySQL database:
Log into MySQL:
bash


mysql -u root -p
Create the database and tables:
sql


CREATE DATABASE library_db;
USE library_db;
SOURCE path/to/database_setup.sql;  # This file contains the SQL commands from the project requirements
Configuration

Update the config.py file with your MySQL user, password, and database details.
Usage

To run the Library Management System:
bash


python ModuleFiveMiniProject.py
Follow the on-screen prompts to interact with the system.
Running Tests

To run tests, execute:
bash


python -m unittest discover -s tests
Ensure you have a tests directory with test files configured properly.
Deployment

For deployment, ensure that your MySQL server is accessible from your deployment environment and that all environment variables are set correctly.
Built With

Python: Core programming language
MySQL: Database management
mysql-connector-python: Database connector used for Python.
