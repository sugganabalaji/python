#Program for Removing a table
# OracleDropTableEx1.py
import oracledb as orc # step 1

def dropTable():
    try:
        connobj = orc.connect("c##scott/tiger@localhost/orcl") #step 2: Needs to install oracle database on Local system to connect - user > scott
        curobj = connobj.cursor()
        dq = "drop table temp"
        # dq = input("Enter Table Creation Query in Oracle DB:")
        curobj.execute(dq)
        print("Table dropped--verify")
    except orc.DatabaseError as db:
        print("Problem on Oracle Databse: ", db)

#Main program
dropTable()