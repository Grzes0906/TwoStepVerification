import smtplib
import random
from tkinter import simpledialog, messagebox

class TwoStepVer:
    def __init__(self):
        self.my_email = 'orion20003@gmail.com'
        self.password = 'oole rqoy krlz leuj'


    def send_code(self, recipient_email):
        self.ver_code = random.randint(100000, 999999)
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(self.my_email, self.password)
            smtp.sendmail(self.my_email, recipient_email, f"Subject: Verification Code\n\nYour verification code is: {self.ver_code}")
        return self.ver_code

    def verify_code(self):
        # Create a pop-up input box
        user_code = simpledialog.askinteger("Verification", "Enter the verification code sent to your email:")

        if user_code == self.ver_code:
            messagebox.showinfo("Success", "Verification successful!")
            return True
        else:
            messagebox.showerror("Error", "Incorrect verification code.")
            return False

# Example usage

