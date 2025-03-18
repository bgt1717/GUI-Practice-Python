import tkinter as tk  # Import tkinter for GUI creation
from tkinter import messagebox  # Import messagebox for pop-up warnings
import os  # Import os to check file existence

# Function to load expenses from a file and display them in the listbox
def load_expenses():
    if os.path.exists("expenses.txt"):  # Check if the file exists
        with open("expenses.txt", "r") as file:  # Open the file in read mode
            for line in file:  # Read each line from the file
                listbox.insert(tk.END, line.strip())  # Insert each expense into the listbox

# Function to add a new expense
def add_expense():
    expense = entry.get()  # Get the user input from the entry field
    if expense:  # Check if the input is not empty
        listbox.insert(tk.END, expense)  # Add expense to the listbox
        with open("expenses.txt", "a") as file:  # Open the file in append mode
            file.write(expense + "\n")  # Write the expense to the file with a newline
        entry.delete(0, tk.END)  # Clear the entry field after adding expense
    else:
        messagebox.showwarning("Input Error", "Please enter an expense.")  # Show a warning if input is empty

# Function to delete the selected expense
def delete_expense():
    try:
        selected_index = listbox.curselection()[0]  # Get the index of the selected item
        listbox.delete(selected_index)  # Remove the selected item from the listbox
        update_expense_file()  # Update the file after deletion
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select an expense to delete.")  # Show warning if no selection

# Function to update the expense file after deletion
def update_expense_file():
    with open("expenses.txt", "w") as file:  # Open file in write mode to overwrite existing content
        expenses = listbox.get(0, tk.END)  # Get all items from the listbox
        for expense in expenses:
            file.write(expense + "\n")  # Write each expense back to the file

# Function to load the dark mode setting from a file
def load_dark_mode_setting():
    if os.path.exists("settings.txt"):  # Check if settings file exists
        with open("settings.txt", "r") as file:
            setting = file.read().strip()
            return setting == "dark"  # Return True if 'dark' is saved, False otherwise
    return False  # Default to light mode if no settings file

# Function to save the dark mode setting to a file
def save_dark_mode_setting(is_dark):
    with open("settings.txt", "w") as file:
        file.write("dark" if is_dark else "light")  # Save the current mode as 'dark' or 'light'

# Function to toggle between light mode and dark mode
def toggle_dark_mode():
    global is_dark_mode
    if is_dark_mode:  # If currently in dark mode, switch to light mode
        root.configure(bg="#f0f0f0")
        frame.configure(bg="#f0f0f0")
        label.configure(bg="#f0f0f0", fg="black")
        entry.configure(bg="white", fg="black")
        listbox.configure(bg="white", fg="black")
        add_button.configure(bg="#4CAF50", fg="white")
        delete_button.configure(bg="#f44336", fg="white")
        dark_mode_button.configure(bg="#f0f0f0", fg="black", text="Dark Mode")
    else:  # If currently in light mode, switch to dark mode
        root.configure(bg="#2E2E2E")
        frame.configure(bg="#2E2E2E")
        label.configure(bg="#2E2E2E", fg="white")
        entry.configure(bg="#555555", fg="white")
        listbox.configure(bg="#555555", fg="white")
        add_button.configure(bg="#4CAF50", fg="white")
        delete_button.configure(bg="#f44336", fg="white")
        dark_mode_button.configure(bg="#2E2E2E", fg="white", text="Light Mode")
    
    is_dark_mode = not is_dark_mode  # Toggle the state
    save_dark_mode_setting(is_dark_mode)  # Save the new mode setting

# Create the main application window
root = tk.Tk()  # Initialize the main window
root.title("Expense Tracker")  # Set the window title
root.geometry("500x500")  # Set the window size (width x height)

# Load the dark mode setting from the file (default is light mode)
is_dark_mode = load_dark_mode_setting()

# Apply the dark mode or light mode based on the setting
if is_dark_mode:
    root.configure(bg="#2E2E2E")
    frame_bg = "#2E2E2E"
    label_fg = "white"
    entry_bg = "#555555"
    listbox_bg = "#555555"
    dark_mode_button_text = "Light Mode"
else:
    root.configure(bg="#f0f0f0")
    frame_bg = "#f0f0f0"
    label_fg = "black"
    entry_bg = "white"
    listbox_bg = "white"
    dark_mode_button_text = "Dark Mode"

# Create a frame to center the UI
frame = tk.Frame(root, bg=frame_bg)
frame.pack(expand=True)

# Create a label for the entry field
label = tk.Label(frame, text="Enter Expense:", bg=frame_bg, fg=label_fg, font=("Arial", 20))
label.pack(pady=5)

# Create an entry field for input
entry = tk.Entry(frame, width=30, font=("Arial", 12), bg=entry_bg, fg=label_fg)  # Create an entry widget with width 30 characters
entry.pack(pady=5)  # Display the entry field with padding

# Create an 'Add Expense' button
add_button = tk.Button(frame, text="Add Expense", command=add_expense, bg="#4CAF50", fg="white", font=("Arial", 15), padx=10, pady=5)
add_button.pack(pady=5)  # Display the button with padding

# Create a frame to center the listbox
listbox_frame = tk.Frame(frame)
listbox_frame.pack(pady=10)

# Create a listbox to display the added expenses
listbox = tk.Listbox(listbox_frame, width=50, height=10, font=("Arial", 12), bg=listbox_bg, fg=label_fg, justify="center")  # Centered listbox
listbox.pack()  # Display the listbox

# Create a 'Delete Expense' button
delete_button = tk.Button(frame, text="Delete Expense", command=delete_expense, bg="#f44336", fg="white", font=("Arial", 15), padx=10, pady=5)
delete_button.pack(pady=5)  # Display the button with padding

# Create a 'Dark Mode' toggle button
dark_mode_button = tk.Button(frame, text=dark_mode_button_text, command=toggle_dark_mode, bg=frame_bg, fg=label_fg, font=("Arial", 15), padx=10, pady=5)
dark_mode_button.pack(pady=5)

# Load existing expenses from file (if any)
load_expenses()

# Start the main event loop to keep the application running
root.mainloop()
