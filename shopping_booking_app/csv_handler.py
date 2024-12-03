import csv
import os
import hashlib
from typing import List, Dict
from constants import CSV_FILE_PATH, ERROR_MESSAGES

# File paths for storing data
USERS_CSV_FILE = "data/users.csv"

# Booking CSV Functions
def initialize_csv(file_path: str = CSV_FILE_PATH):
    """
    Initializes the CSV file with headers if it doesn't exist.
    """
    try:
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if file.tell() == 0:  # File is empty, add headers
                writer.writerow(["User Name", "Email", "Phone", "Shop Name", "Booking Time", "Location"])
    except Exception as e:
        print(f"Error initializing CSV file: {e}")


def save_booking(data: Dict[str, str], file_path: str = CSV_FILE_PATH):
    """
    Saves a new booking to the CSV file.

    Args:
        data (dict): Dictionary containing booking details.
        file_path (str): Path to the CSV file.
    """
    try:
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                data.get("user_name"),
                data.get("email"),
                data.get("phone"),
                data.get("shop_name"),
                data.get("booking_time"),
                data.get("location")
            ])
    except Exception as e:
        print(f"Error saving booking: {e}")
        raise ValueError(ERROR_MESSAGES["csv_error"])


def read_all_bookings(file_path: str = CSV_FILE_PATH) -> List[Dict[str, str]]:
    """
    Reads all bookings from the CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        List[Dict[str, str]]: List of all bookings.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            print("DEBUG: Read bookings:", data)  # Debugging line
            return data
    except Exception as e:
        print(f"Error reading bookings: {e}")
        raise ValueError(ERROR_MESSAGES["csv_error"])


def search_bookings(query: str, field: str, file_path: str = CSV_FILE_PATH) -> List[Dict[str, str]]:
    """
    Searches bookings based on a query in a specific field.

    Args:
        query (str): The search query.
        field (str): The field to search (e.g., 'Email', 'Shop Name').
        file_path (str): Path to the CSV file.

    Returns:
        List[Dict[str, str]]: List of matching bookings.
    """
    try:
        bookings = read_all_bookings(file_path)
        return [booking for booking in bookings if query.lower() in booking.get(field, "").lower()]
    except Exception as e:
        print(f"Error searching bookings: {e}")
        raise ValueError(ERROR_MESSAGES["csv_error"])


def sort_bookings(field: str, descending: bool = False, file_path: str = CSV_FILE_PATH) -> List[Dict[str, str]]:
    """
    Sorts bookings based on a specific field.

    Args:
        field (str): The field to sort by (e.g., 'Booking Time', 'Shop Name').
        descending (bool): Whether to sort in descending order.
        file_path (str): Path to the CSV file.

    Returns:
        List[Dict[str, str]]: List of sorted bookings.
    """
    try:
        bookings = read_all_bookings(file_path)
        return sorted(bookings, key=lambda x: x.get(field, ""), reverse=descending)
    except Exception as e:
        print(f"Error sorting bookings: {e}")
        raise ValueError(ERROR_MESSAGES["csv_error"])


# User Management Functions
def initialize_users_csv():
    """
    Initializes the users.csv file with headers if it doesn't exist.
    """
    if not os.path.exists(USERS_CSV_FILE):
        with open(USERS_CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if file.tell() == 0:  # File is empty, add headers
                writer.writerow(["Username", "Email", "Password"])


def hash_password(password: str) -> str:
    """
    Hashes a password using SHA-256.

    Args:
        password (str): The plain text password.

    Returns:
        str: The hashed password.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def save_user(username: str, email: str, password: str):
    """
    Saves a new user to the users.csv file.

    Args:
        username (str): The username.
        email (str): The user's email.
        password (str): The plain text password.
    """
    initialize_users_csv()
    hashed_password = hash_password(password)
    with open(USERS_CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([username, email, hashed_password])


def authenticate_user(identifier: str, password: str) -> bool:
    """
    Authenticates a user by username/email and password.

    Args:
        identifier (str): The username or email.
        password (str): The plain text password.

    Returns:
        bool: True if authentication is successful, False otherwise.
    """
    initialize_users_csv()
    hashed_password = hash_password(password)
    with open(USERS_CSV_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if (row["Username"] == identifier or row["Email"] == identifier) and row["Password"] == hashed_password:
                return True
    return False


def is_user_registered(username: str, email: str) -> bool:
    """
    Checks if a username or email is already registered.

    Args:
        username (str): The username to check.
        email (str): The email to check.

    Returns:
        bool: True if the user is already registered, False otherwise.
    """
    initialize_users_csv()
    with open(USERS_CSV_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Username"] == username or row["Email"] == email:
                return True
    return False
