# docker-compose test
*A simple Flask app + Ngingx & uWSGI with Docker Compose*

## Run

To develop locally, create a new virtual `env` in the flask directory & run the app:

```bash
pip install -r requirements.txt
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```

Then, open `localhost:5000` in your browser.

Or to run the app in the container:

```bash
docker-compose up --build
```

Then, open `localhost` in your browse.

## Credit
- [Containerizing Python web apps with Docker, Flask, Nginx & uWSGI](https://www.youtube.com/watch?v=dVEjSmKFUVI) by [Julian Nash](https://github.com/Julian-Nash)
