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

# Drop Table in MySQL
query ="DROP TABLE Student;"

cursorObject.execute(query)
dataBase.commit()

# Drop Table if exists
query ="Drop Table if exists Employee;"

cursorObject.execute(query)
dataBase.commit()

# disconnecting from server
dataBase.close()

