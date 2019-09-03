from . import countyCSV, roadStreetCSV, villageCSV
import csv
import sqlite3

conn = sqlite3.connect('test.db')
print('Opened database successfully')
# conn.execute('''CREATE TABLE COUNTY
#                 (ZIPCODE CHAR(10) NOT NULL,
#                 COUNTY CHAR(20) NOT NULL,
#                 ENADDR TEXT NOT NULL);''')
# print('Table created successfully')

# conn.close()

csvfile = open(countyCSV, 'r')
rows = csv.reader(csvfile)
for row in rows:
    conn.execute('insert into COUNTY values (?, ?, ?);', (
                row[0],
                row[1],
                row[2]))
for row in con.execute("SELECT * FROM COUNTY"):
    print(row)
conn.close()