# Job Portal App

Team 404 clone of [Sany07/Job-Portal-Django](https://github.com/Sany07/Job-Portal-Django)


## Install requirements

```
pip install -r requirements.txt
```
#### note: Comment this module `psycopg2==2.8.6` in `requirements.txt` for local development

## Database

```
Set the database from settings.py
```

## To initialize the app for development, edit `job/settings.py` and update from

```
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'django_job_app_dev',
        # 'USER': 'root',
        # 'PASSWORD': 'root',
        # 'HOST': 'localhost',
        # 'PORT': '3306',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ["PGDATABASE"],
        'USER': os.environ["PGUSER"],
        'PASSWORD': os.environ["PGPASSWORD"],
        'HOST': os.environ["PGHOST"],
        'PORT': os.environ["PGPORT"],
    }
}
```

## to

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_job_app_dev',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': os.environ["PGDATABASE"],
        # 'USER': os.environ["PGUSER"],
        # 'PASSWORD': os.environ["PGPASSWORD"],
        # 'HOST': os.environ["PGHOST"],
        # 'PORT': os.environ["PGPORT"],
    }
}
```

## Then create new database in mysql server in xampp, or any mysql server

```
CREATE DATABASE django_job_app_dev
```

#### note: xampp mysql servers defaults to `user:root` and `password:<empty>`, update your `job/settings.py` properly

## To migrate the database open terminal in project directory and type

```
python manage.py makemigrations
python manage.py migrate
```

## Collects all static files in your apps

```
python manage.py collectstatic
```

## Run the server

```
python manage.py runserver localhost:80
```

### You may now view the app on your browser via url: [http://localhost](http://localhost:80)

### Post an issue for any concerns