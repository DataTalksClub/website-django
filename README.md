#  DTC website in Django


## Running it locally 

### Installing dependencies

Install pipenv:

```bash
pip install pipenv
```

Install the dependencies:

```bash
pipenv install
```

Activate virtual env:

```bash
pipenv shell
```

### Running the service

```bash
cd dtc
python manage.py runserver
```


## Docker

```bash
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="dtc_db" \
  -v dtc_postgres:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13
```