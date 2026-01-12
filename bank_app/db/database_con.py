from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()  # configuring the dotenv
from contextlib import contextmanager


@contextmanager
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

    yield db_cursor  # yielding the cursor object which can be used in other functions at its current state

    db_cursor.close()
    db.close()


def get_all_datas():
    with get_connection() as cursor:
        cursor.execute("SELECT * FROM expenses;")  # this will gives us the current use and host
        datas = cursor.fetchall()  # fetching all the datas using sql query
        for expense in datas:  # fetching the data returned after running the query
            print(expense)


def get_expense_date_data(expense_date):  # retrieving the expense data based on expense date
    with get_connection() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s",
                       [expense_date])  # this will gives us the current use and host
        datas = cursor.fetchall()  # fetching all the datas using sql query
        for expense in datas:  # fetching the data returned after running the query
            print(expense)


if __name__ == '__main__':
    get_expense_date_data('2024-08-02')
