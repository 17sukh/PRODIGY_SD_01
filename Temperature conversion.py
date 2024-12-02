import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = unit_var.get()
        
        if unit == "Celsius":
            fahrenheit = (temp * 9/5) + 32
            kelvin = temp + 273.15
            result_label.config(
                text=f"{temp}°C is equivalent to:\n{fahrenheit:.2f}°F\n{kelvin:.2f}K"
            )
        elif unit == "Fahrenheit":
            celsius = (temp - 32) * 5/9
            kelvin = (temp - 32) * 5/9 + 273.15
            result_label.config(
                text=f"{temp}°F is equivalent to:\n{celsius:.2f}°C\n{kelvin:.2f}K"
            )
        elif unit == "Kelvin":
            celsius = temp - 273.15
            fahrenheit = (temp - 273.15) * 9/5 + 32
            result_label.config(
                text=f"{temp}K is equivalent to:\n\t{celsius:.2f}°C\n\t{fahrenheit:.2f}°F"
            )
        else:
            messagebox.showerror("Invalid Input", "Please select a valid unit!")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!")


root = tk.Tk()
root.title("Temperature Converter")

#temperature input
tk.Label(root, text="Enter Temperature:").grid(row=0, column=0, padx=10, pady=10)
entry_temp = tk.Entry(root, width=10)
entry_temp.grid(row=0, column=1, padx=10, pady=10)

# Unit selection
tk.Label(root, text="Select Unit:").grid(row=1, column=0, padx=10, pady=10)
unit_var = tk.StringVar(value="Celsius")  # Default unit
unit_menu = tk.OptionMenu(root, unit_var, "Celsius", "Fahrenheit", "Kelvin")
unit_menu.grid(row=1, column=1, padx=10, pady=10)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result display
result_label = tk.Label(root, text="", justify="left", font=("Times New Roman", 12))
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
