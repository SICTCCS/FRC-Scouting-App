import pymysql

# Connect to the database
mydb = pymysql.connect(
  host="10.60.4.27",
  user="Sictc",
  password="Pencil1!",
  database="Scores"
)

# Create a cursor object
mycursor = mydb.cursor()


# Define the SQL query to insert the data
sql = "INSERT INTO ScoreTable (Team_Name, Mobility, Balance, AmountOfAuto, ConeTop, ConeMiddle, ConeBottom, CubeTop, CubeMiddle, CubeBottom) VALUES (7657, 1, 1, 1, 1, 1, 1, 1, 1, 1)"


# Execute the query
mycursor.execute(sql)

# Commit the changes to the database
mydb.commit()

# Print the number of rows inserted
print(mycursor.rowcount, "record inserted.")