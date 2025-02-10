# OracleTableCreateEx1.py
import oracledb as orc # step 1
try:
    connobj = orc.connect("c##scott/tiger@localhost/orcl") #step 2: Needs to install oracle database on Local system to connect - user > scott
    print("Python Program Got Communication from Oracle Database")
    print("Type of connobj = ", type(connobj))
    print("--------------------------------------")
    curobj = connobj.cursor()
    print("Python Program Created Cursor object")
    print("Type of curobj = ", type(curobj))
    q = "Create table Employee(empno number(5) primary key, empname varchar2(50) not null, salary number(5,2) not null)"
    q = "Create table temp(id number(5), name varchar2(50))"
    #q = input("Enter Table Creation Query in Oracle DB:")
    #create table citigzen (abc number(4), cname varchar2(20))

    curobj.execute(q)
    print("Table created--verify")
except orc.DatabaseError as db:
    print("Problem on Oracle Databse: ", db)
