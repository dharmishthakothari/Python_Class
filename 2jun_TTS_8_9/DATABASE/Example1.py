import sqlite3
conn=sqlite3.connect("first.db")
if conn:
    print("Connnection done successfully ")
    cur=conn.cursor()
    #cur.execute("create table IF NOT EXISTS student(sid int,sname varchar(20),email varchar(20))")
    # cur.execute("insert into student values(101,'Shubh','shubh@gmail.com')")
    # conn.commit()
    # conn.close()
    cur.execute("select * from student")
    rows=cur.fetchall()
    for row in rows:
        print(row)
    # cur.execute("update student set sname='mahesh' where sid=101")
    # conn.commit()
    print("Query executed successfully ")

