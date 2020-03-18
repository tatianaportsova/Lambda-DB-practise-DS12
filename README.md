
## How to set up from scratch

Setup virtual env:

```sh
pipenv --python 3.7
pipenv install python-dotenv psycopg2-binary
pipenv shell
```

Setup env variables in a ".env" file (using credentials from ElephantSQL):

```sh
DB_NAME = "abc"
DB_USER = "abc"
DB_PASSWORD = "abc.abc"
DB_HOST = "abc.abc"
```

Run:

```sh
python app/pg_queries.py
```