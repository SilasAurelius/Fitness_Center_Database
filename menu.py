import mysql.connector
from mysql.connector import Error
import add_member
import add_workout_session
import delete_workout_session
import update_member_info
import view_all_members
import view_all_workout_sessions
import view_members_by_age_range

def connect_database():
    db_name = "fitness_center_db"
    user = "root"
    password = "Password1"
    host = "localhost"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )
        
        print("Connected to MySQL database successfully")
        return conn        
            
    except Error as e:
        print(f"Error: {e}")
        return None

def main():
    conn = connect_database()
    if not conn:
        return
    
    print("Fitness Center Database")
    while True:
        print("==============")
        print(" ****MENU**** ")
        print("==============")
        print("1. Add Member")
        print("2. Add Workout Session")
        print("3. Update Member Info")
        print("4. View All Members")
        print("5. View All Workout Sessions")
        print("6. View All Members Age Between Age Range")
        print("7. Delete Member")
        print("8. Quit")

        user_choice = int(input("Enter selection: "))
        if user_choice == 1:
            add_member.add_member(conn)
        elif user_choice == 2:
            member_id = int(input("Enter member ID: "))
            date = input("Enter workout session date (YYYY-MM-DD): ")
            duration_minutes = int(input("Enter session duration in minutes: "))
            calories_burned = int(input("Enter calories burned: "))
            add_workout_session.add_workout_session(conn, member_id, date, duration_minutes, calories_burned)
        elif user_choice == 3:
            update_member_info.update_member_info(conn)
        elif user_choice == 4:
            view_all_members.view_all_members(conn)
        elif user_choice == 5:
            view_all_workout_sessions.view_all_workout_sessions(conn)
        elif user_choice == 6:
            min_age = int(input("Enter minimum age: "))
            max_age = int(input("Enter maximum age: "))
            view_members_by_age_range.view_members_by_age_range(conn, min_age, max_age)
        elif user_choice == 7:
            delete_workout_session()
        elif user_choice == 8:
            print("Thank you for using the Fitness Center Database. Goodbye.")
            break
        else:
            print("Invalid entry.")

if __name__ == "__main__":
    main()
