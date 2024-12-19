import mysql.connector

def view_all_members(conn):
    cursor = conn.cursor()

    query = "SELECT id, name, age FROM members"
    
    try:
        cursor.execute(query)
        members = cursor.fetchall()

        if members:
            print("\nAll Members:")
            for member in members:
                print(f"ID: {member[0]}, Name: {member[1]}, Age: {member[2]}")
        else:
            print("No members found.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
