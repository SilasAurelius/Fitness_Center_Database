import mysql.connector

def delete_workout_session(conn, session_id):
    cursor = conn.cursor()

    check_session_query = "SELECT COUNT(*) FROM workout_sessions WHERE session_id = %s"
    cursor.execute(check_session_query, (session_id,))
    session_exists = cursor.fetchone()[0]

    if session_exists == 0:
        print(f"Error: Workout session with ID {session_id} does not exist.")
        cursor.close()
        return

    delete_query = "DELETE FROM workout_sessions WHERE session_id = %s"

    try:
        cursor.execute(delete_query, (session_id,))
        conn.commit()

        print(f"Workout session with ID {session_id} has been deleted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
