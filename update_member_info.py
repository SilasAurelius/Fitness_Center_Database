import mysql.connector
from mysql.connector import Error

def update_member_info(conn):
    cursor = conn.cursor()
    member_id = int(input("Enter the member ID you want to update: "))

    check_member_query = "SELECT COUNT(*) FROM members WHERE id = %s"
    cursor.execute(check_member_query, (member_id,))
    member_exists = cursor.fetchone()[0]

    if member_exists == 0:
        print(f"Error: Member with ID {member_id} does not exist.")
        cursor.close()
        return

    print("Select the information you want to update:")
    print("1. Update Name")
    print("2. Update Age")
    update_choice = int(input("Enter your choice: "))

    if update_choice == 1:
        new_name = input("Enter the new name: ")
        update_query = "UPDATE members SET name = %s WHERE id = %s"
        cursor.execute(update_query, (new_name, member_id))
        print(f"Name updated to {new_name} successfully.")

    elif update_choice == 2:
        while True:
            try:
                new_age = int(input("Enter the new age: "))
                if new_age < 0:
                    raise ValueError("Age cannot be negative.")
                break
            except ValueError as e:
                print(f"Invalid input for age. Please enter a valid number: {e}")
        
        update_query = "UPDATE members SET age = %s WHERE id = %s"
        cursor.execute(update_query, (new_age, member_id))
        print(f"Age updated to {new_age} successfully.")

    else:
        print("Invalid choice. Please select a valid option.")

    conn.commit()
    cursor.close()
