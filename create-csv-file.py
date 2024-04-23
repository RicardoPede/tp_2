import csv
import os
from conection import conn

# sql= "SELECT * FROM localidades"
# sql= "SELECT provincia, localidad, cp FROM localidades GROUP BY provincia, localidad, cp"
# sql= "SELECT provincia, GROUP_CONCAT(localidad) FROM localidades GROUP BY provincia"
# sql= "SELECT * FROM localidades ORDER BY provincia ASC"
sql = "SELECT provincia FROM localidades GROUP BY provincia ORDER BY provincia ASC"

def create_csv_from_db():
    connect = conn
    print("Connection established for create_csv_from_db")
    cursor = None
    try:
        cursor = connect.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("Total number of rows is: ", cursor.rowcount)
        print("\n")
        for row in rows:
            create_csv_file(row)
    except Exception as e:
        print(f"Error executing query: {e}")
        connect.rollback()
    finally:
        print("Closing cursor and connection")
        if cursor is not None:
            cursor.close()
        print('connection closed')
        connect.close()

def create_csv_file(row):
    os.makedirs('csv_province', exist_ok=True)
    province = row[0]
    province_file = province+'.csv'
    with open(f'csv_province/{province_file}', 'w', newline='', encoding='utf-8') as file:
        try:
            writer = csv.writer(file)
            writer.writerow(['localidad', 'cp', 'id_prov_mstr'])
            if province:
                sql = f"SELECT localidad, cp, id_prov_mstr FROM localidades WHERE provincia = '{province}'"
                cursor = conn.cursor()
                cursor.execute(sql)
                rows = cursor.fetchall()
                for row in rows:
                    writer.writerow(row)
                writer.writerow(['Total de localidades:', len(rows)])
                print(f"File {province_file} created successfully")
        except Exception as e:
            print(f"Error creating csv file: {e}")
        finally:
            if cursor is not None:
                cursor.close()
    
create_csv_from_db()