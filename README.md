# Computer Force (Django) — Assessment Website

Computer Force is a Django-based website built for the course case study/specification.  
It includes a Home page, Products page, Registration page, and About page, with a responsive layout and static assets (CSS, images, JS).

---

## Tech Stack

- **Python 3.x**
- **Django 4.x / 5.x** (project is compatible with standard Django versions)
- HTML + CSS + JavaScript
- Django Templates
- Django Static Files

---

## Project Features (as implemented)

- **Header + Menu bar** with navigation links
- **Search form** (submits a query string to the products page)
- **Purchases sidebar** on desktop (80/20 layout)
- **Mobile responsive behavior**:
  - Burger button toggles mobile menu
  - Bag button opens purchases drawer
- Static UI pages: Home, Products, Register, About

> Note: The “Purchases” section displays test items for layout demonstration (per the wireframe).

---

## Getting Started (Local Setup)

### 1) Clone the project
```bash
git clone <YOUR_REPO_URL>
cd <YOUR_PROJECT_FOLDER>
2) Create and activate a virtual environment
Windows (PowerShell)

python -m venv .venv
. .venv\Scripts\Activate.ps1
macOS / Linux

python3 -m venv .venv
source .venv/bin/activate
3) Install dependencies
pip install -r requirements.txt
If your project does not include requirements.txt, install Django directly:

pip install django
4) Run migrations (safe even if no DB features are used)
python manage.py migrate
5) Run the server
python manage.py runserver
Open in browser:

http://127.0.0.1:8000/

Pages / Routes
Typical routes included in this project:

/ → Home

/products/ → Products listing / categories

/accounts/register/ (or similar) → Register

/about/ → About

Routes may vary slightly depending on your urls.py. The navigation menu uses Django {% url %} tags.

Static Files (CSS/JS/Images)
This project uses Django’s static files system.

Key files:

static/css/styles.css

static/js/site.js

static/img/ (category images, logo, etc.)

During development (runserver), Django serves static files automatically.

If needed, ensure:

STATIC_URL = "static/" exists in settings.py

INSTALLED_APPS includes "django.contrib.staticfiles"

Troubleshooting
Static files not updating (CSS changes not visible)
Hard refresh the browser:

Windows: Ctrl + F5

macOS: Cmd + Shift + R

Ensure the file is correctly linked in base.html:

<link rel="stylesheet" href="{% static 'css/styles.css' %}">
Confirm the browser is loading your CSS:

Open DevTools → Network tab → reload → click styles.css and verify it is the latest version.

Server won’t start / Module not found
Make sure the virtual environment is activated and dependencies are installed:

pip install -r requirements.txt
python manage.py runserver
Port already in use
Run on another port:

python manage.py runserver 8001
Then open:

http://127.0.0.1:8001/

Folder Structure (Typical)
project-root/
├─ manage.py
├─ <project_name>/
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py / asgi.py
├─ core/ (or main app)
│  ├─ templates/
│  └─ views.py
├─ static/
│  ├─ css/styles.css
│  ├─ js/site.js
│  └─ img/
└─ requirements.txt
Notes for Assessment Marking
Layout follows the wireframe requirement:

Desktop: main content + purchases sidebar (80/20)

Mobile: burger menu + purchases drawer

UI components are built with reusable base template (base.html)

Clean typography using Google Fonts (Inter)

Author
© 2026 Adrian Posada
