import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import datetime
from datetime import datetime
import Database

class CarCard(tk.Frame):
    def __init__(self, master, matricule, model, image_path, price):
        super().__init__(master, bg='#F0F0F0', bd=1, relief='solid', width=300, height=400, padx=10, pady=10)

        self.model_label = tk.Label(self, text=model, font=('Helvetica', 14, 'bold'), bg='#FFFFFF')
        self.model_label.grid(row=0, column=0, pady=5)

        image = Image.open(image_path).resize((300, 200), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(image)
        self.image_label = tk.Label(self, image=self.photo)
        self.image_label.grid(row=1, column=0, pady=10)

        self.matricule_label = tk.Label(self, text=matricule, font=('Helvetica', 12), bg='#FFFFFF')
        self.matricule_label.grid(row=2, column=0, pady=5)

        self.price_label = tk.Label(self, text=f'{price} DH', font=('Helvetica', 12), bg='#FFFFFF')
        self.price_label.grid(row=3, column=0, pady=5)

        reserver = tk.Button(self, text="Reserver", bg="#333333", fg="#FFFFFF", bd=0, padx=10, pady=5, command=lambda: self.show_rental_frame(matricule))
        reserver.grid(row=3, column=0, pady=5, sticky="w")

    def show_rental_frame(self, matricule):
        rental_window = tk.Toplevel()
        rental_window.title("Rental Information")
        rental_window.geometry("300x200")

        start_date = datetime.today().date()

        try:
            start_date_entry = DateEntry(rental_window, width=20, font=('Helvetica', 12), state='readonly')
            start_date_entry.pack(pady=5)
            start_date_entry.delete(0, tk.END)
            start_date_entry.insert(0, start_date.strftime('%Y-%m-%d'))
        except AttributeError:
            start_date_entry = ttk.Entry(rental_window, width=20, font=('Helvetica', 12), state='readonly')
            start_date_entry.pack(pady=5)
            start_date_entry.insert(0, start_date.strftime('%Y-%m-%d'))

        end_date_label = tk.Label(rental_window, text="End Date:", font=('Helvetica', 12))
        end_date_label.pack(pady=5)

        end_date_entry = DateEntry(rental_window, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023)
        end_date_entry.pack(pady=5)

        confirm_btn = ttk.Button(rental_window, text="Confirm", command=lambda: self.confirm_rental(matricule, start_date_entry.get(), end_date_entry.get()))
        confirm_btn.pack(pady=10)

    def confirm_rental(self,matricule, start_date_entry, end_date_entry):
        if Database.Connection.is_car_reserved(matricule):
            return "Sorry, the selected car is not available for the selected dates."
    
    # Convert start and end dates to datetime objects
        start_date = datetime.strptime(start_date_entry, '%m/%d/%y')
        end_date = datetime.strptime(end_date_entry, '%m/%d/%y')
    
    # Calculate rental duration and price
        duration = (end_date - start_date).days
        price_per_day = Database.Connection.get_car_price(matricule)
        price = duration * price_per_day
    
    # Add rental to the database
        Database.Connection.add_rental(matricule, start_date, end_date)
        Database.Connection.set_car_reserved(matricule)
    
        messagebox.showinfo("Confirmation", f"Rental confirmed for car {matricule} from {start_date_entry} to {end_date_entry} for a total price of {price}$. Thank you for your rental!")


class HomePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Admin Page")
        self.geometry("1920x1080")
        self.resizable(True, True)
        self.configure(bg='#F0F0F0')

        nav_bar = tk.Frame(self, bg="#333333")
        nav_bar.pack(side="top", fill="x")

        home_btn = tk.Button(nav_bar, text="Home", bg="#333333", fg="#FFFFFF", bd=0, padx=10, pady=5, state="active", command=lambda: self.load_cars(car_container))
        home_btn.pack(side="left")

        rentals_btn = tk.Button(nav_bar, text="Rentals", bg="#333333", fg="#FFFFFF", bd=0, padx=10, pady=5,command=lambda: self.load_reserved_cars(car_container))
        home_btn.pack(side="left")
        rentals_btn.pack(side="left")


        logout_btn = tk.Button(nav_bar, text="Logout", bg="#333333", fg="#FFFFFF", bd=0, padx=10, pady=5, command=self.logout)
        logout_btn.pack(side="right")

        
        car_container = tk.Frame(self, bg="#F0F0F0")
        car_container.pack(side="top", fill="both", expand=True)

        self.load_cars(car_container)

    def load_cars(self, container):
        for widget in container.winfo_children():
            if isinstance(widget,CarCard):
                widget.destroy()

        
        cars=Database.Connection.get_all_cars()

        for i,car in enumerate(cars):
            matricule, model , image_path = car[0] , car[1], car[2]

            with Database.Connection() as cursor:
                cursor.execute("SELECT prix_jour FROM voiture_category WHERE voiture_cat = %s", (car[3],))
                result = cursor.fetchone()

                if result:
                    price = result[0]
                else:
                    price = "N/A"

            card = CarCard(container,matricule,model,image_path,price)
            row = i//3
            col = i% 3
            card.grid(row=row, column=col, padx=110, pady=10, sticky="nw")


    def load_reserved_cars(self,container):
        for widget in container.winfo_children():
            if isinstance(widget,CarCard):
                widget.destroy()

        
        cars=Database.Connection.get_reserved_cars()

        for i,car in enumerate(cars):
            matricule, model , image_path = car[0] , car[1], car[2]

            card = CarCard(container,matricule,model,image_path,"Reserver")
            row = i//3
            col = i% 3
            card.grid(row=row, column=col, padx=110, pady=10, sticky="nw")

            

                

    def logout(self):
        self.destroy()
        import Main_Page
        Main_Page.Menu()

if __name__ == '__main__':
    app = HomePage()
    app.mainloop()
