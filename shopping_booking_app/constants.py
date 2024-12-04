# File paths
CSV_FILE_PATH = "data/bookings.csv"  # Path to the CSV file storing booking data
ASSETS_PATH = "assets/"  # Path to the assets folder

# Application settings
WINDOW_TITLE = "Shopping and Booking App"
WINDOW_SIZE = "800x600"
BACKGROUND_COLOR = "#f7f7f7"  # Light gray background for the GUI

# Predefined luxury shop names and their multiple locations
LUXURY_SHOPS = {
    "Chanel Boutique": ["Dubai, UAE", "Riyadh, Saudi Arabia", "Doha, Qatar", "Cairo, Egypt"],
    "Louis Vuitton Store": ["Abu Dhabi, UAE", "Jeddah, Saudi Arabia", "Manama, Bahrain", "Kuwait City, Kuwait"],
    "Gucci Flagship": ["Dubai, UAE", "Muscat, Oman", "Beirut, Lebanon", "Alexandria, Egypt"],
    "Hermès Outlet": ["Riyadh, Saudi Arabia", "Doha, Qatar", "Sharjah, UAE", "Amman, Jordan"],
    "Prada Store": ["Dubai, UAE", "Abu Dhabi, UAE", "Jeddah, Saudi Arabia", "Cairo, Egypt"],
    "Dior Boutique": ["Manama, Bahrain", "Doha, Qatar", "Kuwait City, Kuwait", "Erbil, Iraq"],
    "Versace Collection": ["Dubai, UAE", "Damascus, Syria", "Basra, Iraq", "Muscat, Oman"],
    "Fendi Store": ["Riyadh, Saudi Arabia", "Sharjah, UAE", "Beirut, Lebanon", "Al Khobar, Saudi Arabia"],
    "Dolce & Gabbana": ["Dubai, UAE", "Jeddah, Saudi Arabia", "Manama, Bahrain", "Cairo, Egypt"],
    "Burberry Shop": ["Doha, Qatar", "Abu Dhabi, UAE", "Kuwait City, Kuwait", "Amman, Jordan"],
    "Armani Exchange": ["Dubai, UAE", "Muscat, Oman", "Beirut, Lebanon", "Sharjah, UAE"],
    "Balenciaga Boutique": ["Dubai, UAE", "Riyadh, Saudi Arabia", "Manama, Bahrain", "Erbil, Iraq"],
    "Bottega Veneta": ["Doha, Qatar", "Abu Dhabi, UAE", "Basra, Iraq", "Cairo, Egypt"],
    "Cartier Store": ["Dubai, UAE", "Jeddah, Saudi Arabia", "Alexandria, Egypt", "Al Khobar, Saudi Arabia"],
    "Givenchy Outlet": ["Muscat, Oman", "Riyadh, Saudi Arabia", "Manama, Bahrain", "Damascus, Syria"],
    "Valentino Boutique": ["Dubai, UAE", "Doha, Qatar", "Kuwait City, Kuwait", "Amman, Jordan"],
    "Yves Saint Laurent": ["Beirut, Lebanon", "Sharjah, UAE", "Basra, Iraq", "Cairo, Egypt"],
    "Rolex Showroom": ["Dubai, UAE", "Riyadh, Saudi Arabia", "Abu Dhabi, UAE", "Erbil, Iraq"],
    "Tiffany & Co.": ["Doha, Qatar", "Muscat, Oman", "Manama, Bahrain", "Alexandria, Egypt"],
    "Loro Piana": ["Dubai, UAE", "Riyadh, Saudi Arabia", "Doha, Qatar", "Amman, Jordan"],
    "Michael Kors": ["Abu Dhabi, UAE", "Muscat, Oman", "Cairo, Egypt", "Beirut, Lebanon"],
    "Tom Ford": ["Dubai, UAE", "Riyadh, Saudi Arabia", "Alexandria, Egypt", "Sharjah, UAE"],
    "Salvatore Ferragamo": ["Jeddah, Saudi Arabia", "Doha, Qatar", "Cairo, Egypt", "Erbil, Iraq"],
    "Bvlgari": ["Dubai, UAE", "Abu Dhabi, UAE", "Manama, Bahrain", "Amman, Jordan"],
    "Hugo Boss": ["Muscat, Oman", "Beirut, Lebanon", "Sharjah, UAE", "Cairo, Egypt"],
    "Lacoste": ["Riyadh, Saudi Arabia", "Doha, Qatar", "Kuwait City, Kuwait", "Basra, Iraq"],
    "Ralph Lauren": ["Dubai, UAE", "Abu Dhabi, UAE", "Manama, Bahrain", "Damascus, Syria"],
    "Alexander McQueen": ["Dubai, UAE", "Jeddah, Saudi Arabia", "Beirut, Lebanon", "Amman, Jordan"],
    "Jimmy Choo": ["Dubai, UAE", "Riyadh, Saudi Arabia", "Doha, Qatar", "Cairo, Egypt"],
    "Chopard": ["Muscat, Oman", "Alexandria, Egypt", "Sharjah, UAE", "Basra, Iraq"]
}

