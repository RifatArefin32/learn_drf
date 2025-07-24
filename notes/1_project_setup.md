# Project Setup

## Create Root Project Directory and Setup Git
Create a root directory `Django_REST_Framework/`
```bash
mkdir Django_REST_Framework
cd Django_REST_Framework/
```
Initialize git and default `.gitignore` file for Django
```bash
git init
touch .gitignore
```

## Install Django
First create a virtual environment `env` and activate it.
```bash
python3 -m venv env
source env/bin/activate
```

Install Django and Django REST Framework and add `rest_framework` in the `INSTALLED_APPS` array in `django_rest_framework/settings.py` file.
```bash
pip install djangorestframework
```

Add a `requirements.txt` file
```bash
pip freeze > requirements.txt
```

Create a django project at the root directory
```bash
django-admin startproject django_rest_framework .
```
Add `'rest_framework'` to the `INSTALLED_APPS` array at the `settings.py` of the project. 

## PostgreSQL Configuration
Install `psycopg2` for PostgreSQL which is the PostgreSQL adapter for Python. Django uses it to connect to PostgreSQL.
```bash
pip install psycopg2
```
Now, create a database, a user and then grant the user to that database
```bash
sudo -u postgres psql # enter into postgresql
```
```sql
CREATE DATABASE drf_db;
CREATE USER drf_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE drf_db TO drf_user;
```

Update Django Settings to Use PostgreSQL in our `django_rest_framework/settings.py`
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'drf_db',
        'USER': 'drf_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',  # or your database host
        'PORT': '5432',       # default port for PostgreSQL
    }
}
```