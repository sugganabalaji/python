#Program for Removing a table
# OracleDropTableEx2.py
import oracledb as orc # step 1

def dropTable():
    try:
        connobj = orc.connect("c##scott/tiger@localhost/orcl") #step 2: Needs to install oracle database on Local system to connect - user > scott
        curobj = connobj.cursor()
        tname = input("Enter Table Name to Remove:")#Citizen
        curobj.execute("drop table %s" %tname)
        print("Table dropped--verify")
    except orc.DatabaseError as db:
        print("Problem on Oracle Databse: ", db)

#Main program
dropTable()