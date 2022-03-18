from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
import os
import sys

FONT_NAME = "Arial"
BLUE = "#4FD3C4"
PINK = "#e2979c"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="入力エラー", message="入力されていない項目があります。")
    else:
        try:
            with open("data.json", "r") as data_file:
                data =json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

#----------------------------FIND FUNCTION__==__________________________#
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="エラー", message="ファイルがありません")

    else:
            if website in data:
                email = data[website]["email"]
                password =data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}")
                pyperclip.copy(password)
            else:
                messagebox.showinfo(title="エラー", message=f"{website}のデータはありません")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas = Canvas(width=200,height=200)
main_image = PhotoImage(file=os.path.join(sys._MEIPASS, 'logo.png'))
canvas.create_image(100,100, image=main_image)
canvas.grid(column=1, row=0)

#Label
website_label = Label(text="Website:", font=(FONT_NAME,10,"bold"))
website_label.grid(column=0, row=1)

id_label = Label(text="Email/Username:", font=(FONT_NAME,10,"bold"))
id_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=(FONT_NAME,10,"bold"))
password_label.grid(column=0, row=3)


#Entry
website_entry = Entry(width=55)
website_entry.grid(column=1,row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=55)
email_entry.grid(column=1,row=2, columnspan=2)
email_entry.insert(0,"password@keep.com")

password_entry = Entry(width=36)
password_entry.grid(column=1,row=3)


#Button
search_button = Button(text="Search", bg="#332FD0",width=15, command=find_password)
search_button.grid(column=2,row=1)

generate_button =Button(text="パスワード自動生成", bg=BLUE,command=generate_password)
generate_button.grid(column=2,row=3)

add_button =Button(text="パスワードを保存する", width=47, bg=PINK, command=save)
add_button.grid(column=1, row=4,columnspan=2)

window.mainloop()
