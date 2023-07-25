# connecting to the database instance via python(not via workbench)
import mysql.connector

mydb = mysql.connector.connect(
    host="database-instance1.c65y190l7c1p.us-east-1.rds.amazonaws.com",
    user="admin",
    password="admin12345",
    database="testdb"
)
print(mydb)

# creating database

mycursor = mydb.cursor()  #cursor function gives full control to mydb variable(dbserver) to read, write, select etc

# creating new database
# mycursor.execute("create database testdb1")


#listing databases 
# mycursor.execute("show databases")

# for i in mycursor:
#     print(i)


# creating table

# mycursor.execute("create table drugs (name varchar(10), api varchar(15))")

# mycursor.execute("show tables")

# for i in mycursor:
#     print(i)


# sql = "insert into products (name, brand) values (%s, %s)"
# val = ("adidas", "nike")

# mycursor.execute(sql, val)

# mydb.commit()

# print(mydb.get_row, "record inserted")

# mycursor.execute("select * from products")

# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)

# mycursor.execute("select * from products where brand='nike'")

# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)
