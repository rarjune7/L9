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

# Update MySQL table

query = "UPDATE STUDENT SET AGE = 23 WHERE Name ='Ram'"
cursorObject.execute(query)
dataBase.commit()

query = "SELECT * FROM STUDENT"
cursorObject.execute(query)
myresult = cursorObject.fetchall()

for x in myresult:
    print(x)

# Delete Data from Table

query = "DELETE FROM STUDENT WHERE NAME = 'Ram'"
cursorObject.execute(query)
dataBase.commit()

query = "SELECT * FROM STUDENT"
cursorObject.execute(query)
myresult = cursorObject.fetchall()

# Only used when you have to 'show something 
for x in myresult:
    print(x)

"""
Update everone whose selction is 'A' to 'C' 
"""
query = "UPDATE STUDENT SET SECTION = 'C' WHERE SECTION ='A'"
cursorObject.execute(query)
dataBase.commit()


# disconnecting from server
dataBase.close()
