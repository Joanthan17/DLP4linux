import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from ttkthemes import ThemedTk
import globals


class EnterPasswordInit(ThemedTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("ADLP TM")
        self.geometry()
        self.frame = ttk.Frame(self)
        self.PassFromFile = "0000"  # to load from a secure file on the enviroment or somthing
        row = ttk.Frame(self.frame)
        self.welcome_label = tk.Label(row,
                                      text="welcome to ADLP - DLP solution for Linux Enviroments. \n Please supply password to enter the system.",
                                      anchor='w')
        self.welcome_label.config(font=("Times Roman", 9))
        self.label = tk.Label(row, text="Password: ", anchor='w')
        self.label.config(font=("Times Roman", 12))
        self.entry = ttk.Entry(row, width=20, font=("Times Roman", 12), show='*')
        self.submit = ttk.Button(row, text="Login", command=self._checkpassword)
        row.pack(fill=tk.X)
        self.welcome_label.pack()
        self.label.pack(side=tk.LEFT)
        self.entry.pack(side=tk.LEFT, fill=tk.X, padx=10)
        self.submit.pack(side=tk.LEFT, fill=tk.X)
        self.frame.pack()

    def _checkpassword(self):
        if self.entry.get() == self.PassFromFile:
            globals.StartAppFlag = True
            self.destroy()
        else:
            msg.showerror("Password incorrect", "password incorrect, try again!")


if __name__ == "__main__":
    # execute only if run as a script
    window = EnterPasswordInit()
    window.set_theme("elegance")
    window.mainloop()
