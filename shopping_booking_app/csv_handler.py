import csv
from typing import List, Dict
from constants import CSV_FILE_PATH, ERROR_MESSAGES

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
        List[Dict[str, str]]: List of bookings as dictionaries.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
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
