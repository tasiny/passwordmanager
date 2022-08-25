from tkinter import *
import random
import string

# CONSTANTS
FONT = ("Arial", 12, "bold")


def store_text():
    """creates text file and amends password data to file"""
    with open("password_list.txt", "a") as file:
        file.write(obtain_stored_pw())


def create_pw():
    """inputs randomized password into entry field"""
    my_string = ""
    for _ in range(12):
        my_string += random_char()
    password_entry.delete(0, "end")
    password_entry.insert(0, my_string)


def obtain_stored_pw():
    """creates error popup for non-entry, else returns all entries as string"""
    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        popup = Toplevel(window)
        popup.geometry("350x150")
        popup.title("Error")
        Label(popup, padx=50, pady=50, text="Do not leave any fields empty", font=FONT).place(x=0, y=0)
    else:
        full_login = f"{website_entry.get()}  |  {email_entry.get()}  |  {password_entry.get()}\n"
        return full_login


def random_char():
    """randomizes a character list and returns a random character"""
    all_char = list(string.punctuation) + list(string.digits) + list(string.ascii_letters)
    random.shuffle(all_char)
    chosen_char = random.choice(all_char)
    return chosen_char


# CANVAS
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)
canvas = Canvas(width=200, height=190)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(60, 95, image=lock_img)
canvas.grid(row=0, column=1)

# LABELS
website_label = Label(text="Website:", font=FONT, justify="right", width=15)
website_label.grid(row=1, column=0, sticky=W+E)
email_label = Label(text="Email/Username:", font=FONT, justify="right", width=15)
email_label.grid(row=2, column=0, sticky=W+E)
password_label = Label(text="Password:", font=FONT, width=15)
password_label.grid(row=3, column=0, sticky=W+E)

# ENTRIES
website_entry = Entry(width=25, justify="left")
website_entry.grid(row=1, column=1, sticky=W)
email_entry = Entry(width=25, justify="left")
email_entry.grid(row=2, column=1, sticky=W)
password_entry = Entry(width=25, justify="left")
password_entry.grid(row=3, column=1, sticky=W)

# BUTTONS
generate_pw_button = Button(command=create_pw, text="Generate Password", justify="right", width=25)
generate_pw_button.grid(row=3, column=1, sticky=E)
add_entry_button = Button(command=store_text, text="Add", width=50)
add_entry_button.grid(row=4, column=1)


window.mainloop()



