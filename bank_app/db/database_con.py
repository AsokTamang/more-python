from dotenv import load_dotenv
import os
import mysql.connector
load_dotenv()  #configuring the dotenv




def get_connection():
    db = mysql.connector.connect(
        host="localhost",
        user=os.getenv("USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        database="expense_manager"
    )

    if db.is_connected():
        print('database connected')
    else:
        print('database not connected')

    db_cursor = db.cursor(
        dictionary=True)  # here cursor is like a sql pointer which helps to run the sql query on databases and with using dictionary=True we

    return db, db_cursor  #returning the connection object and cursor object

def get_all_datas():
    db,db_cursor = get_connection()
    db_cursor.execute("SELECT * FROM expenses;")  # this will gives us the current use and host
    datas = db_cursor.fetchall()  #fetching all the datas using sql query
    for expense in datas:  # fetching the data returned after running the query
        print(expense)
    db_cursor.close()  # closing the cursor first
    db.close()

def get_expense_date_data(expense_date):   #retrieving the expense data based on expense date
    db,db_cursor = get_connection()
    db_cursor.execute("SELECT * FROM expenses WHERE expense_date = %s",[expense_date])  # this will gives us the current use and host
    datas = db_cursor.fetchall()  #fetching all the datas using sql query
    for expense in datas:  # fetching the data returned after running the query
        print(expense)
    db_cursor.close()  # closing the connection
    db.close()
if __name__ == '__main__':
    get_expense_date_data('2024-08-02')
