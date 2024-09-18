# Django/USWDS Example Project: Foundry

Just the scripts for now!

The Djando app is in design/

## Setup Python Virtual Environment

```sh
python3 -m venv ./.foundry
source .foundry/bin/activate
```

### Deactivate

```sh
deactivate
```

## Running


```sh
source .foundry/bin/activate && python manage.py runserver
```

### Install Django

```sh
python -m pip install Django
```

### Project Initiation

```sh
django-admin startproject sitename
python manage.py startapp appname
```

### Capture Packages

```sh
python -m pip freeze > requirements.txt
```

```sh
source .foundry/bin/activate
python manage.py createsuperuser
```

### Database

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py flush --no-input
```

### Shell

```sh
python manage.py shell
```

