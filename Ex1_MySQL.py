# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
  host ="localhost",
  user ="etstudent",
  passwd ="Techsql24#"
)

print(dataBase)

# Disconnecting from the server
dataBase.close()
