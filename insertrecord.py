# To connect to MySQL, we need mysql-connector-python
import mysql.connector as mydbconnection
from mysql.connector import Error


def insert_record(id, name, price, date):
    conn = None

    try:
        conn = mydbconnection.connect(
            database='usersdb',
            user='root',
            password='password'
        )

        if conn.is_connected():
            print('Connected to MySQL database.')

        # Create cursor
        cursor = conn.cursor()

        # Record we want to insert
        record = (id, name, price, date)

        # SQL query
        query = '''
            INSERT INTO laptop (Id, Name, Price, Purchase_date)
            VALUES (%s, %s, %s, %s)
        '''

        # Execute the query
        cursor.execute(query, record)
        print('Query Executed.')

        # Save changes
        conn.commit()
        print('Transaction Committed.')

        print(f'{cursor.rowcount}: Record inserted successfully.')

    except Error as e:
        print(f'Error: {e}')

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection Closed')


insert_record(1, 'Mac Book Pro', 3000, '2026-09-17')
insert_record(12, 'Lenovo Think Pad', 1400, '2026-09-16')
insert_record(9, 'Alienware', 5000, '2026-08-17')