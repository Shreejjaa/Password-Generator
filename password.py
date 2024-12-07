import tkinter as tk
from tkinter import messagebox
import pyperclip
import random


def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!@#$%^&*()-_=+[]{}|;:<>,.?/'

    password_letters = [random.choice(letters) for _ in range(8)]
    password_numbers = [random.choice(numbers) for _ in range(4)]
    password_symbols = [random.choice(symbols) for _ in range(2)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = ''.join(password_list)
    password_entry.delete(0, tk.END)  
    password_entry.insert(0, password)  
    pyperclip.copy(password)  
    messagebox.showinfo(title="Password Generated", message="Password copied to clipboard!")


def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please fill out all fields!")
        return

    is_ok = messagebox.askokcancel(
        title=website, 
        message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\n\nSave?"
    )
    if is_ok:
        with open("passwords.txt", "a") as file:
            file.write(f"Website: {website} | Email: {email} | Password: {password}\n")
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        messagebox.showinfo(title="Success", message="Password saved successfully!")


root = tk.Tk()
root.title("Password Manager")
root.config(padx=50, pady=50)


canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tk.PhotoImage(file="logo.png")  
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

tk.Label(text="Website:").grid(row=1, column=0)
tk.Label(text="Email/Username:").grid(row=2, column=0)
tk.Label(text="Password:").grid(row=3, column=0)

website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "demo@example.com")  

password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)

generate_button = tk.Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


root.mainloop()
