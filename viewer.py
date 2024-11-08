import customtkinter as ctk
import tkinter.filedialog as filedialog
import os
from tkinter import PhotoImage

# Function to open file dialog and show files/folders
def open_folder():
    folder_path = filedialog.askdirectory()  # Opens folder picker
    if folder_path:
        # Clear previous content in the textbox
        textbox.delete(1.0, ctk.END)

        # List files and directories in the selected folder
        try:
            items = os.listdir(folder_path)
            for item in items:
                textbox.insert(ctk.END, item + '\n')  # Insert each item into the textbox
        except Exception as e:
            textbox.insert(ctk.END, f"Error: {e}\n")


# Initialize the main application window
app = ctk.CTk()
app.title("PC Folder and Files Viewer")
app.geometry("400x600")



# Create a button to open the folder dialog
open_button = ctk.CTkButton(app, text="Open Folder", command=open_folder)
open_button.pack(pady=20)

# Create a textbox to display files and folders
textbox = ctk.CTkTextbox(app)
textbox.pack(padx=20, pady=20, fill=ctk.BOTH, expand=True)
# Run the application
app.mainloop()
