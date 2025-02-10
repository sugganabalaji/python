#Program for Rreading the values from KBD and Insert then as Record in Employee table
# OracleInsertRecordEx1.py
import oracledb as orc # step 1

def recordInsert():
    try:
        connobj = orc.connect("c##scott/tiger@localhost/orcl")
        curobj = connobj.cursor()
        iq = "insert into employee values (300,'Hunter',3.6,'matplot')"
        curobj.execute(iq)
        connobj.commit()
        print("Record inserted in Table--verify")
    except orc.DatabaseError as db:
        print("Problem on Oracle Databse: ", db)

#Main program
recordInsert()