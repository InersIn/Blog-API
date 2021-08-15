# Blog-API
API for Blog CRUD

Read Here For API Documentation: [Docs](https://documenter.getpostman.com/view/6844683/Tzz7QJqW)

## Instalation

### Setup Environment
```sh
python3 -m virtualenv .env
```

```sh
source .env/bin/activate
```

```sh
git clone https://github.com/InersIn/Blog-API.git
```

```sh
cd Blog-API
```

```sh
pip3 install -r ./requirements.txt
```

### Import Database
Database configuration for the API. file ```blog/settings.py```
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Blog',       # Database name
        'USER': 'admin',      # Database username
        'PASSWORD': '',       # Database password default in file `database.sql` is empty
        'HOST': 'localhost',  # Database host
        'PORT': '3306'        # Database post
    }
}
```

```sh
mysql -u admin -p Blog < database.sql #Make sure database name is same as `settings.py`
```

### Run Application
```sh
./manage.py runserver
```
