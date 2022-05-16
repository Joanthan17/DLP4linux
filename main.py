from init import *
from classes import *
from tkinter import filedialog


class MainApplication(ThemedTk):
    def __init__(self):
        super().__init__()  # init for tk.TK
        self.title("ADLP - DLP solution for Linux Enviroments")
        self.geometry("700x300")
        # ensure a consistent GUI size
        self.pack_propagate(False)

        self.DevicesNameList = ["Cisco ASA 5500 Series",
                                "Cisco Firepower 1000 Series Appliances",
                                "Cisco Firepower 2100 Series Appliances",
                                "Cisco Firepower 4100 Series Appliances",
                                "Cisco Firepower 7000 Series Appliances",
                                "Cisco Firepower 8000 Series Appliances",
                                "Cisco Firepower 9300 Series Appliances",
                                "Cisco ISA 500 Series",
                                "Cisco ASA 5500 Series",
                                "Cisco Firepower 1000 Series Appliances",
                                "Cisco Firepower 2100 Series Appliances",
                                "Cisco Firepower 4100 Series Appliances",
                                "Cisco Firepower 7000 Series Appliances",
                                "Cisco Firepower 8000 Series Appliances",
                                "Cisco Firepower 9300 Series Appliances",
                                "Cisco ISA 500 Series",
                                "Cisco ASA 5500 Series",
                                "Cisco Firepower 1000 Series Appliances",
                                "Cisco Firepower 2100 Series Appliances",
                                "Cisco Firepower 4100 Series Appliances",
                                "Cisco Firepower 7000 Series Appliances",
                                "Cisco Firepower 8000 Series Appliances",
                                "Cisco Firepower 9300 Series Appliances",
                                "Cisco ISA 500 Series"]
        self.PassFromFile = "0000"  # load password from a secure file on the enviroment
        self.cp_EntriesList = []  # list for change pass event
        self.password_flag = False # init for change pass
        """  -------------------------------- tabs init --------------------------------  """
        self.notebook = ttk.Notebook(self, takefocus=False)  # stores the tabs
        self.FieldsFrame = ttk.Frame(self.notebook, takefocus=False)
        HelpFrame = ttk.Frame(self.notebook, takefocus=False)
        self.notebook.add(self.FieldsFrame, text="ADiLP")
        self.notebook.add(HelpFrame, text="Help")
        self.notebook.pack(fill=tk.BOTH)
        """  ----------------------------------------------------------------------------  """
        """  ------------------------------- set up frame -------------------------------  """
        row = ttk.Frame(self.FieldsFrame)
        txt = "Action: "
        self.label = tk.Label(row, text=txt, anchor='w')
        self.label.config(font=("Times Roman", 12))
        self.file_label = tk.Label(row, text="aaa")
        #self.ent = PlaceholderEntry(row,"input..")
        #self.ent = tk.Entry(row, width=20, font=("Times Roman", 14))
        #self.ent.config(state='disable')
        """  ----------------------------------------------------------------------------  """
        """  ------------------------------- Combobox init ------------------------------  """
        self.drop_menu = ["Enforce Rules",
                          "De-Enforce Rules",
                          "Upload Configuration File",
                          "Upload Udev Rules",
                          "Show Current Devices",
                          "Show Current Configuration",
                          "Monitor Devices",
                          "Identify Device",
                          "Capture Snapshot",
                          "Set New Password",
                          "Remove All Rules"]
        self.filesize_combo = ttk.Combobox(row,
                                           values=self.drop_menu, font=("Times Roman", 12))
        row.pack(fill=tk.X)
        self.label.pack(side=tk.LEFT)

        self.filesize_combo.pack(sid=tk.LEFT)
        self.filesize_combo.set("select action...")
        self.file_label.pack(side=tk.LEFT, fill=tk.X, padx=10)
        #self.ent.pack(side=tk.LEFT, fill=tk.X, padx=10)


        self.filesize_combo.bind("<<ComboboxSelected>>", self._WindowsPopUP)
        """  ----------------------------------------------------------------------------  """
        """  ------------------------------- buttons init -------------------------------  """
        self.StartButton = tk.Button(self.FieldsFrame, text="Run", command=self._GetUserInput)
        self.QuitButton = tk.Button(self.FieldsFrame, text="Quit", command=self._goodbye)

        self.StartButton.pack(padx=5, pady=5)
        self.QuitButton.place(rely=0.0, relx=1.0, x=0, y=0, anchor=tk.NE)
        """  ----------------------------------------------------------------------------  """
        """  ------------------------- text and scroll ----------------------------------  """
        # to be under the stuff

        self.TxtNScroll = TextScrollCombo(self.FieldsFrame)
        self.TxtNScroll.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.TxtNScroll.config(width=400, height=250)
        self.TxtNScroll.txt.config(font=("consolas", 9), undo=True, wrap='word')
        self.TxtNScroll.txt.config(borderwidth=3, relief="sunken")
        quote = ""

       #"""HAMLET: To be, or not to be--that is the question:
       #        Whether 'tis nobler in the mind to suffer
       #        The slings and arrows of outrageous fortune
       #        Or to take arms against a sea of troubles
       #        And by opposing end them. To die, to sleep--
       #        No more--and by a sleep to say we end
       #        The heartache, and the thousand natural shocks
       #        That flesh is heir to. 'Tis a consummation
       #        Devoutly to be wished."""
        self.TxtNScroll.txt.insert(tk.END, quote)
        self.TxtNScroll.txt.config(state='disabled')
        """  -----------------------------------------------------------------------------  """
        """  ------------------------------- Help tab init -------------------------------  """
        self.HelpLabel = tk.Label(HelpFrame, fg="black",
                                   text="This is the _help menu:\n"
                                        "here you will be able to find explanation for everything.")
        self.HelpLabel.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        """  ----------------------------------------------------------------------------  """

    def _AddInput(self, tmp=None):
        """ 0 - "Enforce Rules",
            1 - "De-Enforce Rules"
            2 - Upload Configuration File
            3 - Upload Udev Rules
            4 - Show Current Devices
            5 - Monitor Devices
            6 - Identify Device
            7 - Capture Snapshot
            8 - Set New PAssword
            9 - Remove All Rules
        """
        selected = self.filesize_combo.current()
        if selected == 0:
            print("back end - Enforce API")
        elif selected == 1:
            print("back end - De-Enforce API")
        elif selected == 2:
            print("Upload Configuration File")
            #self.ent.config(state='disable')
        elif selected == 3:
            print("Upload Udev Rules")
            #self.ent.config(state='disable')
        elif selected == 4:
            self._PrintAllDevicesNames()
            print("Show Current Devices")
        elif selected == 5:
            print("Monitor Devices")
        elif selected == 6:
            print("Identify Device")
        elif selected == 7:
            print("Capture Snapshot")
        elif selected == 8:
            if self._SetNewPassword():
                print("password changed - API")
        elif selected == 9:
            print ("Remove All Rules")
            self._RemoveAllRules()


    def _WindowsPopUP(self, e):
        selected = self.filesize_combo.current()
        if selected == 2 :
            self._SelecteFile()
        elif selected == 3:
            self._SelecteFile(type="rules")
        else:
            pass

    def _SelecteFile(self, type="txt"):
        if type == "rules":
            file_path = filedialog.askopenfilename(title="Select Rules File", filetypes=(("rules files" , "*.rules"), ("all files", "*.*")))
        else:
            file_path = filedialog.askopenfilename(title="Select Configuration File", filetypes=(("txt files" , "*.txt"), ("all files", "*.*")))
        self.file_label.configure(text=file_path)
        if file_path:
            with open(file_path, "r") as conf_file:
                self.TxtNScroll.addtext(conf_file.read())

    def _PrintAllDevicesNames(self):
        s = "\n".join(self.DevicesNameList)
        self.TxtNScroll.addtext(s)

    def _RemoveAllRules(self):
        if msg.askokcancel("Remove all rules", "Are you sure you want to Remove all the rules?"):
            print ("removed al rules API")


    def _SetNewPassword(self):
        top_window = globals.spawn_child_window("Change password", self.FieldsFrame)
        fields = "Old Password: ", "New Password: ", "Repeat Password: "
        self.cp_EntriesList = []
        for field in fields:
            row = ttk.Frame(top_window)
            lab_place_saver = tk.Label(row, width=3, anchor='w')
            lab_place_saver.pack(side=tk.LEFT)
            lab = tk.Label(row, width=len(max(fields)) - 1, text=field, anchor='w')
            lab.config(font=("Times Roman", 12))
            ent = tk.Entry(row, width=20, show='*')
            row.pack(fill=tk.X)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.LEFT, padx=3, pady=2, fill=tk.X)
            self.cp_EntriesList.append((ent))
        row2 = ttk.Frame(top_window)
        submit = ttk.Button(row2, text="Set", command=self._CheckNewPassword)
        cancel = ttk.Button(row2, text="Cancel", command=lambda arg1=top_window,: self._exit_changepass_window(arg1))
        row2.pack()
        submit.pack(side=tk.LEFT, fill=tk.X)
        cancel.pack(side=tk.RIGHT, fill=tk.X, padx=10)

    def _CheckNewPassword(self):
        old_pass = self.cp_EntriesList[0].get()
        new_pass1 = self.cp_EntriesList[1].get()
        new_pass2 = self.cp_EntriesList[2].get()
        if len(old_pass) == 0 or len(new_pass1) == 0 or len(new_pass2) == 0:
            msg.showerror("Missing information", "one or more fields are empty!")
        elif old_pass != self.PassFromFile:
            msg.showerror("Password incorrect", "password incorrect, try again!")
            for ent in self.cp_EntriesList:
                ent.delete(0, "end")
        elif new_pass1 != new_pass2:
            msg.showerror("Password incorrect", "unmaching new passwords, try again!")
            for ent in self.cp_EntriesList[1:3]:
                ent.delete(0, "end")
        else:
            self.PassFromFile = new_pass1

    def _exit_changepass_window(self, top_window):
        exit_flag = False
        for ent in self.cp_EntriesList:
            if ent.index("end") != 0:
                exit_flag = True
                break
        if exit_flag:
            if msg.askokcancel("Cancel Acction", "Cancel?"):
                top_window.destroy()
        else:
            top_window.destroy()

    # def enter_password(self, check_password=None):
    #     top_window = spawn_child_window("Enter your password to continue")
    #     self.password_flag = False
    #     row = ttk.Frame(top_window)
    #     label = tk.Label(row, text="Password: ", anchor='w')
    #     label.config(font=("Times Roman", 12))
    #     entry = ttk.Entry(row, width=20, font=("Times Roman", 12), show='*')
    #     submit = ttk.Button(row, text="Login",
    #                         command=lambda arg1=top_window, arg2=entry: self.checkpassword(arg1, arg2))
    #     row.pack(fill=tk.X)
    #     label.pack(side=tk.LEFT)
    #     entry.pack(side=tk.LEFT, fill=tk.X, padx=10)
    #     submit.pack(side=tk.LEFT, fill=tk.X)
    #
    # def checkpassword(self, top_window, entry):
    #     if entry.get() == self.PassFromFile:
    #         top_window.destroy()
    #         self.password_flag = True
    #     else:
    #         msg.showerror("Password incorrect", "password incorrect, try again!")
    #     self.password_flag = False

    def _goodbye(self):
        if msg.askokcancel("Goodbye?", "Are you sure you want to close ADLP?"):
            self.notebook.quit()

    def _help(self):
        print(self.winfo_width())

    def _DisableChildren(self, parent):
        """ disables every child of a given parent (recursively)"""
        for child in parent.winfo_children():
            wtype = child.winfo_class()
            # print (wtype)
            if wtype not in ('TFrame', 'Frame', 'Labelframe', 'TScale'):
                child.configure(state='disable')
            else:
                self._DisableChildren(child)

    def _GetUserInput(self, text=None):
        """ saves all user data for backend and disabling the first tab"""
        if not text:
            self._AddInput()


if __name__ == "__main__":
    # execute only if run as a script
    windowinit = EnterPasswordInit()
    windowinit.set_theme("elegance")
    windowinit.mainloop()
    if globals.StartAppFlag:
        window = MainApplication()
        window.set_theme("elegance")
        window.mainloop()
