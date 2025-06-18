# Django Blog App

A fully functional blog platform built with **Django** and **Bootstrap**, allowing users to create, update, and delete blog posts. It also supports **user registration, login, and profile management**. Blogs are categorized by topics such as **Technology**, **Lifestyle**, etc., and each user can view and manage only their own posts through their profile.

---

## Features

-  User Registration and Login (Authentication & Authorization)
-  Create, Read, Update, Delete (CRUD) operations for blogs
-  Blog categories: Technology, Lifestyle, Travel, and more
-  User profile with:
  - Filtered blog view (only user's posts)
  - Profile details
-  Bootstrap UI for responsive design
-  Access control to restrict blog management to post owners

##  Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default, easy setup)
- **Authentication**: Django Auth System

---

## Getting Started

### 1. Clone the repository

```bash```
git clone https://github.com/Ermi24et/blog_app.git
cd blog_app

### 2. Set up a virtual environment
python -m venv env
source env/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Apply migrations
python manage.py makemigrations
python manage.py migrate

### 5. Create a superuser
python manage.py createsuperuser

### 6. Run the development server
python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser.

## Usage

Home Page: See some blogs.

Categories: Filter blogs by category.

Login/Signup: Access your account.

Profile: View and manage your own posts.

Create Blog: Available after login.

Edit/Delete: Only available for the post owner.

## Contributing
Contributions are welcome! Feel free to fork this repo and submit a pull request.

## Contact
If you have any questions or feedback, feel free to reach out at [lilermi24@gmail.com].

