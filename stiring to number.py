import tkinter as tk

def convert_to_ascii():
    input_text = input_entry.get()
    ascii_result = [ord(char) for char in input_text]
    result_text.config(text=', '.join(str(num) for num in ascii_result))

# Create the main application window
window = tk.Tk()
window.title("ASCII Converter")

# Create input label and entry field
input_label = tk.Label(window, text="Enter alphabets:")
input_label.pack()

input_entry = tk.Entry(window)
input_entry.pack()

# Create result label and colored enter button
result_label = tk.Label(window, text="ASCII Numbers:")
result_label.pack()

result_text = tk.Label(window, text="")
result_text.pack()

enter_button = tk.Button(window, text="Enter", bg="cyan", command=convert_to_ascii)
enter_button.pack()

# Run the application
window.mainloop()
