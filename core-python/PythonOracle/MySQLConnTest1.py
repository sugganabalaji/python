#Program for getting the connection from MYSQL
# MySQLConnTest1.py
import mysql.connector # step 1
print(mysql.connector.__version__)
# step 2 : Needs to install oracle database on Local system to connect - Sys
con = mysql.connector.connect(host="localhost",
                              user="root",
                              passwd="123456")
print("Python Program Got Communication from MySql Database")

