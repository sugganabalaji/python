#Program for Creating the Database from MYSQL
# MySQLDatabaseCreate.py
import mysql.connector

def createdb():
    try:
        con = mysql.connector.connect(host="localhost",
                                  user="root",
                                  passwd="123456")
        dc = "create database Balaji"
        cur=con.cursor()

        cur.execute(dc)
        print("Created Database with Name Balaji")

    except mysql.connector.DatabaseError as error:
        print("Problem in MySSQL: ", error)



#Main program
createdb()



