import string
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# pyperclip - for copy past some piece of data


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_entry.delete(0, END)   # delete previously password

    letters = string.ascii_letters
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # create new string for each every item in list
    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)  # for copy current password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("data.txt", "a") as data_file:

        website = web_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        if len(website) == 0 or len(password) == 0 or len(email) == 0:
            input_validation = messagebox.showinfo(title="Warning!!!",
                                                   message="Please don't leave any fields empty !!!")

        else:
            # check if entered values are valid
            is_ok = messagebox.askyesno(title="Check again !!!", message=f"These are the details: \nEmail: {email} "
                                                                         f"\nPassword: {password} \nIs it ok to save?")
            if is_ok:
                result = f"{website} | {email} | {password} \n"
                data_file.write(result)
                web_entry.delete(0, END)  # delete from 0 to END
                password_entry.delete(0, END)
                web_entry.focus()  # starting new typing from >> website << line


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)  # configure paddings

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=img)  # expecting x and y position
canvas.grid(row=0, column=1)

# Create Labels
txt_web = Label(text="Website: ")
txt_email = Label(text="Email/Username: ")
txt_password = Label(text="Password: ")

txt_web.grid(column=0, row=1)
txt_email.grid(column=0, row=2)
txt_password.grid(column=0, row=3)

# configure Entries
web_entry = Entry(width=36)
email_entry = Entry(width=36)
password_entry = Entry(width=19)

# >> textvariable='password', show="*" << - optional to hide password

# typying starting here
web_entry.focus()

# configure grids
web_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)
email_entry.insert(0, "demurashvili98@gmail.com")  # expecting 0 or END at first argument

password_entry.grid(row=3, column=0, columnspan=2)

# Configure buttons
gen_pass_butt = Button(text="Generate Password", command=password_generator)
gen_pass_butt.grid(row=3, column=1)

add_butt = Button(text="add", width=30, command=save)  # assign to save function
add_butt.grid(row=4, column=1)

window.mainloop()

window.mainloop()
