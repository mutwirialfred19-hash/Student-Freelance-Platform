# KCA Talent Hub — Student Freelancing Platform

## Quick Start
```bash
pip install django pillow
python manage.py migrate
python manage.py runserver
```
Open: http://127.0.0.1:8000
Admin: http://127.0.0.1:8000/admin/

## Admin Login
- Username: admin
- Password: kca2024!  ← CHANGE THIS!

## First Steps in Admin
1. Go to /admin/ → Categories → Add Category
   Add categories like:
   - 💻 Web Development (slug: web-development)
   - 🎨 Graphic Design (slug: graphic-design)
   - 💇‍♀️ Hairdressing (slug: hairdressing)
   - 💅 Nail Art (slug: nail-art)
   - 💆‍♀️ Massage Therapy (slug: massage-therapy)
   - 🍽️ Hospitality (slug: hospitality)
   - 📚 Tutoring (slug: tutoring)
   - 📸 Photography (slug: photography)

2. Students register at /accounts/register/student/
   (MUST use KCA email: number@students.kcau.ac.ke)

3. Clients register at /accounts/register/client/
   (Any email works for clients)

## Pages
- / — Homepage with hero, categories, projects
- /projects/ — Browse all open projects
- /projects/<id>/ — Project detail + proposal form
- /projects/post/ — Post a project (clients only)
- /dashboard/ — Student or client dashboard
- /accounts/register/student/ — Student signup
- /accounts/register/client/ — Client signup
- /accounts/login/ — Login
- /admin/ — Full admin panel
