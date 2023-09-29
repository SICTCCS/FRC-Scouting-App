
# THIS FILE WILL EXTRACT ALL THE DATA FROM THE DB AND PRINT IT TO THE CONSOLE

import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='root', password='pencil1!',
                              host='10.60.4.27', database='Scores')
cursor = cnx.cursor()

# Execute a SELECT query
query = "SELECT * FROM ScoreTable"
cursor.execute(query)

# Print the results
for row in cursor:
    print(row)

# Close the cursor and database connection
cursor.close()
cnx.close()