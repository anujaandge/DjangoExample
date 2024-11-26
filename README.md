# DjangoExample

# Mayinsoft.com

**Mayinsoft.com** is an eCommerce platform built using Django. The application provides a user-friendly shopping experience, featuring intuitive navigation, real-time order tracking, and seamless checkout functionality.

---

## Features

### General
- **Dynamic Views**:  
  Includes an index page, about, contact, search, product view, tracker, and checkout pages.
- **Responsive Design**:  
  Mobile-friendly and optimized layout with Bootstrap.

### Core Functionalities
1. **Flash Sale Carousel**:  
   - Displays recommended items by category.  
   - Quick add-to-cart feature with `localStorage` for cart management.  

2. **Search Functionality**:  
   - Dynamic search with suggestions for related terms.  
   - Typing "Books" shows all items related to "Book".

3. **Order Tracker**:  
   - JSON-based order tracking.  
   - Fetches and displays real-time updates from the `OrderUpdate` model.  

4. **Email Notifications**:  
   - Sends confirmation emails to users for contact submissions.  
   - Admin notifications for contact messages and inquiries.  

5. **Contact Form**:  
   - Captures user inquiries and feedback.  
   - Sends email responses automatically to both the admin and the user.

---

## Tech Stack

### Languages
- **Python 3.x**  
- **HTML, CSS, Bootstrap**

### Frameworks and Libraries
- **Django**: Backend development and template rendering.  
- **JavaScript**: LocalStorage cart functionality and dynamic search behavior.  

### Tools and Databases
- **MySQL**: Database management.  
- **Postman**: API testing.  
- **VSCode**: Development environment.

---

## Models

### `OrderUpdate`
Used for managing and retrieving real-time updates on customer orders. Each update is logged with details, such as order ID, timestamp, and description.

---

## Setup Instructions

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/Mayinsoft.com.git
   cd Mayinsoft.com

2. **Create a Virtual Environment**  
   Create and activate a virtual environment:  

   - On macOS/Linux:  
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```

   - On Windows:  
     ```bash
     python -m venv env
     env\Scripts\activate
     ```
3. **Install Dependencies**  
   Install the required dependencies from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
4. **Setup Database**  
   Apply database migrations to create the required tables:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
5. **Create a Superuser**
   Create an admin account to manage the application:
   ```bash
   python manage.py createsuperuser

6. **Run the Development Server**
   Start the Django development server:
   ```bash
   python manage.py runserver
7. **Access the Application**
   Open your browser and navigate to the application:
   ```bash
   http://127.0.0.1:8000/
8. **Admin Panel**
   Access the admin panel to manage the application backend:
   ```bash
    http://127.0.0.1:8000/admin
  Use the superuser credentials created in Step 5.  
