import mysql.connector

mydb = mysql.connector.connect(
    host="mysql-serhal.alwaysdata.net
    user="serhal",
    password="545-AJK-0101/",
)

mycursor = mydb.cursor()

mycursor.execute("USE API_EXAMPLE")
