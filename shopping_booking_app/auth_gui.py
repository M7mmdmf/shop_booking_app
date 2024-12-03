import tkinter as tk
from tkinter import messagebox
from csv_handler import save_user, authenticate_user, is_user_registered


class AuthApp:
    def __init__(self, root, on_success):
        """
        Initializes the Sign Up / Sign In interface.

        Args:
            root: The root Tkinter window.
            on_success: A callback function to launch the main application after a successful login.
        """
        self.root = root
        self.root.title("Sign Up / Sign In")
        self.root.geometry("400x300")
        self.root.configure(bg="#f7f7f7")
        self.on_success = on_success

        self.username = tk.StringVar()
        self.email = tk.StringVar()
        self.password = tk.StringVar()

        # Create the widgets
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Welcome!", font=("Arial", 16), bg="#f7f7f7").pack(pady=10)

        frame = tk.Frame(self.root, bg="#f7f7f7")
        frame.pack(pady=10)

        # Username Entry
        tk.Label(frame, text="Username:", bg="#f7f7f7").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(frame, textvariable=self.username).grid(row=0, column=1, padx=5, pady=5)

        # Email Entry
        tk.Label(frame, text="Email:", bg="#f7f7f7").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(frame, textvariable=self.email).grid(row=1, column=1, padx=5, pady=5)

        # Password Entry
        tk.Label(frame, text="Password:", bg="#f7f7f7").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(frame, textvariable=self.password, show="*").grid(row=2, column=1, padx=5, pady=5)

        # Buttons
        tk.Button(self.root, text="Sign Up", command=self.sign_up, bg="#4caf50", fg="white").pack(pady=10)
        tk.Button(self.root, text="Sign In", command=self.sign_in, bg="#2196f3", fg="white").pack(pady=10)

    def sign_up(self):
        username = self.username.get().strip()
        email = self.email.get().strip()
        password = self.password.get().strip()

        if not username or not email or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        if is_user_registered(username, email):
            messagebox.showerror("Error", "Username or email already registered!")
            return

        save_user(username, email, password)
        messagebox.showinfo("Success", "Sign Up successful! You can now sign in.")
        self.clear_fields()

    def sign_in(self):
        identifier = self.username.get().strip()  # Username or email
        password = self.password.get().strip()

        if not identifier or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        if authenticate_user(identifier, password):
            messagebox.showinfo("Success", "Sign In successful!")
            self.root.destroy()  # Close the auth window
            self.on_success()  # Launch the main application
        else:
            messagebox.showerror("Error", "Invalid username/email or password!")

    def clear_fields(self):
        """Clears the input fields."""
        self.username.set("")
        self.email.set("")
        self.password.set("")
