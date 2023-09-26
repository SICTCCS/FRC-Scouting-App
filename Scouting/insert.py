import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="192.168.1.212",
  user="root",
  password="pencil1!",
  database="Scores"
)

# Create a cursor object
mycursor = mydb.cursor()


# Define the SQL query to insert the data
sql = "INSERT INTO users (Team_Name, Mobility, Balance, AmountOfAuto, ConeTop, ConeMiddle, ConeBottom, CubeTop, CubeMiddle, CubeBottom) VALUES (7657, 1, 1, 1, 1, 1, 1, 1, 1, 1)"


# Execute the query
mycursor.execute(sql)

# Commit the changes to the database
mydb.commit()

# Print the number of rows inserted
print(mycursor.rowcount, "record inserted.")