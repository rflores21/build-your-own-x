import tkinter as tk
import random

# Function to update the display
def update_display(value):
    current_text = display.get()
    if current_text == "Error":
        clear_display()
        current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + value)

# Function to clear the display
def clear_display(x):
    x.delete(0, tk.END)

# Function to evaluate the expression
# def calculate():
#     random_number = random.randint(1, 100)  # Generate a random number between 1 and 100
#     #display.delete(0, tk.END)
#     display.insert(0, random_number)
def calculate():
    # try:
    #     expression = display.get()
    #     result = int(random(1))
    try:
        expression = display.get()
        result = str(eval(expression))  # Evaluate the expression
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the display
display = tk.Entry(root, font=("Arial", 20), justify="right", bd=10, relief=tk.RIDGE)
display.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=("Arial", 20), padx=20, pady=20, command=calculate)
    elif text == 'C':
        button = tk.Button(root, text=text, font=("Arial", 20), padx=20, pady=20, command=clear_display)
    else:
        button = tk.Button(root, text=text, font=("Arial", 20), padx=20, pady=20, command=lambda t=text: update_display(t))
    button.grid(row=row, column=col, sticky="nsew")

# Configure row and column weights
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Run the application
root.mainloop()