SHOP_TIME_SLOTS = {
    "Chanel Boutique": ["10:00 AM", "11:00 AM", "12:00 PM"],
    "Louis Vuitton Store": ["01:00 PM", "02:00 PM", "03:00 PM"],
    "Gucci Flagship": ["10:00 AM", "12:00 PM", "02:00 PM"],
    "Hermès Outlet": ["09:00 AM", "10:00 AM", "11:00 AM"],
    "Prada Store": ["12:00 PM", "01:00 PM", "02:00 PM"],
    "Dior Boutique": ["09:00 AM", "10:00 AM", "11:00 AM"],
    "Versace Collection": ["01:00 PM", "03:00 PM", "05:00 PM"],
    "Fendi Store": ["10:00 AM", "11:00 AM", "12:00 PM"],
    "Dolce & Gabbana": ["09:00 AM", "10:00 AM", "11:00 AM"],
    "Burberry Shop": ["12:00 PM", "01:00 PM", "02:00 PM"],
    "Armani Exchange": ["01:00 PM", "02:00 PM", "03:00 PM"],
    "Balenciaga Boutique": ["10:00 AM", "12:00 PM", "02:00 PM"],
    "Bottega Veneta": ["09:00 AM", "11:00 AM", "01:00 PM"],
    "Cartier Store": ["12:00 PM", "01:00 PM", "02:00 PM"],
    "Givenchy Outlet": ["10:00 AM", "11:00 AM", "12:00 PM"],
    "Valentino Boutique": ["09:00 AM", "10:00 AM", "11:00 AM"],
    "Yves Saint Laurent": ["01:00 PM", "02:00 PM", "03:00 PM"],
    "Rolex Showroom": ["09:00 AM", "11:00 AM", "01:00 PM"],
    "Tiffany & Co.": ["10:00 AM", "11:00 AM", "12:00 PM"],
    "Loro Piana": ["01:00 PM", "03:00 PM", "05:00 PM"],
    "Michael Kors": ["09:00 AM", "10:00 AM", "11:00 AM"],
    "Tom Ford": ["10:00 AM", "12:00 PM", "02:00 PM"],
    "Salvatore Ferragamo": ["09:00 AM", "10:00 AM", "11:00 AM"],
    "Bvlgari": ["12:00 PM", "01:00 PM", "02:00 PM"],
    "Hugo Boss": ["01:00 PM", "03:00 PM", "05:00 PM"],
    "Lacoste": ["10:00 AM", "12:00 PM", "02:00 PM"],
    "Ralph Lauren": ["09:00 AM", "10:00 AM", "11:00 AM"],
    "Alexander McQueen": ["12:00 PM", "01:00 PM", "02:00 PM"],
    "Jimmy Choo": ["01:00 PM", "02:00 PM", "03:00 PM"],
    "Chopard": ["10:00 AM", "11:00 AM", "12:00 PM"]
}



# Predefined shop locations (unique locations extracted dynamically)
SHOP_LOCATIONS = list(set(location for locations in LUXURY_SHOPS.values() for location in locations))

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
