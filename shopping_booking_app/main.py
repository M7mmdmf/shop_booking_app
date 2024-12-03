import tkinter as tk
from gui import BookingApp

def main():
    """
    Entry point for the Shopping and Booking App.
    Initializes and runs the Tkinter GUI.
    """
    # Create the main application window
    root = tk.Tk()

    # Initialize the Booking App
    app = BookingApp(root)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()
