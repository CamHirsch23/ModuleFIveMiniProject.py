import mysql.connector
from mysql.connector import Error
import datetime

# Database connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='library_management'
        )
        print("MySQL Database connection successful")
        return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None

# Execute SQL query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as e:
        print(f"Error: '{e}'")

# Classes for the Library Management System
class Book:
    def __init__(self, title, author_id, isbn, publication_date, availability=True):
        self.title = title
        self.author_id = author_id
        self.isbn = isbn
        self.publication_date = publication_date
        self.availability = availability

    def add_book(self, connection):
        query = f"""
        INSERT INTO books (title, author_id, isbn, publication_date, availability)
        VALUES ('{self.title}', {self.author_id}, '{self.isbn}', '{self.publication_date}', {self.availability});
        """
        execute_query(connection, query)

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id

    def add_user(self, connection):
        query = f"""
        INSERT INTO users (name, library_id)
        VALUES ('{self.name}', '{self.library_id}');
        """
        execute_query(connection, query)

class Author:
    def __init__(self, name, biography=None):
        self.name = name
        self.biography = biography

    def add_author(self, connection):
        query = f"""
        INSERT INTO authors (name, biography)
        VALUES ('{self.name}', '{self.biography}');
        """
        execute_query(connection, query)

# Command-Line Interface (CLI) for the Library Management System
def main_menu():
    connection = create_connection()
    while True:
        print("\nWelcome to the Library Management System with Database Integration!")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")
        choice = input("Select an option: ")

        if choice == '1':
            book_operations(connection)
        elif choice == '2':
            user_operations(connection)
        elif choice == '3':
            author_operations(connection)
        elif choice == '4':
            print("Exiting system.")
            break
        else:
            print("Invalid option. Please try again.")

def book_operations(connection):
    print("\nBook Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")
    choice = input("Select an operation: ")
    if choice == '1':
        title = input("Enter book title: ")
        author_id = int(input("Enter author ID: "))
        isbn = input("Enter ISBN: ")
        publication_date = input("Enter publication date (YYYY-MM-DD): ")
        book = Book(title, author_id, isbn, publication_date)
        book.add_book(connection)

def user_operations(connection):
    print("\nUser Operations:")
    print("1. Add a new user")
    choice = input("Select an operation: ")
    if choice == '1':
        name = input("Enter user name: ")
        library_id = input("Enter library ID: ")
        user = User(name, library_id)
        user.add_user(connection)

def author_operations(connection):
    print("\nAuthor Operations:")
    print("1. Add a new author")
    choice = input("Select an operation: ")
    if choice == '1':
        name = input("Enter author name: ")
        biography = input("Enter biography (optional): ")
        author = Author(name, biography)
        author.add_author(connection)

if __name__ == "__main__":
    main_menu()
