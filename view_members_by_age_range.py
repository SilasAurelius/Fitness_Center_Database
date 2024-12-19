import mysql.connector

def view_members_by_age_range(conn, min_age, max_age):
    cursor = conn.cursor()

    query = "SELECT id, name, age, email FROM members WHERE age BETWEEN %s AND %s"
    
    try:
        cursor.execute(query, (min_age, max_age))
        members = cursor.fetchall()

        if members:
            print(f"\nMembers Between {min_age} and {max_age} Years Old:")
            for member in members:
                print(f"ID: {member[0]}, Name: {member[1]}, Age: {member[2]}, Email: {member[3]}")
        else:
            print(f"No members found in the age range {min_age} to {max_age}.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
