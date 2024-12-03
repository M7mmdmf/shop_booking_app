from constants import EMAIL_FROM, EMAIL_SUBJECT_TEMPLATE, SUCCESS_MESSAGES

def send_email_simulation(email: str, booking_details: dict):
    """
    Simulates sending a confirmation email.

    Args:
        email (str): The recipient's email address.
        booking_details (dict): A dictionary containing booking details.
    
    Returns:
        str: A success message indicating the email was sent.
    """
    try:
        # Extract booking details
        shop_name = booking_details.get("shop_name", "Unknown Shop")
        booking_time = booking_details.get("booking_time", "Unknown Time")
        location = booking_details.get("location", "Unknown Location")
        user_name = booking_details.get("user_name", "Valued Customer")

        # Construct email content
        email_subject = EMAIL_SUBJECT_TEMPLATE.format(shop_name=shop_name)
        email_body = f"""
        Dear {user_name},

        Thank you for booking an appointment with {shop_name}.
        Here are your booking details:

        Shop Name: {shop_name}
        Booking Time: {booking_time}
        Location: {location}

        If you have any questions or need to modify your booking, please contact us.

        Best regards,
        The Luxury App Team
        """
        # Simulate sending email by printing to console
        print("=" * 50)
        print(f"From: {EMAIL_FROM}")
        print(f"To: {email}")
        print(f"Subject: {email_subject}")
        print(email_body)
        print("=" * 50)

        # Return success message
        return SUCCESS_MESSAGES["email_sent"].format(email=email)
    except Exception as e:
        # Handle unexpected errors
        print(f"Error simulating email: {e}")
        return "Failed to send email. Please try again."
