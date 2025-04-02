import mysql.connector

mydb = mysql.connector.connect(
  host="wrc353.encs.concordia.ca",
  port="3306",
  user="wrc353_4",
  password="DBCOMP53",
  database="wrc353_4"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM FamilyMember")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)