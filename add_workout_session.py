import mysql.connector

def add_workout_session(conn, member_id, date, duration_minutes, calories_burned):
    cursor = conn.cursor()
    
    check_member_query = "SELECT COUNT(*) FROM members WHERE id = %s"
    cursor.execute(check_member_query, (member_id,))
    member_exists = cursor.fetchone()[0]

    if member_exists == 0:
        print(f"Error: Member with ID {member_id} does not exist.")
        cursor.close()
        return

    insert_query = """
    INSERT INTO workout_sessions (member_id, date, duration_minutes, calories_burned)
    VALUES (%s, %s, %s, %s)
    """
    new_session = (member_id, date, duration_minutes, calories_burned)

    try:
        cursor.execute(insert_query, new_session)
        conn.commit()

        print("New workout session added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
