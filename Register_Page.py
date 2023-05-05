from tkinter import *
from tkinter import ttk, messagebox
from Database import Connection




class Register:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1000x650")
        self.master.title("Car Rental Management - Register")
        self.master.resizable(False, False)
        self.master.configure(bg="#262626")

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

        self.title_label = ttk.Label(self.master, text="Car Rental Management App - Register", font=("Helvetica", 28, "bold"), foreground="white", background="#262626")
        self.title_label.place(relx=0.5, rely=0.1, anchor=CENTER)


        self.email_label = ttk.Label(self.master, text="Email")
        self.email_label.place(relx=0.3, rely=0.3, anchor=E)
        self.email = ttk.Entry(self.master)
        self.email.place(relx=0.4, rely=0.3, anchor=W, width=300, height=40)

        
        self.username_label = ttk.Label(self.master, text="Username")
        self.username_label.place(relx=0.3, rely=0.4, anchor=E)
        self.username_entry = ttk.Entry(self.master)
        self.username_entry.place(relx=0.4, rely=0.4, anchor=W, width=300, height=40)

       
        self.password_label = ttk.Label(self.master, text="Password")
        self.password_label.place(relx=0.3, rely=0.5, anchor=E)
        self.password_entry = ttk.Entry(self.master, show="*")
        self.password_entry.place(relx=0.4, rely=0.5, anchor=W, width=300, height=40)

        self.Confirm_password_label = ttk.Label(self.master, text="Confirm Password")
        self.Confirm_password_label.place(relx=0.3, rely=0.6, anchor=E)
        self.Confirm_password_entry = ttk.Entry(self.master, show="*")
        self.Confirm_password_entry.place(relx=0.4, rely=0.6, anchor=W, width=300, height=40)

        self.login_button = ttk.Button(self.master, text="Register", command=self.register)
        self.login_button.place(relx=0.5, rely=0.8, anchor=CENTER, width=150, height=40)


        self.back_button = ttk.Button(self.master, text="Back", command=self.back)
        self.back_button.place(relx=0.5, rely=0.7, anchor=CENTER, width=150, height=40)



    def back(self):
        self.master.destroy()
        import Main_Page
        Main_Page.Menu()


    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email.get()
        password_confirmation = self.Confirm_password_entry.get()
        if username == "" or password == "" or email == "" or password_confirmation == "": 
            messagebox.showerror("Error", "Please enter information")
        elif password_confirmation != password : 
            messagebox.showinfo("Error","Password does not match")
        else:
                with Connection() as cursor:
                    query = "INSERT INTO client (nom_client, email, password_client) VALUES (%s, %s, %s)"
                    values = (username, email, password)
                    cursor.execute(query, values)
                    messagebox.showinfo("Success", "Register successful Click Back to Login")
           

if __name__ == '__main__':
    root = Tk()
    register = Register(root)
    root.mainloop()
