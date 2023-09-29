# THIS FILE WILL CLEAR ALL THE DATA FROM THE DB, USE AT THE END OF EACH COMPETITION
import tkinter as tk
from tkinter import messagebox

# Create a new window
window = tk.Tk()

# Set the window title
window.title("Execute Code?")

# Set the window size
window.geometry("500x200")

# Create a label widget with the question
label = tk.Label(window, text="Are you sure you want to clear the database? Data cannot be recovered once cleared.")

# Pack the label widget into the window
label.pack()

# Create a frame to hold the buttons
button_frame = tk.Frame(window)

# Create a "Yes" button
yes_button = tk.Button(button_frame, text="Yes", command=lambda: execute_code())

# Create a "No" button
no_button = tk.Button(button_frame, text="No", command=lambda: print("Code not executed."))

# Pack the buttons into the frame
yes_button.pack(side=tk.LEFT)
no_button.pack(side=tk.LEFT)

# Pack the frame into the window
button_frame.pack()

# Define a function to execute the code
def execute_code():
    import mysql.connector
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
    # Your code goes here
    print("Data cleared.")
   

# Run the main event loop
window.mainloop()