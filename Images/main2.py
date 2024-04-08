import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Swep@26",
    database="anushkadatabase"
)
mycursor = mydb.cursor()

# Create table if not exists
mycursor.execute('''CREATE TABLE IF NOT EXISTS files
             (id INT AUTO_INCREMENT PRIMARY KEY,
             filename VARCHAR(255),
             date DATETIME)''')

def save_file():
    filename = entry_filename.get()
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql = "INSERT INTO files (filename, date) VALUES (%s, %s)"
    val = (filename, date)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("Success", "File information saved successfully!")

def show_files():
    mycursor.execute("SELECT * FROM files")
    files = mycursor.fetchall()
    if not files:
        messagebox.showinfo("No Files", "No files found in the database.")
    else:
        files_list = '\n'.join([f"File: {file[1]}, Date: {file[2]}" for file in files])
        messagebox.showinfo("Files", files_list)

# GUI
root = tk.Tk()
root.title("File Manager")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False,False)

label_filename = tk.Label(root, text="File Name:")
label_filename.grid(row=0, column=0, padx=5, pady=5)

entry_filename = tk.Entry(root)
entry_filename.grid(row=0, column=1, padx=5, pady=5)

button_save = tk.Button(root, text="Save", command=save_file)
button_save.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="we")

button_show_files = tk.Button(root, text="Show Files", command=show_files)
button_show_files.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

root.mainloop()

# Close the database connection when GUI is closed
mydb.close()