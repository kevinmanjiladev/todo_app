# 🧠 To-Do Web App (Built with Django)

Hey there! 👋  
This is a simple yet powerful **To-Do web application** I built using **Django**.  
It helps users stay organized by adding, editing, and managing daily tasks — all in a clean blue-and-white themed interface.  

---

## ✨ What You Can Do

- 🧍 Create your own account (Register/Login)
- ✅ Add new tasks easily  
- 🕓 Edit or delete tasks anytime  
- 🎯 Mark tasks as completed  
- 🔒 Each user gets their own private to-do list  
- 💻 Clean and responsive interface — works beautifully on desktop and mobile

---

## 💡 Why I Built This

I wanted to create something simple but useful — a productivity app that looks good, feels smooth, and helps people get things done.  
It also gave me hands-on experience with **Django’s authentication system**, models, and templates.

---

## ⚙️ Tech Stack

| Layer | Tools Used |
|-------|-------------|
| **Backend** | Django (Python) |
| **Frontend** | HTML, CSS, Bootstrap |
| **Database** | SQLite (default) |
| **Version Control** | Git & GitHub |

---

## 🖼️ Screenshots

![image alt](https://github.com/kevinmanjiladev/todo_app/blob/74b9fa113cace6fc4c4253e4a02176354d7b8524/Login%20Page.jpg)
---

## 🚀 How to Run the Project Locally

If you’d like to try it out yourself, here’s how 👇

### 1️⃣ Clone the repository
```bash
git clone https://github.com/kevinmanjiladev/todo_app.git
cd todo_app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

