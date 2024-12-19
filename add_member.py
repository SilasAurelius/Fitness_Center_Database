import mysql.connector
from mysql.connector import Error

def add_member(conn):
    cursor = conn.cursor()

    name = input("Enter member's name: ")
    while True:
        try:
            age = int(input("Enter member's age: "))
            if age < 0:
                raise ValueError("Age cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input for age. Please enter a valid number: {e}")
        return

    insert_query = """
    INSERT INTO members (name, age)
    VALUES (%s, %s)
    """
    new_member = (name, age)

    try:
        cursor.execute(insert_query, new_member)
        conn.commit()
        print(f"New member '{name}' added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
