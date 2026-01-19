# 🚀 StarNet: Cosmic Task Manager

![Project Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Framework](https://img.shields.io/badge/Django-4.2.7-092E20?logo=django)
![Theme](https://img.shields.io/badge/Theme-Cosmic%20Hyper--Glass-bc13fe)

**StarNet** is a next-generation Task & Project Management solution built with Django. It features a stunning **"Cosmic Hyper-Glass"** premium UI/UX, combining deep galactic aesthetics with modern glassmorphism to create an immersive productivity environment.

## ✨ Key Features

### 🎨 Ultra-Premium UI/UX
*   **Cosmic Hyper-Glass Theme**: A deep dark mode with neon accents (`Cyan`, `Violet`, `Emerald`) and advanced glassmorphism.
*   **Interactive Animations**: Smooth transitions, floating elements, and 3D hover effects.
*   **Responsive Design**: Fully optimized for all devices with a futuristic, app-like feel.

### 🛠 Core Functionality
*   **Project Management**: Create, track, and manage complex projects with start/end dates and team assignments.
*   **Task Tracking**: Advanced task lifecycle management (To Do -> In Progress -> Done) with priority levels (Low, Medium, High, Urgent).
*   **Role-Based Access**: Granular permissions for **Managers** (create/assign) and **Standard Users** (view/update).
*   **User Dashboard**: Real-time statistics, recent activity feed, and personal task views.
*   **Team Collaboration**: Assign tasks to specific members and track team progress.

### ⚙️ Technical Highlights
*   **Backend**: Python, Django 4.2, Django ORM.
*   **Frontend**: HTML5, CSS3 (Custom Variables + Animations), JavaScript, Bootstrap 5.
*   **Forms**: Enhanced with `django-crispy-forms` for beautiful, accessible inputs.
*   **Background Tasks**: Integrated **Celery & Redis** support for asynchronous processing.

---

## 📸 Screenshots

| Dashboard | Project View |
|:---:|:---:|
| *Futuristic stats overview with neon charts* | *Clean, glass-panel project details & team lists* |

---

## 🚀 Installation Guide

Follow these steps to deploy StarNet locally:

### 1. Clone the Repository
```bash
git clone https://github.com/BadrECT/Web_App_Paython.git
cd Web_App_Paython
```

### 2. Set Up Virtual Environment
It's recommended to use a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database
Apply migrations to set up the database schema:
```bash
python manage.py migrate
```

### 5. Create Admin User
```bash
python manage.py createsuperuser
```

### 6. Run the Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000` in your browser.

---

## 📂 Project Structure

```
Web_App_Paython/
├── manage.py            # Django CLI utility
├── requirements.txt     # Python dependencies
├── templates/           # Global templates (base.html)
├── static/              # Static assets (CSS, JS, Images)
├── task_manager/        # Main project configuration settings
├── users/               # Authentication & Profile management
└── tasks/               # Core project & task logic app
```

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a Pull Request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📧 Contact

**BadrECT** - [badrkaanoune005@gmail.com](mailto:badrkaanoune005@gmail.com)

Project Link: [https://github.com/BadrECT/Web_App_Paython](https://github.com/BadrECT/Web_App_Paython)
