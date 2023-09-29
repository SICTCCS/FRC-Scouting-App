import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="10.60.4.27",
  user="root",
  password="pencil1!",
  database="Scores"
)

# Create a cursor object
mycursor = mydb.cursor()

# Define the SQL query to rename the table
sql = "ALTER TABLE ScoreTable RENAME TO put_new_table_name"


# Execute the query
mycursor.execute(sql)

# Commit the changes to the database
mydb.commit()

# Print a message to confirm the table was renamed
print("Table renamed successfully.")