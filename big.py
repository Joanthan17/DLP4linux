import tkinter as tk
import traceback
from tkinter import ttk
import json
from tkinter import filedialog

# from utils.jsonChecker import validate_JSON_syntax, validate_data_against_schema, generateDataFromSchema
# from utils.tkEditor import Editor

from os.path import basename
from os import *
from os import path as osPath

# from utils.jsonHardened.jsonHardened import validateJsonSecurity, defaultHardenedSchema
#
# from genson import SchemaBuilder

version = "v1.0.0"


def getMiddleGeometry(parent, width=None, height=None):
    if width is None:
        width = parent.winfo_reqwidth()
    if height is None:
        height = parent.winfo_reqheight()
    screen_width = parent.winfo_screenwidth()
    screen_height = parent.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    return '%dx%d+%d+%d' % (width, height, x, y)


# def safeReadJsonFile(path, parent=None):
#     Json_data_text = readFile(path)
#     if Json_data_text is None:
#         return
#     if validate_JSON_syntax(Json_data_text) is not None:
#         PopSyntaxError(path, parent)
#         return
#     return json.loads(Json_data_text)


def PopSyntaxError(path, parent=None):
    window = PopError(text="file " + basename(path) + ": not valid JSON syntax in file " + path, title="Syntax Error in file " + basename(path))
    def showErrInSyntaxTab(parent):
        s = parent.tabsElems["Syntax"]["filesLb"]
        sd =30
        pass

    ttk.Button(window.window, text='Show Me Error in Syntax Tab', command=lambda: showErrInSyntaxTab(parent)).pack()

    return window


class PopupWindow:
    def __init__(self, parent, title='', text=''):
        window = tk.Toplevel(parent)  # Set parent
        window.title(title)
        window.minsize(225, 150)
        # window.geometry(getMiddleGeometry(parent))
        window.focus_set()
        label_title = ttk.Label(window, text=text)
        btn_ok = ttk.Button(window, text='OK', command=lambda: window.destroy())
        label_title.pack(expand=True)
        btn_ok.pack(side=tk.BOTTOM)
        btn_ok.focus_set()
        btn_ok.bind("<Return>", lambda e: window.destroy())
        btn_ok.bind("<Escape>", lambda e: window.destroy())
        window.geometry(
            "+%d+%d" % (parent.winfo_screenwidth() / 2 - window.winfo_reqwidth() / 2, parent.winfo_screenheight() / 2 - window.winfo_reqheight() / 2))
        self.window = window


class PreviewWindow:
    def __init__(self, parent, path=None, title='', text=''):
        self.window = tk.Toplevel(parent)  # Set parent
        self.window.geometry(getMiddleGeometry(parent, 600, 400))
        self.window.title(title)
        text_elem = tk.Text(self.window)
        scrollb = ttk.Scrollbar(text_elem, command=text_elem.yview)
        scrollb.pack(side=tk.RIGHT, fill="y")
        text_elem.config(yscrollcommand=scrollb.set)

        text_elem.insert(tk.INSERT, text)
        text_elem.configure(state="disabled")
        btns_frame = ttk.Frame(self.window)
        ttk.Button(btns_frame, text='OK', command=lambda: self.window.destroy()).grid()

        if path:
            def openEditor():
                print ("Editor")
                # editor = Editor()
                # editor.file_open(path=path)
                # editor.mainloop()

            ttk.Button(btns_frame, text='Edit', command=openEditor).grid(row=0, column=1)
            ttk.Button(btns_frame, text='Open', command=lambda: startfile(path)).grid(row=0, column=2)

        text_elem.pack(expand=True, fill="both")
        btns_frame.pack(side=tk.BOTTOM)


class Menubar(ttk.Frame):
    """Builds a menu bar for the top of the main window"""

    def __init__(self, parent, *args, **kwargs):
        '''Constructor'''
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_menubar()

    def on_exit(self):
        '''Exits program'''
        quit()

    def display_help(self):
        '''Displays help document'''
        pass

    def display_about(self):
        '''Displays info about program'''
        PopupWindow(self, title="About", text='SchemaAutomation Tool\nMade By Eliav Louski\nאגף התקשוב, יחידת מע"וף, ענף הר"ץ\nVersion ' + version)

    def init_menubar(self):
        self.menubar = tk.Menu(self.root)
        self.menu_file = tk.Menu(self.menubar)  # Creates a "File" menu
        self.menu_file.add_command(label='Exit', command=self.on_exit)  # Adds an option to the menu
        self.menubar.add_cascade(menu=self.menu_file,
                                 label='File')  # Adds File menu to the bar. Can also be used to create submenus.

        self.menu_help = tk.Menu(self.menubar)  # Creates a "Help" menu
        self.menu_help.add_command(label='Help', command=self.display_help)
        self.menu_help.add_command(label='About', command=self.display_about)
        self.menubar.add_cascade(menu=self.menu_help, label='Help')

        self.root.config(menu=self.menubar)


