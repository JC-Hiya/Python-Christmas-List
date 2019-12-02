import tkinter as tk
from tkinter import ttk

controller = None
current_user = None


class Application(tk.Tk):
    def __init__(self):

        global controller

        tk.Tk.__init__(self)

        tk.Tk.wm_title(self, "\'Tis The Season")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)

        menu_bar = tk.Menu(self.container)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=quit)

        menu_bar.add_cascade(label="File", menu=file_menu)
        tk.Tk.configure(self, menu=menu_bar)

        self.frames = {}

        for F in (SignIn, Main):
            frame = F(self.container)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(SignIn)

        controller = self

    def show_frame(self, key):
        frame = self.frames[key]
        frame.tkraise()

    def get_frame(self, key):
        frame = self.frames[key]
        return frame


def pad_grid(self, row_amount, column_amount):
    for i in range(row_amount):
        tk.Frame.grid_rowconfigure(self, i, weight=1)
    for i in range(column_amount):
        tk.Frame.grid_columnconfigure(self, i, weight=1)


def load_main(selected_user):
    global current_user
    if not selected_user == "Select User...":
        current_user = selected_user
        controller.show_frame(Main)


def get_user():
    return current_user


class SignIn(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        pad_grid(self, 5, 4)

        # TODO: Create way to add users

        sign_in_message = tk.Label(self, text="Please select your name:", font=("", 20))

        users = ttk.Combobox(self, values=("Select User...", "User1", "User2", "User3", "User4", "User5", "User6",
                                           "User7", "User8", "User9", "User10", "User11"), state="readonly")
        users.current(0)
        confirm_button = ttk.Button(self, text="Sign In", command=lambda: load_main(users.get()))
        exit_button = ttk.Button(self, text="Exit App", command=quit)

        sign_in_message.grid(row=1, column=1, sticky="nsew", columnspan=2)

        users.grid(row=2, column=1, columnspan=2)

        confirm_button.grid(row=3, column=2, ipadx=15, ipady=15)
        exit_button.grid(row=3, column=1, ipadx=15, ipady=15)


class Main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        pad_grid(self, 1, 1)

        self.master_list = ttk.Treeview(self, columns=2, show=["headings"], selectmode="browse")
        self.master_list["columns"] = ("Who", "What", "Bought By")

        self.master_list.heading("Who", text="Who\'s Asking?")
        self.master_list.heading("What", text="Item Name")
        self.master_list.heading("Bought By", text="Bought By")
        self.master_list.column("Who", width=50)
        self.master_list.column("What", width=50)
        self.master_list.column("Bought By", width=50)

        self.master_list.grid(row=0, column=0, sticky="nsew")


app = Application()

app.geometry("800x600")

app.mainloop()