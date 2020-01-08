import mysql.connector
mydb=mysql.connector.connect(host='localhost',
                             user='root',
                             password='',
                             database='a')
print(mydb.connection_id)
cur=mydb.cursor()
s="create table book(book_id integer(4),title varchar(20),price float(5,2))"
i="insert into book(book_id,title,price) values(%s,%s,%s)"
c=int(input("enter book id:"))
b=input("enter book name:")
n=float(input("enter book price:"))
data=[c,b,n]
cur.execute(i,data)
choose="select * from book"
cur.execute(choose)
result=cur.fetchall()
for rec in result:
    print(rec)

mydb.commit()