class Notebook:
    def __init__(self, parent, tabsNames=None):
        if tabsNames is None:
            tabsNames = []
        self.notebook = ttk.Notebook(parent)
        self.notebook.pack()
        self.tabs = {}
        for tabName in tabsNames:
            self.tabs[tabName] = ttk.Frame(self.notebook)
            self.notebook.add(self.tabs[tabName], text=tabName)
        self.notebook.pack(expand=1, fill="both")


def readFile(path):
    try:
        f = open(path, 'r')
        return f.read()
    except Exception as e:
        errWindow = PopupWindow(root, title="ERROR", text=e.__str__())
        trace = traceback.format_exc()

        def showErrTrace():
            PreviewWindow(root, title="Error Trace " + basename(path), text=trace)

        ttk.Button(errWindow.window, text='Show Error Trace', command=showErrTrace).pack()

        return False


def PopError(text="", title="ERROR"):
    return PopupWindow(root, title=title, text=text)


class ScrollableListboxFrame(ttk.Frame):
    def __init__(self, parent, height=3, onDoubleClick=None, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)
        self.pack(expand=True, fill="both")
        self.listbox = tk.Listbox(self, height=height)
        scrollbar = ttk.Scrollbar(self, command=self.listbox.yview)
        scrollbar.pack(fill="y", side=tk.RIGHT)
        self.listbox.config(yscrollcommand=scrollbar.set)
        self.listbox.pack(expand=True, fill="both")
        self.onDoubleClick = onDoubleClick
        if onDoubleClick is not None:
            self.listbox.bind('<Double-1>', onDoubleClick)


