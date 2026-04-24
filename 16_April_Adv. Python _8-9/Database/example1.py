import sqlite3

conn=sqlite3.connect("db1.db")
c=conn.cursor()
#sql="create table IF NOT EXISTS student(sid int,sname varchar(20))"
#sql="insert into student values(11,'mahesh')"
sql="select sid,sname from student"
#sql="update student set sname='Dhruv' where sid=11"
ans=c.execute(sql)
rows=c.fetchall()
for i in rows:
    print(i)
conn.commit()
conn.close()

