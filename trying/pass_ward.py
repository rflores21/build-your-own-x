import tkinter as tk
import random
import json
from cryptography.fernet import Fernet

#creates key and saves it to a file
key = Fernet.generate_key()
with open('key.key','wb') as file:
    file.write(key)
    
#loads the key
with open('key.key','rb') as file:
    key = file.read()

# Opens the json file and reads the data
with open('storer.json', 'rb') as file:
    passwords = file.read()
    #print(login)

# Encrypts the data
fernet = Fernet(key)
encrypted = fernet.encrypt(passwords)
    
#this writes your new, encrypted data into a new JSON file
with open('encript.txt','wb') as f:
    f.write(encrypted)

#this decrypts the data
#passwords = fernet.decrypt(encrypted)
#print(passwords)

# Create the main window
root = tk.Tk()
#creats the title of the window
root.title("Password Generator")
#Creates the entry boxes for the user to input their information
name = tk.Entry(root, font=("Arial", 20), justify="right", bd=10, relief=tk.RIDGE)
name.grid(row=0, column=0, columnspan=4)

email = tk.Entry(root, font=("Arial", 20), justify="right", bd=10, relief=tk.RIDGE)
email.grid(row=1, column=0, columnspan=4)

password = tk.Entry(root, font=("Arial", 20), justify="right", bd=10, relief=tk.RIDGE)
password.grid(row=2, column=0, columnspan=4)

note = tk.Entry(root, font=("Arial", 20), justify="right", bd=10, relief=tk.RIDGE)
note.grid(row=3, column=0, columnspan=4)


#buttons for the user to interact with
buttons = [('Generate', 4, 0), ('Save', 4, 1), ('Load', 4, 2), ('Clear', 4, 3)]

# Function to generate a random password of a given length
def generate_password():
    valu = password.get()
    value = int(valu)
    passing = ""
    for i in range(value):
        passing += chr(random.randint(33, 126))
    return update_display(passing)

# Function to update the password display
def update_display(value):
    password.delete(0, tk.END)
    password.insert(0, value)

# Function to clear the displays
def clear_displays():
    name.delete(0, tk.END)
    email.delete(0, tk.END)
    password.delete(0, tk.END)
    note.delete(0, tk.END)
    
# Function to save the password and other information
def save_password():
    small = name.get()
    smaller = small.lower()
    passwords['passwords'][smaller] = {'username': email.get(), 'password': password.get(), 'notes': note.get()}
    with open('storer.json', 'w') as typing:
        json.dump(passwords, typing, indent=4)

# Function to load the password and other information
def load_password():
    y = name.get()
    x = y.lower()
    email.delete(0, tk.END)
    password.delete(0, tk.END)
    note.delete(0, tk.END)
    email.insert(0, passwords['passwords'][x]['username'])
    password.insert(0, passwords['passwords'][x]['password'])
    note.insert(0, passwords['passwords'][x]['notes'])

# Add buttons to the window
for (text, row, col) in buttons:
    if text == 'Generate':
        button = tk.Button(root, text=text, font=("Arial", 20), padx=20, pady=20, command=generate_password)
    elif text == 'Save':
        button = tk.Button(root, text=text, font=("Arial", 20), padx=20, pady=20, command=save_password)
    elif text == 'Load':
        button = tk.Button(root, text=text, font=("Arial", 20), padx=20, pady=20, command=load_password)
    else:
        button = tk.Button(root, text=text, font=("Arial", 20), padx=20, pady=20, command=clear_displays)
    button.grid(row=row, column=col, sticky="nsew")
    
    
#run the function
root.mainloop()