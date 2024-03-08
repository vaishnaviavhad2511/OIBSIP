import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.label_length = tk.Label(master, text="Password Length:")
        self.label_length.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_length = tk.Entry(master)
        self.entry_length.insert(0, "12")
        self.entry_length.grid(row=0, column=1, padx=10, pady=10)

        self.label_options = tk.Label(master, text="Password Options:")
        self.label_options.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.check_upper = tk.BooleanVar()
        self.check_upper.set(True)
        self.checkbox_upper = tk.Checkbutton(master, text="Include Uppercase Letters", variable=self.check_upper)
        self.checkbox_upper.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.check_lower = tk.BooleanVar()
        self.check_lower.set(True)
        self.checkbox_lower = tk.Checkbutton(master, text="Include Lowercase Letters", variable=self.check_lower)
        self.checkbox_lower.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.check_digits = tk.BooleanVar()
        self.check_digits.set(True)
        self.checkbox_digits = tk.Checkbutton(master, text="Include Digits", variable=self.check_digits)
        self.checkbox_digits.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.check_symbols = tk.BooleanVar()
        self.check_symbols.set(True)
        self.checkbox_symbols = tk.Checkbutton(master, text="Include Symbols", variable=self.check_symbols)
        self.checkbox_symbols.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=5, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        length = int(self.entry_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0")
            return

        use_upper = self.check_upper.get()
        use_lower = self.check_lower.get()
        use_digits = self.check_digits.get()
        use_symbols = self.check_symbols.get()

        if not (use_upper or use_lower or use_digits or use_symbols):
            messagebox.showerror("Error", "Select at least one character type")
            return

        characters = ""
        if use_upper:
            characters += string.ascii_uppercase
        if use_lower:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        generated_password = ''.join(random.choice(characters) for _ in range(length))

        pyperclip.copy(generated_password)

        messagebox.showinfo("Password Generated", "Password copied to clipboard:\n{}".format(generated_password))


def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
