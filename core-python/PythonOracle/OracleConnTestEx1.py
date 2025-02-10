# OracleConnTestEx1.py
import oracledb as orc # step 1
print(orc.__version__)
try:
    # step 2 : Needs to install oracle database on Local system to connect - Sys
    connobj = orc.connect("system/root@localhost/orcl")
    print("Python Program Got Communication from Oracle Database")
    print("Type of connobj = ", type(connobj))
except orc.DatabaseError as db:
    print("Problem while connecting to Oracle Database: ", db)
