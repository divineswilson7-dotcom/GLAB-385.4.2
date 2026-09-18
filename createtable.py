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

        # Creates a cursor object that allows SQL actions
        cursor = conn.cursor()

        # Create the laptop table
        query = '''
            CREATE TABLE laptop (
                Id INT,
                Name VARCHAR(255),
                Price INT,
                Purchase_date DATE
            )
        '''

        # Execute the SQL query
        cursor.execute(query)
        print('Table created successfully.')

    except Error as e:
        print(f'Error: {e}')

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection Closed')


if __name__ == "__main__":
    connect()