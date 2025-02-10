# OracleCursorObjEx.py
import oracledb as orc # step 1
try:
    connobj = orc.connect("c##scott/tiger@localhost/orcl") #step 2: Needs to install oracle database on Local system to connect - user > scott
    print("Python Program Got Communication from Oracle Database")
    print("Type of connobj = ", type(connobj))
    print("--------------------------------------")
    curobj = connobj.cursor()
    print("Python Program Created Cursor object")
    print("Type of curobj = ", type(curobj))
except orc.DatabaseError as db:
    print("Problem while getting cursor object: ", db)
