import cgi
import pymysql

form = cgi.FieldStorage()
Team_Name = form.getvalue('Team_Name')
Mobility = form.getvalue('Mobility')
Balance = form.getvalue('Balance')
AmountOfAuto = form.getvalue('AmountOfAuto')
ConeTop = form.getvalue('ConeTop')
ConeMiddle = form.getvalue('ConeMiddle')
ConeBottom = form.getvalue('ConeBottom')
CubeTop = form.getvalue('CubeTop')
CubeMiddle = form.getvalue('CubeMiddle')
CubeBottom = form.getvalue('CubeBottom')


# Connect to the database
mydb = pymysql.connect(
  host="10.60.4.27",
  user="root",
  password="pencil1!",
  database="Scores" 
)

# Create a cursor object
mycursor = mydb.cursor()


# Define the SQL query to insert the data
sql = "INSERT INTO ScoreTable (Team_Name, Mobility, Balance, AmountOfAuto, ConeTop, ConeMiddle, ConeBottom, CubeTop, CubeMiddle, CubeBottom) VALUES ("+str(Team_Name)+","+str(Mobility)+","+str(Balance)+","+str(AmountOfAuto)+","+str(ConeTop)+","+str(ConeMiddle)+","+str(ConeBottom)+","+str(CubeTop)+","+str(CubeMiddle)+","+str(CubeBottom)+" )"


# Execute the query
mycursor.execute(sql)

# Commit the changes to the database
mydb.commit()

# Print the number of rows inserted
print(mycursor.rowcount, "record inserted.")