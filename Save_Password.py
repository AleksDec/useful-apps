import mysql.connector as mysql
# ------------------------------------
USER = ''
PORT = ''
PASSWORD = ''
HOST = ''
DB = ''
TABLE_NAME = ''

try:
    conn = mysql.connect(user=USER,
              port=PORT,
              password=PASSWORD,
              host=HOST,
              database=DB)

    if conn.is_connected() == True:
        print('Connected!')

    else:
        print('Fail')

except Exception as ex:
    print('Connection failed!')

# --------------- Create cursor --------------------
cursor = conn.cursor()

# --------------- Add row to the table - Option 2 + Autoincrement --------------------
add_password = (f"INSERT INTO {TABLE_NAME} "
              "(Strona, Usługa, Użytkownik, Hasło) "
              "VALUES (%s, %s, %s, %s)")

data_password = ("Strona","Usługa",
                 "Użytkownik","Hasło")

cursor.execute(add_password, data_password)

import csv

query = f"SELECT * FROM {TABLE_NAME}"
cursor.execute(query)

records = cursor.fetchall()
print(cursor.rowcount)

pass_to_csv = []
for row in records:
    pass_to_csv.append(row)

with open (r'C:\...\pass_save.csv','w', newline ='') as file:
    writer = csv.writer(file)
    for password in pass_to_csv:
        writer.writerow(password)

# with open (r'C:\...\pass_save.csv','r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

file.close()

conn.commit()
cursor.close()
conn.close()