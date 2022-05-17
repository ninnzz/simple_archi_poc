# Simple architecture POC

## Setup

- Install python +3.10 https://www.python.org/downloads/release/python-3100/
- Install poetry https://python-poetry.org/docs/

After installing python and poetry, run the following command

```
poetry config virtualenvs.in-project true
poetry install
```

## Running application

```
poetry run uvicorn app.server:app --reload
```

If not using poetry

```
uvicorn app.server:app --reload
```

Once you successfully install the application


This command will run the application. Check `http://127.0.0.1:8000` to see your web sever.

Check `http://127.0.0.1:8000/docs` for full list of available APIs.
