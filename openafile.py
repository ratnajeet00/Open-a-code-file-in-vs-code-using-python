import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, Listbox, Scrollbar, Button

def list_files_and_folders(directory):
    items = os.listdir(directory)
    return items

def open_item_with_default_program(item_path):
    try:
        subprocess.run(["start", item_path], shell=True)
    except FileNotFoundError:
        messagebox.showerror("Error", "Failed to open the item.")

def open_selected_item():
    selected_index = files_listbox.curselection()
    if selected_index:
        selected_item = os.path.join(directory_path.get(), files_listbox.get(selected_index))
        open_item_with_default_program(selected_item)
    else:
        messagebox.showinfo("Info", "Please select an item to open.")

def browse_directory():
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        directory_path.set(selected_directory)
        refresh_item_list()

def refresh_item_list():
    directory = directory_path.get()
    if os.path.isdir(directory):
        items = list_files_and_folders(directory)
        files_listbox.delete(0, tk.END)
        for item in items:
            files_listbox.insert(tk.END, item)

# Create the main application window
app = tk.Tk()
app.title("File and Folder Viewer")

# Create and pack widgets
directory_label = tk.Label(app, text="Directory:")
directory_label.pack()

directory_path = tk.StringVar()
directory_entry = tk.Entry(app, textvariable=directory_path)
directory_entry.pack()

browse_button = tk.Button(app, text="Browse", command=browse_directory)
browse_button.pack()

items_label = tk.Label(app, text="Items:")
items_label.pack()

scrollbar = Scrollbar(app, orient=tk.VERTICAL)
files_listbox = Listbox(app, yscrollcommand=scrollbar.set)
scrollbar.config(command=files_listbox.yview)

files_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

open_button = Button(app, text="Open", command=open_selected_item)
open_button.pack()

refresh_button = Button(app, text="Refresh List", command=refresh_item_list)
refresh_button.pack()

# Start the GUI event loop
app.mainloop()
