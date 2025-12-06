Bookeat is a restaurant reservation web application

Setup:
1 Create virtual environment with Python 3.10+
python -m venv venv
.\venv\Scripts\activate
2 pip install -r requirements.txt
3 python manage.py makemigrations
4 python manage.py migrate
5 python manage.py loaddata fixtures/initial_data.json
6 python manage.py runserver

Notes:
This is a local web app focusing on:
Homepage with three restaurants (Yaponamama, B&B, Giotto)
Restaurant detail pages showing up to 10 meals
Reservation create/edit/delete and a reservations list
Register and login
Selecting meals during reservation


SuperUser password and login:
Zarina 
Zarina123
