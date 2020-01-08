import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='')
print(mydb.connection_id)
cur=mydb.cursor()
cur.execute("SHOW DATABASES")


