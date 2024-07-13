import tkinter as tk
from tkinter import ttk

def convert_km_to_miles():
    # Get the value from the entry, convert it to miles, and update the label
    try:
        km = float(km_entry.get())
        miles = km * 0.621371
        result_label.config(text=f"Distance in miles: {miles:.2f}")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("KM to Miles Converter")

# Create a frame to hold the widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Kilometers entry
km_label = ttk.Label(frame, text="Enter distance in kilometers:")
km_label.grid(row=0, column=0, sticky=tk.W, pady=2)

km_entry = ttk.Entry(frame, width=15)
km_entry.grid(row=0, column=1, sticky=tk.W, pady=2)
km_entry.focus()

# Convert button
convert_button = ttk.Button(frame, text="Convert", command=convert_km_to_miles)
convert_button.grid(row=1, column=0, columnspan=2, pady=2)

# Result label
result_label = ttk.Label(frame, text="Distance in miles: ")
result_label.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=2)

# Start the application
root.mainloop()