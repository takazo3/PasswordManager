from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


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
    email =email_entry.get()
    password =password_entry.get()

    if len(email)==0 or len(password)==0:
        messagebox.showinfo(title="入力エラー",message="入力されていない項目があります。")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"内容: \nEmail:{email}\nPassword: {password}\nこれを記録しますか？")

        if is_ok:
            with  open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")

                website_entry.delete(0, END)
                password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas = Canvas(width=200,height=200)
main_image = PhotoImage(file='logo.png')
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
generate_button =Button(text="Generate Password", bg=BLUE,command=generate_password)
generate_button.grid(column=2,row=3)

add_button =Button(text="Save Password", width=47, bg=PINK, command=save)
add_button.grid(column=1, row=4,columnspan=2)











window.mainloop()
