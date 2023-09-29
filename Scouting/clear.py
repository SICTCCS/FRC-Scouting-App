# THIS FILE WILL CLEAR ALL THE DATA FROM THE DB, USE AT THE END OF EACH COMPETITION

import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='root', password='pencil1!',
                              host='10.60.4.27', database='Scores')
cursor = cnx.cursor()

# Execute a DELETE query to clear the table
query = "DELETE FROM your_table"
cursor.execute(query)

# Commit the changes to the database
cnx.commit()

# Close the cursor and database connection
cursor.close()
cnx.close()