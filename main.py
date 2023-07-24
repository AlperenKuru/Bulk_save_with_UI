# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 15:02:04 2023

@author: alperenk
"""

import tkinter as tk
from tkinter import filedialog
import requests

def get_access_token():
    url = "[YOUR_AUTHORIZE_REQUEST_URL]"
    data = {
        "LoginID": entry_login_id.get(),
        "Password": entry_password.get()
    }
    response = requests.post(url, json=data)
    response_data = response.json()
    access_token = response_data.get("Token")
    return access_token

def add_entry():
    entry = tk.Entry(root)
    entry.pack()
    entry_SubIds.append(entry)

def show_messages(messages):
    message_window = tk.Toplevel(root)
    message_window.title("Messages")

    message_label = tk.Label(message_window, text="\n".join(messages))
    message_label.pack()

def start_process():
    ValueMainId = entry_ValueMainId.get()
    ValueIsActiveFlag = entry_ValueIsActiveFlag.get()
    
    error_messages = []  # A list to store error messages
    success_messages = []  # A list to store successful messages
    
    # File selection process
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    with open(file_path, "r") as file:
        user_ids = file.read().splitlines()

    # Get Access Token
    access_token = get_access_token()
    
    # Start the loop and POST process
    entry_count = len(entry_SubIds)
    count = 0
    for user_id in user_ids:
        for i in range(entry_count):
            ValueSubId = entry_SubIds[i].get()
            url = "[YOUR_AUTHORIZE_REQUEST_URL]"
            data = {
                "MainId": ValueMainId,
                "SubId": ValueSubId,
                "UserId": user_id,
                "IsActiveFlag": ValueIsActiveFlag,
            }
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, json=data, headers=headers)

            if response.status_code != 200:
                error_message = f"{user_id} Retrieved {response.text} while saving user."
                error_messages.append(error_message)
                print(error_message)  # Also print to the console
                break
            else:
                success_message = f"Posted value user id: {user_id}, SubId: {ValueSubId}"
                success_messages.append(success_message)
                print(success_message)  # Also print to the console
                count += 1
    
    # Show successful and error messages
    show_messages(success_messages)
    show_messages(error_messages)
    
    print(f"Total {count} values posted.")

# Create the main application window
root = tk.Tk()
root.title("Bulk Save With UI")

# Set the window dimensions
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Create input fields and the file select button

label_login_id = tk.Label(root, text="LoginID:")
label_login_id.pack()
entry_login_id = tk.Entry(root)
entry_login_id.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

label_ValueMainId = tk.Label(root, text="MainID:")
label_ValueMainId.pack()
entry_ValueMainId = tk.Entry(root)
entry_ValueMainId.pack()

label_ValueSubId = tk.Label(root, text="SubID:")
label_ValueSubId.pack()
entry_SubIds = []  # A list to store dynamically created SubID Entry fields

button_add = tk.Button(root, text="+", command=add_entry)
button_add.pack()

label_ValueIsActiveFlag = tk.Label(root, text="IsActiveFlag:")
label_ValueIsActiveFlag.pack()
entry_ValueIsActiveFlag = tk.Entry(root)
entry_ValueIsActiveFlag.pack()

button_select_file = tk.Button(root, text="Select file", command=start_process)
button_select_file.pack()


button_select_file = tk.Button(root, text="Start", command=start_process)
button_select_file.pack()

# Start the main loop
root.mainloop()
