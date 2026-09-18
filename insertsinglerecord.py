# To connect to MySQL, we need mysql-connector-python
import mysql.connector as mydbconnection
from mysql.connector import Error


def connect():
    conn = None

    try:
        conn = mydbconnection.connect(
            database='usersdb',
            user='root',
            password='password'
        )

        if conn.is_connected():
            print('Connected to MySQL database.')

        cursor = conn.cursor()

        # Insert one record directly into the laptop table
        query = '''
            INSERT INTO laptop (Id, Name, Price, Purchase_date)
            VALUES (13, 'Mac Air M1', 1000, '2021-08-15')
        '''

        cursor.execute(query)
        print('Query Executed.')

        conn.commit()
        print('Transaction Committed.')

        print(f'{cursor.rowcount}: Record inserted successfully.')

    except Error as e:
        print(f'Error: {e}')

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection Closed')


if __name__ == "__main__":
    connect()