class FilesListboxManager(ScrollableListboxFrame):
    def __init__(self, parent, height=3, onDoubleClick=None, **kwargs):
        def addFiles():
            files = filedialog.askopenfilenames(title='Choose DLP Schema files', filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
            for file in files:
                if file not in lb.get(0, 'end'):
                    lb.insert(lb.size(), file)

        def removeFile():
            if len(lb.curselection()) == 0:
                PopError("Please select file from the list")
                return
            [index] = lb.curselection()
            lb.delete(index)

        def previewFile(*args):
            if len(lb.curselection()) == 0:
                PopError("Please select file from the list")
                return
            [index] = lb.curselection()
            filePath = lb.get(index)
            Json_schema_text = readFile(filePath)
            if Json_schema_text:
                PreviewWindow(root, title="Preview " + basename(filePath), text=Json_schema_text, path=filePath)

        if onDoubleClick is None:
            onDoubleClick = previewFile
        ScrollableListboxFrame.__init__(self, parent, height=height, onDoubleClick=onDoubleClick, **kwargs)
        lb = self.listbox

        # Listbox frame
        btns_frame = ttk.Frame(parent)
        btns_frame.pack(pady=[0, 20])
        ttk.Button(btns_frame, text='Add Files', command=addFiles).grid(padx=5)
        # ttk.Button(btns_frame, text='Preview Selected', command=previewFile).grid(row=0, column=1, padx=5)
        ttk.Button(btns_frame, text='Remove File', command=removeFile).grid(row=0, column=1, padx=5)
        ttk.Button(btns_frame, text='Remove All', command=lambda: lb.delete(0, 'end')).grid(row=0, column=2, padx=5)
        # End of Listbox frame



class ErrorsListboxFrame(ScrollableListboxFrame):
    def __init__(self, parent, height=3, onDoubleClick=None, **kwargs):
        self.errors = []

        def previewError(*args):
            if len(lb.curselection()) == 0:
                PopError("Please select file from the list")
                return
            [index] = lb.curselection()
            filePath = self.errors[index][0]
            Json_schema_text = readFile(filePath)
            if Json_schema_text:
                PreviewWindow(root, title="Error Info " + basename(filePath), text=self.errors[index][1].__str__(), path=filePath)

        if onDoubleClick is None:
            onDoubleClick = previewError
        ScrollableListboxFrame.__init__(self, parent, height=height, onDoubleClick=onDoubleClick, **kwargs)
        lb = self.listbox

    def delete(self, startIndex=0, endIndex=0):
        self.listbox.delete(startIndex, endIndex)
        if endIndex is None:
            endIndex = startIndex
        if startIndex == 'end':
            startIndex = len(self.errors)
        if endIndex == 'end':
            endIndex = len(self.errors)
        self.errors = self.errors[:startIndex] + self.errors[endIndex:]

    def addError(self, filePath, error):
        self.errors.append([filePath, error])
        errorText = 'in File ' + basename(filePath) + ": " + error.__str__()
        self.listbox.insert(self.listbox.size(), errorText)
        # if startIndex == 'end':
        #     startIndex = len(self.erros)
        # if endIndex == 'end':
        #     endIndex = len(self.erros)
        # self.erros = self.erros[startIndex:endIndex]
        # self.listbox.delete(startIndex, endIndex)


class OpenWithPreviewEntry(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.filepath = tk.StringVar()

        def previewFile(*args):
            filePath = self.filepath.get()
            Json_schema_text = readFile(filePath)
            if Json_schema_text:
                PreviewWindow(root, title="Preview " + basename(filePath), text=Json_schema_text, path=filePath)

        def openFile(*args):
            self.filepath.set("")
            file = filedialog.askopenfilename(title='Choose JSON Schema file',
                                              filetypes=(("JSON files", "*.json"), ("all files", "*.*")))
            self.filepath.set(file)

        fileFrame = ttk.Frame(parent)
        ttk.Button(fileFrame, text='Open File', command=openFile).grid(row=1, column=0)
        fileEntry = ttk.Entry(fileFrame, textvariable=self.filepath, width=60)
        fileEntry.grid(row=1, column=1)
        ttk.Button(fileFrame, text='Preview File', command=previewFile).grid(row=1, column=3)
        fileFrame.pack(pady=10)


class JSON_notebook(Notebook):
    def __init__(self, parent):
        tabsNames = ["Syntax", "Data", "Security", "Schema Generator"]
        Notebook.__init__(self, parent, tabsNames)
        self.tabsElems = {name: {} for name in tabsNames}
        self.build_syntax_tab()
        self.build_data_tab()
        # self.build_security_tab()
        self.build_schemaGenerator_tab()

    # def build_security_tab(self):
    #     tab = self.tabs["Security"]
    #     ttk.Label(tab, text="This tool checks if a given schema hardened.", font=("", 10)).pack()
    #     # Listbox frame
    #     ttk.Label(tab, text="Loaded Files").pack()
    #     filesLb = FilesListboxManager(tab)
    #
    #     def validate():
    #         errorsFrame.delete(0, 'end')
    #         valid = True
    #         for file in filesLb.listbox.get(0, 'end'):
    #             Json_schema_text = readFile(file)
    #             if validate_JSON_syntax(Json_schema_text) is not None:
    #                 PopError("file " + basename(file) + ": not valid JSON syntax!")
    #                 return
    #             if Json_schema_text:
    #                 errors = validateJsonSecurity(json.loads(Json_schema_text))
    #                 if errors:
    #                     valid = False
    #                     for error in errors:
    #                         errorsFrame.addError(file, error)
    #         if valid:
    #             PopupWindow(errorsFrame, "Success", "All Files Are Valid!")
    #
    #     def configuration():
    #         confPath = 'utils/jsonHardened/jsonHardenedSchema.json'
    #         with open(confPath) as f:
    #             schemaConfig = json.load(f)
    #         filePath = osPath.join(osPath.dirname(__file__), confPath)
    #         prevWindow = PreviewWindow(root, title="schema Configuration", text=json.dumps(schemaConfig, indent=2), path=filePath)
    #
    #         def restore():
    #             with open(confPath, 'w') as f:
    #                 f.write(json.dumps(defaultHardenedSchema, indent=2))
    #
    #         ttk.Button(prevWindow.window, text='Restore Default', command=restore).pack()
    #
    #     btns_frame = ttk.Frame(tab)
    #     ttk.Button(btns_frame, text='Validate!', command=validate).grid()
    #     ttk.Button(btns_frame, text='Configuration', command=configuration).grid(row=0, column=1)
    #     btns_frame.pack()
    #     ttk.Label(tab, text="validation results:").pack()
    #     errorsFrame = ErrorsListboxFrame(tab, height=5)

    def build_data_tab(self):
        tab = self.tabs["Data"]
        ttk.Label(tab, text="This tool validate json data files against given JSON Schema file.", font=("", 10)).pack(pady=10)
        ttk.Label(tab, text="Schema:").pack()
        fileEntry = OpenWithPreviewEntry(tab)
        fp = fileEntry.filepath
        ttk.Label(tab, text="Loaded Files:").pack()
        filesLb = FilesListboxManager(tab)

        # def validate(parent):
        #     errorsFrame.delete(0, 'end')
        #     jsonSchema = safeReadJsonFile(fp.get(), parent=parent)
        #     if jsonSchema is None: return
        #     valid = True
        #     for file in filesLb.listbox.get(0, 'end'):
        #         jsonData = safeReadJsonFile(file)
        #         if jsonData is None: return
        #         errors = validate_data_against_schema(jsonSchema, jsonData)
        #         for error in errors:
        #             valid = False
        #             errorsFrame.addError(file, error)
        #     if valid:
        #         PopupWindow(errorsFrame, "Success", "All Files Are Valid!")
        #
        # ttk.Button(tab, text='Validate!', command=lambda: validate(self)).pack()
        # ttk.Label(tab, text="validation results:").pack()
        # errorsFrame = ErrorsListboxFrame(tab, height=5)

    def build_syntax_tab(self):
        # Syntax tab
        tab = self.tabs["Syntax"]
        ttk.Label(tab, text="This tool checks if the json files have valid syntax.", font=("", 10)).pack()
        # Listbox frame
        ttk.Label(tab, text="Loaded Files").pack()
        filesLb = FilesListboxManager(tab)

        # def validate():
        #     errorsFrame.delete(0, 'end')
        #     valid = True
        #     for file in filesLb.listbox.get(0, 'end'):
        #         Json_schema_text = readFile(file)
        #         if Json_schema_text:
        #             error = validate_JSON_syntax(Json_schema_text)
        #             if error is not None:
        #                 valid = False
        #                 errorsFrame.addError(file, error)
        #     if valid:
        #         PopupWindow(errorsFrame, "Success", "All Files Are Valid!")
        #
        # ValidateBtn = ttk.Button(tab, text='Validate!', command=validate).pack()
        # ttk.Label(tab, text="validation results:").pack()
        # errorsFrame = ErrorsListboxFrame(tab, height=5)
        #
        # self.tabsElems["Syntax"]["filesLb"] = filesLb
        # self.tabsElems["Syntax"]["ValidateBtn"] = ValidateBtn
        # self.tabsElems["Syntax"]["errorsFrame"] = errorsFrame

    def build_schemaGenerator_tab(self):
        tab = self.tabs["Schema Generator"]
        ttk.Label(tab, text="This tool validate json data files against given JSON Schema file.", font=("", 10)).pack(pady=10)
        ttk.Label(tab, text="Schema:").pack()
        fileEntry = OpenWithPreviewEntry(tab)
        fp = fileEntry.filepath

        # def generate():
        #     schemaPath = fp.get()
        #     Json_schema_text = safeReadJsonFile(schemaPath)
        #     generateDataFromSchema()

        # ttk.Button(tab, text='Generate!', command=generate).pack(expand=True)


class GUI(ttk.Frame):
    """Main GUI class"""

    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)
        self.root = parent
        self.init_gui()

    def init_gui(self):
        self.root.title('Schema Automation Tool ' + version)
        # self.root.geometry("800x600")
        self.root.geometry(getMiddleGeometry(self.root, 800, 600))
        self.grid_columnconfigure(0, weight=1)  # Allows column to stretch upon resizing
        self.grid_rowconfigure(0, weight=1)  # Same with row
        self.root.option_add('*tearOff', 'FALSE')  # Disables ability to tear menu bar into own window

        # Menu Bar
        self.menubar = Menubar(self.root)

        # Tabs
        self.langTabs = Notebook(root, ["JSON", "XML"])
        self.JSON_notebook = JSON_notebook(self.langTabs.tabs["JSON"])

        # Padding
        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=5)


if __name__ == '__main__':
    root = tk.Tk()
    GUI(root)
    root.mainloop()
