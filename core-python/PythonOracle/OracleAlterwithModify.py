#Program for modificationn the column sizes of table
# OracleAlterwithModify.py
import oracledb as orc # step 1

def alterColSizes():
    try:
        connobj = orc.connect("c##scott/tiger@localhost/orcl") #step 2: Needs to install oracle database on Local system to connect - user > scott
        curobj = connobj.cursor()
        aq = "alter table employee modify(empno number(10), empname varchar(15))"
        curobj.execute(aq)
        print("Table altered--verify")
    except orc.DatabaseError as db:
        print("Problem on Oracle Databse: ", db)

#Main program
alterColSizes()