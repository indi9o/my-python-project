import tkinter as tk
from tkinter import ttk
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.main import get_greeting, get_day_greeting, create_connection, create_table, insert_greeting, fetch_greetings

def submit():
    name = name_entry.get()
    language = language_var.get()
    greeting = get_greeting(language)
    day_greeting = get_day_greeting()
    
    # Connect to the database
    database = "greetings.db"
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
        insert_greeting(conn, name, f"{greeting}, {name}! {day_greeting}")
    
    # Fetch and display all greetings from the database
    rows = fetch_greetings(conn)
    result_text.set(f"{greeting}, {name}! {day_greeting}\n\nSemua Salam:\n" + "\n".join([str(row) for row in rows]))

# Create the main window
root = tk.Tk()
root.title("Aplikasi Salam")

# Create and place the widgets
ttk.Label(root, text="Masukkan nama Anda:").grid(column=0, row=0, padx=10, pady=10)
name_entry = ttk.Entry(root)
name_entry.grid(column=1, row=0, padx=10, pady=10)

ttk.Label(root, text="Pilih bahasa yang Anda inginkan:").grid(column=0, row=1, padx=10, pady=10)
language_var = tk.StringVar(value="en")
ttk.Radiobutton(root, text="Inggris", variable=language_var, value="en").grid(column=1, row=1, padx=10, pady=10)
ttk.Radiobutton(root, text="Spanyol", variable=language_var, value="es").grid(column=2, row=1, padx=10, pady=10)
ttk.Radiobutton(root, text="Indonesia", variable=language_var, value="id").grid(column=3, row=1, padx=10, pady=10)

submit_button = ttk.Button(root, text="Kirim", command=submit)
submit_button.grid(column=0, row=2, columnspan=3, padx=10, pady=10)

result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text)
result_label.grid(column=0, row=3, columnspan=3, padx=10, pady=10)

# Start the main event loop
root.mainloop()