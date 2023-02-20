"""
Database Connection
"""
import os
import pymysql

def remove_newline(string):
    if isinstance(string, str):
        return string.replace("\n","")
    return None


def mysql_connection():
    try_count = 0
    while try_count < 3:
        try:
            return pymysql.connect(host=remove_newline(os.getenv("DB_HOST")),
                                   user=remove_newline(os.getenv("DB_USER")),
                                   password=remove_newline(os.getenv("DB_PASS")),
                                   database=remove_newline(os.getenv("DB_NAME")),
                                   port=3306,
                                   cursorclass=pymysql.cursors.DictCursor,
                                   client_flag=pymysql.constants.CLIENT.MULTI_STATEMENTS)
        except pymysql.err.OperationalError:
            try_count+= 1
            if try_count == 3:
                raise


def execute_sql(sql, parameter, select=True):
    try:
        with mysql_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parameter)
                if select:
                    return cursor.fetchall()
                connection.commit()
                return None
    except pymysql.err.OperationalError:
        print("error")
        return "problem connection with mysql"


def get_all_customers():
    sql = "SELECT * FROM Customers;"
    results = execute_sql(sql, None, True)
    return results

def add_new_customer(name, email, phone, gender, photo_id, signature):
    sql = "INSERT INTO Customers (Name, Email, Phone, Gender, Photo_ID, Signature) VALUES (%s, %s, %s, %s, %s, %s);"
    print(sql)
    execute_sql(sql, (name, email, phone, gender, photo_id, signature),False)
