# restaurant_project — Mata Pita Da Dhaba
Starter Django + DRF project for a local restaurant. Pages: Home, Menu, Reservation, Contact.
## Quick start
1. python -m venv venv
2. source venv/bin/activate   (or venv\Scripts\activate on Windows)
3. pip install -r requirements.txt
4. cp .env.example .env
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py createsuperuser
8. python manage.py runserver
- Admin: /admin  — add MenuItem entries and manage reservations
- API: /api/menu/  /api/reservations/
- Frontend: http://127.0.0.1:8000/
