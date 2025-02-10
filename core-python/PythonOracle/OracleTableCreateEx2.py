# OracleTableCreateEx2.py
import oracledb as orc # step 1

def createtable():
    try:
        connobj = orc.connect("c##scott/tiger@localhost/orcl") #step 2: Needs to install oracle database on Local system to connect - user > scott
        curobj = connobj.cursor()
        print("Python Program Created Cursor object")
        print("Type of curobj = ", type(curobj))
        q = "Create table Employee(empno number(5) primary key, empname varchar2(50) not null, salary number(5,2) not null)"
        #q = input("Enter Table Creation Query in Oracle DB:")
        #create table citigzen (abc number(4), cname varchar2(20))

        curobj.execute(q)
        print("Table created--verify")
    except orc.DatabaseError as db:
        print("Problem on Oracle Databse: ", db)

#Main program
createtable()