from tkinter import *
from tkinter import ttk, messagebox



class Login:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1000x650")
        self.master.title("Car Rental Management - Login")
        self.master.resizable(False, False)
        self.master.configure(bg="#262626")

        # Define style
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure(
            "TLabel",
            background="#262626",
            foreground="white",
            font=("Helvetica", 14)
        )
        self.style.configure(
            "TEntry",
            fieldbackground="white",
            font=("Helvetica", 14)
        )
        self.style.map(
            "TButton",
            background=[("active", "#EC4F1D")],
            foreground=[("active", "white")]
        )

        # Add a title label
        self.title_label = ttk.Label(self.master, text="Car Rental Management App", font=("Helvetica", 28, "bold"), foreground="white", background="#262626")
        self.title_label.place(relx=0.5, rely=0.2, anchor=CENTER)

        # Add a username label and entry
        self.username_label = ttk.Label(self.master, text="Username")
        self.username_label.place(relx=0.3, rely=0.4, anchor=E)
        self.username_entry = ttk.Entry(self.master)
        self.username_entry.place(relx=0.4, rely=0.4, anchor=W, width=300, height=40)

        # Add a password label and entry
        self.password_label = ttk.Label(self.master, text="Password")
        self.password_label.place(relx=0.3, rely=0.5, anchor=E)
        self.password_entry = ttk.Entry(self.master, show="*")
        self.password_entry.place(relx=0.4, rely=0.5, anchor=W, width=300, height=40)

        # Add a login button
        self.login_button = ttk.Button(self.master, text="Login", command=self.login)
        self.login_button.place(relx=0.5, rely=0.6, anchor=CENTER, width=150, height=40)

        # Add a back button
        self.back_button = ttk.Button(self.master, text="Back", command=self.back)
        self.back_button.place(relx=0.5, rely=0.7, anchor=CENTER, width=150, height=40)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "" or password == "":
            messagebox.showerror("Error", "Please enter a username and password")
        else:
            from Database import Connection

            with Connection() as cursor:
                query = query = "SELECT * FROM client WHERE nom_client=%s AND password_client=%s"
                values = (username,password)
                cursor.execute(query,values)
                result = cursor.fetchone()

                if result:
                    messagebox.showinfo("Succes","Login succesful")
                    self.master.destroy()
                    import Admin_Page
                    Admin_Page.HomePage()
            
                else:
                    messagebox.showerror("Eroor","Invalid Username or Password")
                   

    def back(self):
        self.master.destroy()
        import Main_Page
        Main_Page.Menu()

if __name__ == '__main__':
    root = Tk()
    login = Login(root)
    root.mainloop()