# 🎬 Book Movie Tickets

A full-stack web application that allows users to explore movies and book tickets — inspired by the functionality of **BookMyShow**.

## 📌 Overview

**Book Movie Tickets** is a Django-based web application where users can:

- Browse movies with posters and details
- View showtimes and movie details
- Book tickets for selected showtimes
- Manage their bookings

This project mimics the core features of popular platforms like BookMyShow, providing an intuitive and responsive movie booking experience.

---

## ✨ Features

- 🎞️ **Movie Listings** – Explore all available movies
- 📝 **Movie Details Page** – Description, genre, duration, language, etc.
- 🕒 **Showtime Selection** – Choose from available showtimes
- 🎟️ **Ticket Booking** – Select number of tickets and seats
- 👤 **User Authentication** – Sign up and log in to book tickets
- 📂 **Booking History** – View past ticket bookings (if implemented)

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default, configurable)
- **Version Control:** Git & GitHub

---

## 📁 Folder Structure
book_movie_tickets/
├── movies/ # App for movie-related views and models
├── templates/ # HTML templates
├── static/ # Static files (CSS, JS, images)
├── .env # Environment variables (ignored in Git)
├── db.sqlite3 # Default database
└── manage.py

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/krakesh1309/movie_ticket_.git
cd book_movie_tickets

2. Create and activate a virtual environment (optional but recommended)
bash
Copy code
python -m venv venv
source venv/bin/activate
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Apply migrations
bash
Copy code
python manage.py migrate
5. Run the server
bash
Copy code
python manage.py runserver
Then visit http://localhost:8000 in your browser.

📸 Screenshots
You can add screenshots here later by uploading them to your repo and using:


📄 License
This project is licensed under the MIT License.

🙌 Acknowledgements
Inspired by BookMyShow

Built with Django and ❤️

vbnet
Copy code

Would you like me to create a matching `.env.example` file or help set up the deployment steps for this project?






You said:
modify the REadme file like it is just the ott platform user will come and first register, then login and then he will select movies showtime book ticket, cancel tickets before1hr of show and watch the movies.with all notifications while creating account, booking email, pop mesg successfyll booikng and notifactions for show 


ChatGPT said:
Here is the modified README.md tailored for your OTT-style movie booking and streaming platform, including registration, login, showtime booking, cancellation, notifications, and streaming features:

markdown
Copy code
# 🎥 Book Movie Tickets – OTT Platform

An OTT-style web application where users can **register, book movie showtimes, watch movies**, and manage their bookings — packed with real-time notifications, email alerts, and cancellation policies.

---

## 📌 Overview

**Book Movie Tickets** is a full-stack Django-based OTT platform where users:

- Create an account and log in
- Browse available movies and showtimes
- Book tickets and receive confirmation via email and pop-up messages
- Cancel tickets (up to 1 hour before showtime)
- Watch movies directly within the platform

---

## ✨ Features

- 🔐 **User Registration & Login** – Secure signup and login with form validations
- 📩 **Email Notifications** – On successful registration and booking confirmation
- 📱 **Real-Time Popups & Alerts** – Success messages for booking, cancellation, and actions
- 🎞️ **Movie Browsing** – List of movies with posters, descriptions, and showtimes
- ⏰ **Ticket Booking** – Select movie, showtime, and book instantly
- ❌ **Ticket Cancellation** – Cancel booking if more than 1 hour remains before showtime
- ▶️ **Movie Streaming** – Watch booked movies directly inside the platform (OTT-style)

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Database:** SQLite (configurable to PostgreSQL/MySQL)
- **Email:** Django Email Backend (Console/SMTP)
- **Notifications:** Django messages framework, JavaScript alerts
- **Version Control:** Git & GitHub

---

## 🧭 User Flow

1. **Register** an account with your email and password
2. **Login** securely to access your dashboard
3. **Browse Movies** and pick a showtime
4. **Book Tickets** and receive instant email + popup confirmation
5. **Watch Movie** if booking is successful and showtime is valid
6. **Cancel Tickets** (up to 1 hour before showtime) with notification
7. **Receive Reminders** and real-time status of showtime/events

---

## 📁 Folder Structure

book_movie_tickets/
├── movies/ # App containing views, models, urls
├── templates/ # HTML templates for UI
├── static/ # Static files (CSS, JS, images)
├── media/ # Uploaded content (if any)
├── .env # Environment variables (not tracked)
├── db.sqlite3 # Default database
└── manage.py

yaml
Copy code

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/krakesh1309/movie_ticket_.git
cd book_movie_tickets
2. Set up virtual environment
bash
Copy code
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure .env file
Create a .env file and include necessary variables (like secret keys, email credentials):

env
Copy code
SECRET_KEY=your_secret_key
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_password
5. Run migrations
bash
Copy code
python manage.py migrate
6. Start the development server
bash
Copy code
python manage.py runserver
Visit http://localhost:8000

📸 Screenshots
Add screenshots like registration, booking, email alert, and movie player here.

📝 Future Enhancements
Add online payment gateway

Implement OTP/email verification

Add personalized recommendations

Add ratings and reviews

📄 License
This project is licensed under the MIT License.

🙌 Acknowledgements
Inspired by BookMyShow, Netflix, and Hotstar

Built using Django with ❤️

vbnet
Copy code


















