# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
  host ="localhost",
  user ="etstudent",
  passwd ="Techsql24#",
  database = "pythonLib"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# Select data from MySQL table using Python

query = "SELECT NAME, ROLL FROM STUDENT"
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
    print(x)

# Where clause

query = "SELECT * FROM STUDENT where AGE >=20"
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
    print(x)

# Order By clause

query = "SELECT * FROM STUDENT ORDER BY NAME DESC"
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
    print(x)

# Limit Clause

query = "SELECT * FROM STUDENT LIMIT 2 OFFSET 1"
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
    print(x)

#Divider 
    
print("--------------------------")

"""
Find all the record who section is 'A'
"""

query = "SELECT * FROM STUDENT WHERE SECTION = 'A' "
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
    print(x)

# disconnecting from server
dataBase.close()

