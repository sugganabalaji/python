#Program for adding the column(s) to table
# OracleAlterwithAdd.py
import oracledb as orc # step 1

def alterColAdd():
    try:
        connobj = orc.connect("c##scott/tiger@localhost/orcl") #step 2: Needs to install oracle database on Local system to connect - user > scott
        curobj = connobj.cursor()
        aq = "alter table employee add(company varchar(50))"
        curobj.execute(aq)
        print("Table altered--verify")
    except orc.DatabaseError as db:
        print("Problem on Oracle Databse: ", db)

#Main program
alterColAdd()