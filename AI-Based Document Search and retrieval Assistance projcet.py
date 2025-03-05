import os
import re
import tkinter as tk
from tkinter import messagebox

def search_in_file(file_path, search_term):
    matches = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line_number, line in enumerate(lines, start=1):
                if re.search(search_term, line, re.IGNORECASE):
                    highlighted_line=re.sub(f'({search_term})',r'[\1]',line,flags=re.IGNORECASE)
                    matches.append(f"Line {line_number}: {highlighted_line.strip()}")
    except Exception as e:
        matches.append(f"Error reading {file_path}: {e}")
    return matches

def search_in_documents(directory, search_term):

    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):  
                file_path = os.path.join(root, file)
                matches = search_in_file(file_path, search_term)
                if matches:
                    results.append(f"File: {file}")
                    results.extend(matches)
    return results

def start_search():
    directory = directory_entry.get()
    search_term = search_term_entry.get()

    if not directory or not search_term:
        messagebox.showerror("Input Error", "Both directory and search term are required!")
        return

    results = search_in_documents(directory, search_term)
    listbox.delete(0, tk.END)  

    if not results:
        listbox.insert(tk.END, "No matches found.")
    else:
        for result in results:
            listbox.insert(tk.END, result)


root = tk.Tk()
root.title("Document Search Assistant")


directory_label = tk.Label(root, text="Directory Path:")
directory_label.pack(padx=10, pady=5)

directory_entry = tk.Entry(root, width=50)
directory_entry.pack(padx=10, pady=5)

search_term_label = tk.Label(root, text="Search Term:")
search_term_label.pack(padx=10, pady=5)

search_term_entry = tk.Entry(root, width=50)
search_term_entry.pack(padx=10, pady=5)

search_button = tk.Button(root, text="Search", command=start_search)
search_button.pack(pady=10)

listbox = tk.Listbox(root, width=80, height=20)
listbox.pack(padx=10, pady=10)

root.mainloop()
