from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pswd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    our_website = web_input.get()
    our_email = email_input.get()
    our_password = password_input.get()

    if len(our_website) == 0 or len(our_password) == 0:
        messagebox.showinfo(title="Warning", message="Please don't leave the field empty!")
    else:
        is_ok = messagebox.askokcancel(title=Message,
                                       message=f"These are the details entered:\nEmail: {our_email}\n"
                                               f"Password: {our_password}\nIs it OK to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{our_website} | {our_email} | {our_password}\n")
                web_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

web_input = Entry(width=38)
web_input.grid(row=1, column=1, columnspan=2)
web_input.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_input = Entry(width=38)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "reshmashnr@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_pswd)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=38, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()