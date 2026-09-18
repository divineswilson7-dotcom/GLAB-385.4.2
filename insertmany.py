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

        # Creates a cursor object
        cursor = conn.cursor()

        # Multiple records we want to insert
        records_to_insert = [
            (4, 'HP Pavilion Power', 1999, '2019-01-11'),
            (5, 'MSI WS75 9TL-496', 5799, '2019-02-27'),
            (6, 'Microsoft Surface', 2330, '2019-07-23')
        ]

        # SQL query
        query = '''
            INSERT INTO laptop (Id, Name, Price, Purchase_date)
            VALUES (%s, %s, %s, %s)
        '''

        # Insert all records
        cursor.executemany(query, records_to_insert)
        print('Query Executed.')

        # Save changes
        conn.commit()
        print('Transaction Committed.')

        print(f'{cursor.rowcount}: Record(s) inserted successfully.')

    except Error as e:
        print(f'Error: {e}')

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection Closed')


if __name__ == "__main__":
    connect()