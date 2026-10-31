import mysql.connector
# conn = mysql.connector.connect( 
#     host="localhost", 
#     user="root", 
#     password="Edwin@5923", 
#     database="school_db" 
#     )
# if conn.is_connected(): 
#     print("Connected successfully!")
try: 
    conn = mysql.connector.connect( 
        host="localhost", user="root", 
        password="Edwin@5923", 
        database="school_db" ) 
except mysql.connector.Error as err: 
    print(f"Error: {err}")
cursor = conn.cursor()
cursor.execute( 
    "CREATE TABLE IF NOT EXISTS students (" 
    "id INT AUTO_INCREMENT PRIMARY KEY," 
    "name VARCHAR(255)," 
    "age INT" 
    ")" 
    )

# Inserting data
# sql = "INSERT INTO students (name, age) VALUES (%s, %s)" 
# values = ("anandhakrishnan", 22) 
# try: 
#     cursor.execute(sql, values) 
#     conn.commit() 
# except mysql.connector.Error: 
#     conn.rollback()

#Reading Data
# cursor.execute("SELECT * FROM students") 
# rows = cursor.fetchall() 
# for row in rows: 
#     print(row) 
# cursor.close() 
# conn.close()
# Updating Data
# sql = "UPDATE students SET age = %s WHERE id = %s" 
# values = (39, 2) 
# cursor.execute(sql, values) 
# conn.commit()

# Delete data
# sql = "DELETE FROM students WHERE id = %s" 
# values = (3,) 
# cursor.execute(sql, values) 
# conn.commit()

# Write a Python program that connects to a MySQL database named shop_db and performs the following operations:

# Create a table named products with:
# id – INT, Primary Key, Auto Increment
# product_name – VARCHAR(100)
# price – FLOAT
# quantity – INT
# Insert the following products:
# Laptop, 55000, 5
# Mouse, 800, 20
# Keyboard, 1500, 10