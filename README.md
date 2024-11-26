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
