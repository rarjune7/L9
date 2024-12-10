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

studentRecord = """CREATE TABLE STUDENT (
                   NAME  VARCHAR(20) NOT NULL,
                   BRANCH VARCHAR(50),
                   ROLL INT NOT NULL,
                   SECTION VARCHAR(5),
                   AGE INT
                   )"""

# table created
cursorObject.execute(studentRecord)

# show the result of decribe sentence
cursorObject.execute("DESCRIBE STUDENT")

myresult = cursorObject.fetchall()
print(myresult)

# disconnecting from server
dataBase.close()
