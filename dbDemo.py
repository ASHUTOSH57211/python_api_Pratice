import mysql.connector as sqlActions

#required things

# host, databaseName, user, password

conn = sqlActions.connect(host='localhost',database='PythonAutomation', user='root',password='ashutosh5721')

print(conn.is_connected())

cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
row = cursor.fetchone()   #fetch one row from the table
print(row)



