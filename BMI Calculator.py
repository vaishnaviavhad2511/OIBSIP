import tkinter as tk
from tkinter import messagebox

def reset_entry():
    age_tf.delete(0, 'end')
    height_tf.delete(0, 'end')
    weight_tf.delete(0, 'end')

def calculate_bmi():
    try:
        kg = float(weight_tf.get())
        m = float(height_tf.get()) / 100
        bmi = kg / (m * m)
        bmi = round(bmi, 1)
        bmi_index(bmi)
    except ValueError:
        messagebox.showerror('BMI Calculator', 'Please enter valid numerical values for height and weight.')

def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi} is Underweight')
    elif 18.5 <= bmi < 24.9:
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi} is Normal')
    elif 24.9 <= bmi < 29.9:
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi} is Overweight')
    else:
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi} is Obesity')

ws = tk.Tk()
ws.title('BMI Calculator')
ws.geometry('400x300')

frame = tk.Frame(ws, padx=10, pady=10)
frame.pack(expand=True)

tk.Label(frame, text="Enter Height (cm)").grid(row=0, column=0)
tk.Label(frame, text="Enter Weight (kg)").grid(row=1, column=0)

height_tf = tk.Entry(frame)
height_tf.grid(row=0, column=1, pady=5)

weight_tf = tk.Entry(frame)
weight_tf.grid(row=1, column=1, pady=5)

tk.Button(frame, text='Calculate', command=calculate_bmi).grid(row=2, column=0, pady=5)
tk.Button(frame, text='Reset', command=reset_entry).grid(row=2, column=1, pady=5)
tk.Button(frame, text='Exit', command=ws.destroy).grid(row=2, column=2, pady=5)

ws.mainloop()
