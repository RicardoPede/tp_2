import sys
import MySQLdb
from main import main

def connection():
    main()
    try:
        conn = MySQLdb.connect(host='localhost', user='root', password='', db='mi-base-de-datos')
        print("Connection established")
        return conn

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        sys.exit(1)

conn = connection()

if __name__ == '__main__':
    connection()
