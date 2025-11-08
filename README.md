# TinyLink - URL Shortener

A modern, scalable URL shortener built with Django that allows you to create short, memorable links from long URLs. Perfect for sharing links on social media, in messages, or anywhere space is limited.<br/>

<style> 
 img { border: 2px solid #e1e5e9; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06); transition: all 0.3s ease; margin: 10px 0; } 
 img:hover { border-color: #3b82f6; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); transform: translateY(-2px); } 
</style>

<img width="1631" height="858" alt="project_run" src="https://github.com/user-attachments/assets/f3a25f9a-f09a-4910-87ed-ffc4bca18dd6" />
<img width="1627" height="862" alt="project_run1" src="https://github.com/user-attachments/assets/5e026046-580b-42f4-9e4e-cd2200358949" />


## 🚀 How to Get and Run the Project

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git


### Installation & Setup
1. **Clone the repository**
```bash
git clone https://github.com/sinakaramiyan/Link-Shortener.git
cd tinylink
```

2. **Clone the repository**
```
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate 
```

3. **Install Dependencies**
```
pip install -r requirements.txt
```

4. **Configure environment variables**
Edit .env with your settings:
```
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

5. **Run migrations**
```
python manage.py makemigrations
python manage.py migrate
```

6. **python manage.py createsuperuser**
```
python manage.py createsuperuser
```

7. **Run the development server**
```
python manage.py runserver
```

8. **Access the application**
 - Main app: http://localhost:8000
 - Admin panel: http://localhost:8000/admin


# 🏗️ Project Description

## Technical Stack

- **Django 4.2+** - High-level Python web framework
- **Tailwind CSS** - Modern utility-first CSS framework
- **PostgreSQL** - Database support
- **Class-Based Views** - Clean, reusable view architecture
- **Template seperation** 

## Architecture & Design Principles

### 🧹 Clean Code

- **PEP 8 Compliance** - Consistent Python code style
- **Modular Structure** - Well-organized app architecture
- **Comprehensive Documentation** - Clear code comments and docstrings
- **Type Hints** - Better code readability and IDE support

### 📈 Scalable Architecture

- **Database Abstraction** - Easy migration between PostgreSQL

### 🎯 Separation of Concerns

- **MVC Pattern** - Models, Views, Templates separation
- **Business Logic** - Clean separation from presentation layer
- **Data Access Layer** - Abstracted database operations

# ✨ Key Features

## 🔗 Core Functionality

- **Instant URL Shortening** - Convert long URLs to short codes in real-time

## 🎨 Modern UI/UX

- **Responsive Design** - Works perfectly on all devices
- **Design** - Modern design elements

# 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
