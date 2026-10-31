import mysql.connector
conn = mysql.connector.connect( 
    host="localhost", 
    user="root", 
    password="Edwin@5923", 
    database="school_db" 
    )

print("Connection established successfully!")