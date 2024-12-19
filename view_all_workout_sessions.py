import mysql.connector

def view_all_workout_sessions(conn):
    cursor = conn.cursor()

    query = """
    SELECT ws.session_id, ws.member_id, ws.date, ws.duration_minutes, ws.calories_burned, m.name
    FROM workout_sessions ws
    JOIN members m ON ws.member_id = m.id
    """
    
    try:
        cursor.execute(query)
        sessions = cursor.fetchall()

        if sessions:
            print("\nAll Workout Sessions:")
            for session in sessions:
                print(f"Session ID: {session[0]}, Member ID: {session[1]}, Member Name: {session[5]}, Date: {session[2]}, Duration: {session[3]} min, Calories Burned: {session[4]}")
        else:
            print("No workout sessions found.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
