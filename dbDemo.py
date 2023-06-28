import mysql.connector as sqlActions

#required things

# host, databaseName, user, password

conn = sqlActions.connect(host='localhost',database='APIDevelop', user='root',password='ashutosh5721')

print(conn.is_connected())

cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
row = cursor.fetchone()
print(row)






