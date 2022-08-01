# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

Set enviroment variables as follows:
App_TOKEN - app token
APP_KEY - app key
NOT_STARTED_LIST_ID - list id for not started list
STARTED_LIST_ID - list id for started list
DONE_LIST_ID - list id for done list



## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Testing the app
Run "poetry run pytest"
You should see 4 tests pass

## Setting up vm using ansible
Update inventory with VM addresses
Run "ansible-playbook playbook.yaml -i inventory"
Enter required params when prompted

## Running using container
Ensure .env file is added to base of dicetory

Build the container using the following commands:
Development:
docker build --target development --tag todo-app:dev .
Production:
docker build --target production --tag todo-app:prod .
Test:
docker build --target test --tag todo-app:test .

Run the containers using the following commands:
Development:
docker run -p 5000:5000 --env-file .env --mount type=bind,source="$(pwd)"/todo_app,target=/todo-app/todo_app todo-app:dev
Production:
docker run -p 5000:5000 --env-file .env todo-app:prod
Test:
docker run -it --env-file .env.test todo-app:test


## Run Docker Compose
Ensure .env file is added to base dicetory

Run "docker compose up" from the comand line

