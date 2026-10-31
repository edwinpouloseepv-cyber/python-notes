import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Edwin@5923",
        database="shop_db")
except mysql.connector.Error as err:
    print(f"Error: {err}")
cursor = conn.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS products ("
    "id INT AUTO_INCREMENT PRIMARY KEY, "
    "product_name VARCHAR(100), "
    "price FLOAT,"
    "quantity INT"
    ")"
    )

# Inserting data
# sql = "INSERT INTO products (product_name, price, quantity) VALUES (%s, %s, %s)"
# values = ("keyboard", 1500, 10)
# try:
#     cursor.execute(sql, values)
#     conn.commit()
# except mysql.connector.Error as err:
#     print(f"Error: {err}")
#     conn.rollback()


#Reading Data
# cursor.execute("SELECT * FROM products") 
# rows = cursor.fetchall() 
# for row in rows: 
#     print(row) 
# cursor.close() 
# conn.close()

# Updating Data
# sql = "UPDATE products SET price = %s WHERE id = %s" 
# values = (65000, 1) 
# cursor.execute(sql, values) 
# conn.commit()


# Delete data
# sql = "DELETE FROM products WHERE PRODUCT_NAME = %s" 
# values = ("mouse",) 
# cursor.execute(sql, values) 
# conn.commit()
