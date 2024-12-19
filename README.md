#### Fitness Center Database
---
This program allows the user to maintain a fitness center database by connecting a database from MySQL Workbench tool to my Python file.
### CORE FEATURES:
1. Adding a new member
2. Add a workout session
3. Update member information (_Just name and age, I did not include an email row_).
4. View all members
5. Exit the program

### UTILIZING THE DATABASE
I begin by importing mysql.connector. This will help me connect my database and then manipulate it with my Python code.
A try/except block exists to test the connection and handle errors and a success message so the user knows they can proceed.
I've divided the menu functions into modules. This allows more reliable code and helps with the debugging process.

When using this database, cursor is used for my queries to pull data and then manipulate it with commit(). To safely end the query and any new manipulated results, I use cursor.close()

### FINAL THOUGHTS
I found this assignment to be a bit challenging as using MySQL and MySQL Workbench is new to me. Despite the challenge, it was exciting to see how multiple programming languages can work together.
