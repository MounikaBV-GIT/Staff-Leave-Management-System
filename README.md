# Staff Leave Management System (SLMS)

A web-based **Staff Leave Management System** built using Python and Django to simplify employee leave applications and administrative leave management. The application allows staff members to apply for leave and track their leave status, while administrators can manage staff members and review leave requests through a centralized interface.

## 📌 Project Overview

Managing staff leave requests manually can be time-consuming and difficult to track. This project provides a simple web application where staff can submit leave requests and administrators can approve or reject them.

The application features a clean, colorful user interface built with HTML and CSS, along with Django's backend functionality for handling users, leave requests, and administrative actions.

## ✨ Features

### 👤 Staff Features
- User registration and login.
- Staff dashboard for accessing leave-management options.
- Apply for leave by specifying the leave type, dates, and reason.
- View submitted leave requests and their current status.
- Track whether a leave request is pending, approved, or rejected.

### 🛡️ Admin Features
- Admin dashboard for managing leave requests.
- View leave applications submitted by staff.
- Approve or reject pending leave requests.
- Manage staff records.
- Add and edit staff information.
- Review leave request details, including staff names, leave types, dates, and reasons.

### 🎨 User Interface
- Colorful and consistent styling using CSS.
- Responsive layouts for improved usability across screen sizes.
- Styled forms, buttons, navigation links, and tables.
- Color-coded leave statuses:
  - 🟢 Approved
  - 🔴 Rejected
  - 🟠 Pending

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework and application logic |
| HTML5 | Page structure |
| CSS3 | Styling and responsive design |
| SQLite | Database for local development |
| Git and GitHub | Version control and project hosting |

## 📂 Project Structure

```text
slmsproject/
├── leave/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── slmsproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
│   └── css/
│       └── style.css
├── templates/
│   ├── Home.html
│   ├── login.html
│   ├── register.html
│   ├── admin_dashboard.html
│   ├── staff_dashboard.html
│   ├── apply_leave.html
│   ├── my_leave.html
│   ├── view_leaves.html
│   ├── manage_staff.html
│   ├── add_staff.html
│   └── edit_staff.html
├── .gitignore
├── manage.py
└── requirements.txt
```

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the repository

Replace `YOUR_USERNAME` with your GitHub username and `YOUR_REPOSITORY` with your repository name.

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

### 2. Navigate to the project directory

```bash
cd slmsproject
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux or macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create an administrator account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin username and password.

### 8. Start the development server

```bash
python manage.py runserver
```

### 9. Open the application

Visit the following URL in your browser:

http://127.0.0.1:8000/

The exact routes available depend on the project's URL configuration.

## 🚀 How to Use

1. Start the Django development server.
2. Open the application in your browser.
3. Register a staff account or log in with an existing account.
4. Staff members can submit leave applications and check their leave status.
5. Administrators can log in to manage staff and review leave requests.
6. Administrators can approve or reject pending requests.
7. Staff members can check the updated status of their applications.

## 🔐 Security Considerations

- Django's authentication system can be used to manage user accounts.
- CSRF protection should be enabled for form submissions.
- Administrative views should be restricted to authorized users.
- Secret keys and environment-specific credentials should not be committed to GitHub.
- Debug mode should be disabled when deploying the application to production.

## 🔮 Future Enhancements

- Email notifications when leave requests are approved or rejected.
- Leave balance tracking for each staff member.
- Search, filtering, and pagination for leave records.
- Calendar-based leave visualization.
- Export leave reports to Excel or PDF.
- Improved role-based permissions and reporting.
- Cloud deployment for online access.

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Building web applications using Python and Django.
- Creating and managing database models.
- Implementing user registration and authentication workflows.
- Handling HTML forms and Django templates.
- Performing CRUD operations.
- Managing leave request approval workflows.
- Applying reusable CSS styling to multiple pages.
- Organizing a Django project for version control.

## 👩‍💻 Author

**Mounika BV**

Aspiring Python Developer | Django Developer

GitHub: https://github.com/MounikaBV-GIT

---

*This project was developed as a practical web application to streamline staff leave management and strengthen full-stack development skills using Django.*