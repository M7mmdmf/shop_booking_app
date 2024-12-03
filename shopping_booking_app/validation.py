import re
from constants import ERROR_MESSAGES, SHOP_LOCATIONS, LUXURY_SHOPS

def validate_email(email: str) -> bool:
    """
    Validates an email address format.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(email_regex, email):
        return True
    return False

def validate_phone(phone: str) -> bool:
    """
    Validates a phone number format.
    
    Args:
        phone (str): The phone number to validate.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    phone_regex = r"^\d{8,15}$"  # 8 to 15 digits
    if re.match(phone_regex, phone):
        return True
    return False

def validate_booking_time(time: str) -> bool:
    """
    Validates the booking time format.
    
    Args:
        time (str): The booking time to validate (e.g., "10:00 AM").
    
    Returns:
        bool: True if valid, False otherwise.
    """
    time_regex = r"^(0[1-9]|1[0-2]):[0-5][0-9] (AM|PM)$"  # Format: HH:MM AM/PM
    if re.match(time_regex, time):
        return True
    return False

def validate_shop_location(location: str) -> bool:
    """
    Validates if the shop location is in the predefined list of locations.
    
    Args:
        location (str): The shop location to validate.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    if location in SHOP_LOCATIONS:
        return True
    return False

def validate_shop_name(shop_name: str) -> bool:
    """
    Validates if the shop name is in the predefined list of shop names.
    
    Args:
        shop_name (str): The shop name to validate.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    if shop_name in LUXURY_SHOPS:
        return True
    return False

def validate_all_fields(email: str, phone: str, time: str, location: str, shop_name: str) -> str:
    """
    Validates all user inputs.

    Args:
        email (str): User's email address.
        phone (str): User's phone number.
        time (str): Booking time.
        location (str): Shop location.
        shop_name (str): Shop name.

    Returns:
        str: Error message if validation fails, or an empty string if all inputs are valid.
    """
    if not email or not validate_email(email):
        return ERROR_MESSAGES["invalid_email"]
    if not phone or not validate_phone(phone):
        return ERROR_MESSAGES["invalid_phone"]
    if not time or not validate_booking_time(time):
        return ERROR_MESSAGES["invalid_time"]
    if not location or not validate_shop_location(location):
        return ERROR_MESSAGES["invalid_location"]
    if not shop_name or not validate_shop_name(shop_name):
        return ERROR_MESSAGES["empty_field"]
    return ""  # All fields are valid
