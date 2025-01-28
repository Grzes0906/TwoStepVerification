from tkinter import *
from tkinter import messagebox, simpledialog
import random
import pyperclip
import json
import two_step_ver

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

verification = two_step_ver.TwoStepVer()
recipient_email = "grzegorz_pawlak@yahoo.com"

# User credentials for authentication
users_db = {"admin": "password123"}

# ---------------------------- AUTHENTICATION WINDOW ---------------------------- #
def open_authentication_window():

    def login():
        username = username_entry.get()
        password = password_entry.get()

        if username in users_db and users_db[username] == password:
            messagebox.showinfo("Success", "Login successful!")
            auth_window.destroy()
            open_verification_window()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def register():
        username = username_entry.get()
        password = password_entry.get()

        if username in users_db:
            messagebox.showerror("Error", "Username already exists.")
        elif not username or not password:
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            users_db[username] = password
            messagebox.showinfo("Success", "Registration successful! You can now log in.")

    auth_window = Tk()
    auth_window.title("Authentication")
    auth_window.config(padx=50, pady=50)

    Label(auth_window, text="Username:").grid(row=0, column=0)
    username_entry = Entry(auth_window, width=30)
    username_entry.grid(row=0, column=1)

    Label(auth_window, text="Password:").grid(row=1, column=0)
    password_entry = Entry(auth_window, width=30, show="*")
    password_entry.grid(row=1, column=1)

    login_button = Button(auth_window, text="Login", command=login)
    login_button.grid(row=2, column=0, pady=10)

    register_button = Button(auth_window, text="Register", command=register)
    register_button.grid(row=2, column=1, pady=10)

    auth_window.mainloop()

# ---------------------------- VERIFICATION WINDOW ---------------------------- #
def open_verification_window():

    def enter_code():
        verification_code_correct = False
        while not verification_code_correct:
            verification.send_code(recipient_email)
            verification_code_correct = verification.verify_code()
            if verification_code_correct:
                open_main_window()

    def brute_force():
        sent_code = verification.send_code(recipient_email)
        brute_forced_code = verification.brute_force_code(sent_code)
        if brute_forced_code:
            print(f"Brute force successful! Code: {brute_forced_code}")
            open_main_window()
        else:
            print("Brute force failed.")

    verification_window = Tk()
    verification_window.title("Two-Step Verification")
    verification_window.config(padx=50, pady=50)

    enter_code_button = Button(verification_window, text="Enter Code", width=44, command=enter_code)
    enter_code_button.grid(column=1, row=1, columnspan=2)

    brute_force_button = Button(verification_window, text="Bruteforce Attack", width=44, command=brute_force)
    brute_force_button.grid(column=4, row=1, columnspan=2)

    verification_window.mainloop()

# ---------------------------- MAIN WINDOW ---------------------------- #
def open_main_window():

    def generate_password():

        letters_list = [random.choice(letters) for nr in range(random.randint(8, 10))]

        numbers_list = [random.choice(numbers) for nr in range(random.randint(2, 4))]
        symbols_list = [random.choice(symbols) for nr in range(random.randint(2, 4))]
        password_list = numbers_list + symbols_list + letters_list

        random.shuffle(password_list)

        password = "".join(password_list)
        password_textbox.delete(0, END)
        password_textbox.insert(0, password)
        pyperclip.copy(password)


    # ---------------------------- SAVE PASSWORD ------------------------------- #
    def add():
        website = website_textbox.get()
        email = email_textbox.get()
        password = password_textbox.get()

        new_data = {
            website: {
                "Email/Username": email,
                "Password": password,
            }
        }

        if website == '':
            messagebox.showerror('Error', 'Please enter your website')
        elif email == '':
            messagebox.showerror('Error', 'Please enter your email')
        elif password == '':
            messagebox.showerror('Error', 'Please enter your password')
        else:
            try:
                with open("password.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("password.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            except json.decoder.JSONDecodeError:
                with open("password.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("password.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_textbox.delete(0, END)
                email_textbox.delete(0, END)
                password_textbox.delete(0, END)
                website_textbox.focus()


    # ---------------------------- Search ------------------------------- #
    def find_password():
        website = website_textbox.get()
        try:
            with open("password.json", "r") as file:
                data_f = json.load(file)
        except FileNotFoundError:
            messagebox.showerror('Error', 'No Data File Found')
        except json.decoder.JSONDecodeError:
            messagebox.showerror('Error', 'Data file is empty')
        else:
            if website in data_f:
                messagebox.showinfo(website, data_f[website])
            else:
                messagebox.showerror('Error', 'No details for the website exists')



    verification_window.destroy()
    window = Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50)

    canvas = Canvas(window, width=200, height=200)
    logo_png = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image = logo_png)
    canvas.grid(column=1, row=0)

    website_label = Label(text="Website:")
    website_label.grid(column=0, row=1)

    email_label = Label(text="Email/Username:")
    email_label.grid(column=0, row=2)

    password_label = Label(text="Password:")
    password_label.grid(column=0, row=3)

    website_textbox = Entry(width =34)
    website_textbox.grid(column=1, row=1, columnspan=1)
    website_textbox.focus()

    email_textbox = Entry(width=52)
    email_textbox.grid(column=1, row=2, columnspan=2)
    email_textbox.insert(0, "oriion011@gmail.com")

    password_textbox = Entry(width =34)
    password_textbox.grid(column=1, row=3, columnspan=1)

    generate_password_button = Button( text="Generate Password", command = generate_password)
    generate_password_button.grid(column=2, row=3)

    add_button = Button( text="Add", width= 44, command= add)
    add_button.grid(column=1, row=4, columnspan=2)

    search_button = Button( text="Search", width= 14, command= find_password)
    search_button.grid(column=2, row=1)

    window.mainloop()

open_authentication_window()