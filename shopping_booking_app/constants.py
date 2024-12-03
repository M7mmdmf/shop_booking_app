# File paths
CSV_FILE_PATH = "data/bookings.csv"  # Path to the CSV file storing booking data
ASSETS_PATH = "assets/"  # Path to the assets folder

# Application settings
WINDOW_TITLE = "Shopping and Booking App"
WINDOW_SIZE = "600x600"
BACKGROUND_COLOR = "#f7f7f7"  # Light gray background for the GUI

# Predefined luxury shop names
LUXURY_SHOPS = [
    "Luxury Boutique Dubai",
    "Premium Store Riyadh",
    "Elite Fashion Doha",
    "Chic Emporium Abu Dhabi",
    "Lavish Styles Manama"
]

# Predefined shop locations in the Middle East
SHOP_LOCATIONS = [
    "Dubai",
    "Riyadh",
    "Doha",
    "Abu Dhabi",
    "Manama"
]

# Email simulation settings
EMAIL_FROM = "noreply@luxuryapp.com"
EMAIL_SUBJECT_TEMPLATE = "Booking Confirmation for {shop_name}"

# Error messages
ERROR_MESSAGES = {
    "empty_field": "All fields must be filled out.",
    "invalid_email": "Invalid email address. Please enter a valid email.",
    "invalid_phone": "Invalid phone number. Please enter a valid phone number.",
    "invalid_time": "Invalid booking time. Please use HH:MM AM/PM format.",
    "invalid_location": "Please select a valid location.",
    "csv_error": "Error accessing the CSV file. Please try again later."
}

# Success messages
SUCCESS_MESSAGES = {
    "booking_successful": "Booking successful! A confirmation email has been sent.",
    "email_sent": "Confirmation email sent to {email}."
}

# Time format (24-hour or AM/PM)
TIME_FORMAT = "AM/PM"
