# Django E-commerce Web Application

This project is a Django-based e-commerce platform designed for selling fashion and apparel products. It features a complete user journey from browsing products to placing an order.

## How It Works

The application provides a seamless shopping experience for users:

1.  **Browse Products**: Users can explore various product categories, including discounted items, new arrivals, and specific sections like women's fashion and footwear.
2.  **View Details**: Each product has a dedicated detail page showing more information and similar items.
3.  **Wishlist**: Authenticated users can add or remove items from their personal wishlist.
4.  **Shopping Cart**: Users can add products to their shopping cart (bag), update quantities, and remove items.
5.  **Checkout**: The checkout process allows users to review their cart and place an order.
6.  **Order History**: After placing an order, users can view their complete order history in their account.
7.  **User Account**: Users can register, log in, and manage their account information.

## Key Features

-   **User Authentication**: Secure login, registration, and session management.
-   **Product Management**: Display products with details, discounts, and categories.
-   **Wishlist**: Allows users to save products for later.
-   **Shopping Cart**: A fully functional cart to manage items before purchase.
-   **Order System**: Manages customer orders and history.
-   **Search**: Users can search for products by name or description.

## Setup and Installation

Follow these steps to set up the project locally:

1.  **Create a Virtual Environment**:
    ```bash
    py -m venv venv
    ```

2.  **Activate the Environment**:
    ```bash
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies**:
    *It is recommended to create a `requirements.txt` file. For now, you can install the required packages manually.*
    ```bash
    pip install django pillow python-dotenv
    ```

4.  **Apply Migrations**:
    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser**:
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create an administrator account.

6.  **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.

## Project Structure

The core logic of the application is located in the `my_web_demo` app. This app handles all the views, models, and templates related to products, user accounts, and the shopping workflow.

-   `views.py`: Contains the logic for rendering pages and handling user interactions.
-   `models.py`: Defines the database structure for products, users, orders, etc.
-   `urls.py`: Maps URLs to their corresponding views.
-   `templates/`: Contains the HTML templates for the user interface.