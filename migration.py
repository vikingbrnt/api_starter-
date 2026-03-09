import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS api_example")
mycursor.execute("USE api_example")
mycursor.execute("CREATE TABLE IF NOT EXISTS users_id (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
