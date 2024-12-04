import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from constants import LUXURY_SHOPS, SHOP_LOCATIONS, SHOP_TIME_SLOTS, SUCCESS_MESSAGES
from validation import validate_all_fields
from csv_handler import initialize_csv, save_booking, search_bookings, sort_bookings
from auth_gui import AuthApp


class BookingApp:
    def __init__(self, root, username, email):
        """
        Initializes the booking app.

        Args:
            root: The root Tkinter window.
            username (str): The logged-in user's username.
            email (str): The logged-in user's email.
        """
        self.root = root
        self.root.title("Shopping and Booking App")
        self.root.geometry("800x600")
        self.root.configure(bg="#f7f7f7")  # Light background

        # User details
        self.username = username
        self.email = email

        # Initialize the CSV file
        initialize_csv()

        # Input variables
        self.phone = tk.StringVar()
        self.shop_name = tk.StringVar()
        self.booking_time_slot = tk.StringVar()
        self.location = tk.StringVar()

        # Store all shop names and locations for reference
        self.all_shop_names = list(LUXURY_SHOPS.keys())
        self.all_locations = SHOP_LOCATIONS

        # Load icons
        self.load_icons()

        # Layout
        self.create_widgets()

    def load_icons(self):
        """Load button icons."""
        try:
            # Button icons
            self.submit_icon = ImageTk.PhotoImage(Image.open("assets/submit.png").resize((20, 20)))
            self.view_icon = ImageTk.PhotoImage(Image.open("assets/view.png").resize((20, 20)))
            self.search_icon = ImageTk.PhotoImage(Image.open("assets/search.png").resize((20, 20)))
        except Exception as e:
            print(f"Error loading icons: {e}")

    def create_widgets(self):
        """Create all the input fields, dropdowns, and buttons."""
        # Title
        title_label = tk.Label(self.root, text=f"Welcome, {self.username}!", font=("Arial", 20), bg="#f7f7f7")
        title_label.pack(pady=10)

        # Input fields
        form_frame = tk.Frame(self.root, bg="#f7f7f7")
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="Phone:", bg="#f7f7f7").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        tk.Entry(form_frame, textvariable=self.phone).grid(row=0, column=1, padx=10, pady=5)

        # Shop Name Dropdown
        tk.Label(form_frame, text="Shop Name:", bg="#f7f7f7").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.shop_dropdown = ttk.Combobox(form_frame, textvariable=self.shop_name)
        self.shop_dropdown["values"] = self.all_shop_names
        self.shop_dropdown.bind("<<ComboboxSelected>>", self.update_location_and_time_slots)
        self.shop_dropdown.grid(row=1, column=1, padx=10, pady=5)

        # Time Slot Dropdown
        tk.Label(form_frame, text="Time Slot:", bg="#f7f7f7").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.time_slot_dropdown = ttk.Combobox(form_frame, textvariable=self.booking_time_slot)
        self.time_slot_dropdown["values"] = []  # Initially empty
        self.time_slot_dropdown.grid(row=2, column=1, padx=10, pady=5)

        # Location Dropdown
        tk.Label(form_frame, text="Location:", bg="#f7f7f7").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.location_dropdown = ttk.Combobox(form_frame, textvariable=self.location)
        self.location_dropdown["values"] = self.all_locations
        self.location_dropdown.bind("<<ComboboxSelected>>", self.update_shops_and_time_slots)
        self.location_dropdown.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        button_frame = tk.Frame(self.root, bg="#f7f7f7")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text=" Submit Booking", image=self.submit_icon, compound="left", command=self.submit_booking).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(button_frame, text=" View All Bookings", image=self.view_icon, compound="left", command=self.view_bookings).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(button_frame, text=" Search Booking", image=self.search_icon, compound="left", command=self.search_booking).grid(row=0, column=2, padx=10, pady=10)

    def update_location_and_time_slots(self, event):
        """
        Updates the locations and time slots dropdowns based on the selected shop name.
        Retains the current location and time slot if they are valid.
        """
        selected_shop = self.shop_name.get()
        valid_locations = LUXURY_SHOPS.get(selected_shop, self.all_locations)
        current_location = self.location.get()
        if current_location not in valid_locations:
            self.location.set("")  # Clear location if invalid
        self.location_dropdown["values"] = valid_locations

        # Update time slots
        valid_time_slots = SHOP_TIME_SLOTS.get(selected_shop, [])
        current_time_slot = self.booking_time_slot.get()
        if current_time_slot not in valid_time_slots:
            self.booking_time_slot.set("")  # Clear time slot if invalid
        self.time_slot_dropdown["values"] = valid_time_slots

    def update_shops_and_time_slots(self, event):
        """
        Updates the shop names and time slots dropdowns based on the selected location.
        Retains the current shop name and time slot if they are valid.
        """
        selected_location = self.location.get()
        valid_shops = [
            shop for shop, locations in LUXURY_SHOPS.items() if selected_location in locations
        ]
        current_shop = self.shop_name.get()
        if current_shop not in valid_shops:
            self.shop_name.set("")  # Clear shop name if invalid
        self.shop_dropdown["values"] = valid_shops

        # Update time slots for the current shop if it's still valid
        valid_time_slots = SHOP_TIME_SLOTS.get(self.shop_name.get(), [])
        current_time_slot = self.booking_time_slot.get()
        if current_time_slot not in valid_time_slots:
            self.booking_time_slot.set("")  # Clear time slot if invalid
        self.time_slot_dropdown["values"] = valid_time_slots

    def submit_booking(self):
        """
        Handles the submission of a new booking.
        Saves the username and email from the sign-in session along with the booking details.
        """
        data = {
            "user_name": self.username,
            "email": self.email,
            "phone": self.phone.get(),
            "shop_name": self.shop_name.get(),
            "booking_time": self.booking_time_slot.get(),
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
        """
        Clears all input fields except username and email.
        """
        self.phone.set("")
        self.shop_name.set("")
        self.booking_time_slot.set("")
        self.location.set("")

    def view_bookings(self):
        """
        Displays all bookings sorted by booking time.
        """
        try:
            bookings = sort_bookings("Booking Time")
            if not bookings:
                messagebox.showinfo("No Bookings", "No bookings found.")
                return
            booking_text = "\n".join(
                f"{booking['User Name']} - {booking['Shop Name']} ({booking['Booking Time']}, {booking['Location']})"
                for booking in bookings
            )
            messagebox.showinfo("All Bookings", booking_text)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def search_booking(self):
        """
        Searches bookings for the current logged-in user and displays matching results.
        """
        try:
            results = search_bookings(self.email, "Email")
            if not results:
                messagebox.showinfo("No Results", "No bookings found for your account.")
                return

            result_text = "\n".join(
                f"{result['Shop Name']} ({result['Booking Time']}, {result['Location']})"
                for result in results
            )
            messagebox.showinfo("Your Bookings", result_text)
        except Exception as e:
            messagebox.showerror("Error", str(e))


# Launch the Sign In/Sign Up first, then proceed to the main booking app
def main():
    def launch_booking_app(username, email):
        root = tk.Tk()
        BookingApp(root, username, email)
        root.mainloop()

    # Launch the authentication GUI
    root = tk.Tk()
    AuthApp(root, on_success=lambda username, email: launch_booking_app(username, email))
    root.mainloop()


if __name__ == "__main__":
    main()
