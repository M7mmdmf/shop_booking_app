import tkinter as tk
from tkinter import ttk, messagebox
from constants import LUXURY_SHOPS, SHOP_LOCATIONS, ERROR_MESSAGES, SUCCESS_MESSAGES
from validation import validate_all_fields
from csv_handler import initialize_csv, save_booking, search_bookings, sort_bookings

class BookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping and Booking App")
        self.root.geometry("800x600")
        self.root.configure(bg="#f7f7f7")

        # Initialize CSV
        initialize_csv()

        # Input variables
        self.user_name = tk.StringVar()
        self.email = tk.StringVar()
        self.phone = tk.StringVar()
        self.shop_name = tk.StringVar()
        self.booking_time = tk.StringVar()
        self.location = tk.StringVar()

        # Layout
        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Shopping and Booking App", font=("Arial", 20), bg="#f7f7f7")
        title_label.pack(pady=10)

        # Input fields
        form_frame = tk.Frame(self.root, bg="#f7f7f7")
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="User Name:", bg="#f7f7f7").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        tk.Entry(form_frame, textvariable=self.user_name).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Email:", bg="#f7f7f7").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        tk.Entry(form_frame, textvariable=self.email).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Phone:", bg="#f7f7f7").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        tk.Entry(form_frame, textvariable=self.phone).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Shop Name:", bg="#f7f7f7").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        shop_dropdown = ttk.Combobox(form_frame, textvariable=self.shop_name, values=list(LUXURY_SHOPS.keys()))
        shop_dropdown.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Booking Time (HH:MM AM/PM):", bg="#f7f7f7").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        tk.Entry(form_frame, textvariable=self.booking_time).grid(row=4, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Location:", bg="#f7f7f7").grid(row=5, column=0, padx=10, pady=5, sticky="e")
        location_dropdown = ttk.Combobox(form_frame, textvariable=self.location, values=SHOP_LOCATIONS)
        location_dropdown.grid(row=5, column=1, padx=10, pady=5)

        # Buttons
        button_frame = tk.Frame(self.root, bg="#f7f7f7")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Submit Booking", command=self.submit_booking).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(button_frame, text="View All Bookings", command=self.view_bookings).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(button_frame, text="Search Booking", command=self.search_booking).grid(row=0, column=2, padx=10, pady=10)

    def submit_booking(self):
        # Collect input
        data = {
            "user_name": self.user_name.get(),
            "email": self.email.get(),
            "phone": self.phone.get(),
            "shop_name": self.shop_name.get(),
            "booking_time": self.booking_time.get(),
            "location": self.location.get(),
        }

        # Validate input
        validation_result = validate_all_fields(
            data["email"], data["phone"], data["booking_time"], data["shop_name"], data["location"]
        )
        if validation_result:
            messagebox.showerror("Validation Error", validation_result)
            return

        # Save booking
        try:
            save_booking(data)
            messagebox.showinfo("Success", SUCCESS_MESSAGES["booking_successful"])
            self.clear_fields()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_fields(self):
        self.user_name.set("")
        self.email.set("")
        self.phone.set("")
        self.shop_name.set("")
        self.booking_time.set("")
        self.location.set("")

    def view_bookings(self):
        # View all bookings
        bookings = sort_bookings("Booking Time")
        booking_text = "\n".join(
            f"{booking['User Name']} - {booking['Shop Name']} ({booking['Booking Time']}, {booking['Location']})"
            for booking in bookings
        )
        if booking_text:
            messagebox.showinfo("All Bookings", booking_text)
        else:
            messagebox.showinfo("No Bookings", "No bookings found.")

    def search_booking(self):
        # Search bookings
        query = self.email.get()
        if not query:
            messagebox.showerror("Error", "Please enter an email to search.")
            return

        results = search_bookings(query, "Email")
        result_text = "\n".join(
            f"{result['User Name']} - {result['Shop Name']} ({result['Booking Time']}, {result['Location']})"
            for result in results
        )
        if result_text:
            messagebox.showinfo("Search Results", result_text)
        else:
            messagebox.showinfo("No Results", "No bookings found for the given email.")
