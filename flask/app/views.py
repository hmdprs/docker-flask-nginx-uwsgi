import os

from app import app


@app.route("/")
def index():

    # get environment variable
    app_name = os.getenv("APP_NAME")
    if app_name:
        return f"Hello from {app_name} running in a Docker container behind Nginx!"

    return "Hello from Flask"
