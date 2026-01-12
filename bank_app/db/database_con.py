from dotenv import load_dotenv
import os
import mysql.connector
load_dotenv()  #configuring the dotenv
db=mysql.connector.connect(
     host="localhost",
     user=os.getenv("USERNAME"),
     password=os.getenv("DB_PASSWORD"),
     database="expense_manager"
)

if db.is_connected():
    print('database connected')
else:
    print('database not connected')

db_cursor=db.cursor(dictionary=True)  #here cursor is like a sql pointer which helps to run the sql query on databases and with using dictionary=True we are able to get the output in dictionary format
db_cursor.execute("SELECT * FROM expenses;")  #this will gives us the current use and host
datas = db_cursor.fetchall()
for expense in datas:  #fetching the data returned after running the query
    print(expense)
db.close()   #closing the connection