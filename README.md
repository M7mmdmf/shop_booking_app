# Shopping and Booking Application

## Identifying Information
- **Name**: Mohammad Falaknaz  
- **P-Number**: P338126  
- **Course Code**: IY499  

---

## Declaration of Own Work
I confirm that this assignment is my own work. Where I have referred to online sources, I have provided comments detailing the reference and included a link to the source.

---

## Program Description
This is a **Shopping and Booking Application** that allows users to book appointments at luxury shops across multiple locations in the Middle East. Users can select shops visually via logos, choose available time slots, and specify the location for their booking. The application includes:
- User authentication via **Sign Up** and **Sign In**.
- Dynamic filtering of shops and locations based on user selection.
- A visually rich interface with shop logos and dynamically updated information.
- Booking management with options to submit, view, and search bookings.
- Comprehensive input validation for a smooth and error-free experience.

This program is suitable for luxury service providers looking to streamline appointment booking while offering a seamless user experience.

---

## List of Libraries Used
The following libraries were used in the project:
1. **tkinter**: For GUI creation.
2. **Pillow**: For image handling (shop logos and icons).
3. **csv**: For data storage and retrieval (bookings and user credentials).
4. **os**: For file handling (dynamic loading of assets).
5. **ttk**: For enhanced UI components.

---

## Installation Instructions
1. Clone or download the repository from the provided link.
2. Ensure you have Python 3.7+ installed on your system.
3. Install required libraries by running:
   ```bash
   pip install pillow
4. Place the following assets in their respective directories:
- **shop logos:** Add all shop logos (.png format) in the assets/logos/ directory.
- **Icons:** Ensure icons for submit, search, and view buttons are in assets/.

---

## Running the Program

1. Launch the program by executing the authentication GUI:
    ```bash
    python gui.py
    ```
2. Sign in or sign up to access the main booking interface.
3. Once logged in, you can:
    - **Select Shop**: Choose a shop visually by clicking on its logo. Selected shops are highlighted.
    - **Choose Time Slot**: Select an available time slot dynamically based on the chosen shop.
    - **Select Location**: Choose a location where the shop is available.
    - **Submit Booking**: Save your booking information to the system.
    - **View All Bookings**: Display all submitted bookings in a sorted order.
    - **Search Bookings**: Find bookings associated with your account automatically.

---

## Features

1. **Dynamic Filtering**: Locations and time slots adjust dynamically based on the shop selected and vice versa.
2. **Interactive UI**: Shop logos are displayed in a grid, and clicking a logo selects the shop visually.
3. **User-Friendly Design**: Clean interface with clear navigation and minimal distractions.
4. **Validation**: Comprehensive input validation ensures only correct data is submitted.
5. **Authentication**: Secure user login and registration.

---

## Description of Assets

- **Shop Logos**: PNG files for each shop's logo, resized to 60x60 pixels, located in `assets/logos/`.
- **Icons**: PNG icons for submit, view, and search functionalities located in `assets/`.

---

## Example Bookings

Here are example entries stored in the `bookings.csv` file:

| User Name           | Email              | Phone       | Shop Name         | Booking Time | Location             |
|---------------------|--------------------|-------------|-------------------|--------------|----------------------|
| Mohammad Falaknaz   | test@example.com   | 0501234567  | Chanel Boutique   | 10:00 AM     | Dubai, UAE           |
| Ali Khan            | ali@example.com   | 0507654321  | Gucci Flagship    | 2:00 PM      | Riyadh, Saudi Arabia |

---

## Known Issues

- Missing assets will result in placeholder logos being displayed.
- Users must ensure valid time slots and locations are selected before submitting.
