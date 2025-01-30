import itertools
import smtplib
import random
import time
from tkinter import simpledialog, messagebox

from click.termui import V

symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           '!', '#', '$', '%', '&', '(', ')', '*', '+']

TIMEOUT_SECONDS = 30
VERIFICATION_CODE_LENGTH = 4

class TwoStepVer:


    def __init__(self):
        self.my_email = 'orion20003@gmail.com'
        self.password = 'oole rqoy krlz leuj'


    def send_code(self, recipient_email, code_length):
        # self.ver_code = random.randint(100000, 9999999)
        self.ver_code = ''.join(random.choice(symbols) for _ in range(code_length))
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(self.my_email, self.password)
            smtp.sendmail(self.my_email, recipient_email, f"Subject: Verification Code\n\nYour verification code is: {self.ver_code}")
        return self.ver_code

    def verify_code(self):
        # Create a pop-up input box
        user_code = simpledialog.askstring("Verification", "Enter the verification code sent to your email:")

        if user_code == self.ver_code:
            messagebox.showinfo("Success", "Verification successful!")
            return True
        else:
            messagebox.showerror("Error", "Incorrect verification code.")
            return False

    def brute_force_code(self, actual_code, code_length):
        print("Starting brute force...")

        start_time = time.time()

        for length in range(1, code_length+1):
            for combination in itertools.product(symbols, repeat=length):
                code = ''.join(combination)

                elapsed_time = time.time() - start_time
                if elapsed_time > TIMEOUT_SECONDS:
                    print("Brute force failed due to timeout.")
                    return None

                print(code)
                if code == actual_code:
                    print(f"Brute force code found: {code}")
                    return code
        print("Brute force failed.")
        return None

