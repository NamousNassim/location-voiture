import tkinter as tk
from tkinter import messagebox
from Login_Page import Login
from Register_Page import Register

class Menu:
    def __init__(self):
      
        self.window = tk.Tk()
        self.window.geometry("1000x650")
        self.window.title("Welcome Page")
        self.window.iconphoto(False, tk.PhotoImage(file="Assets/Car_Logo.png"))
        self.window.configure(bg="#262626")
        self.window.resizable(False, False)

        self.login_btn = tk.Button(
            self.window,
            text="Login",
            font=("Courier", 20, "bold"),
            bg="#EC4F1D",
            fg="white",
            activebackground="white",
            activeforeground="#292929",
            borderwidth=0,
            command=self.show_login,
        )
        self.login_btn.place(x=30, y=170, width=446, height=310)

        self.register_btn = tk.Button(
            self.window,
            text="Register",
            font=("Courier", 20, "bold"),
            bg="#EC4F1D",
            fg="white",
            activebackground="white",
            activeforeground="#292929",
            borderwidth=0,
            command=self.show_register,
        )
        self.register_btn.place(x=524, y=170, width=446, height=310)

        self.credits_label = tk.Label(
            self.window,
            text="This Project is made by Ijjane Adnane , Makoudi Khalid and Namous Nassim",
            font=("Courier", 14),
            bg="#262626",
            fg="white",
        )
        self.credits_label.place(relx=0.5, rely=0.95, anchor="center")

        self.app_name_label = tk.Label(
            self.window,
            text="Car Rental Management App",
            font=("Courier", 24, "bold"),
            bg="#262626",
            fg="white",
        )
        self.app_name_label.place(relx=0.5, rely=0.1, anchor="center")

    def show_login(self):
       self.window.destroy() 
       root = tk.Tk() 
       login = Login(root)  
       root.mainloop()  

    def show_register(self):
       self.window.destroy()  
       root = tk.Tk()  
       register = Register(root)  
       root.mainloop()  


if __name__ == "__main__":
    menu = Menu()
    menu.window.mainloop()
