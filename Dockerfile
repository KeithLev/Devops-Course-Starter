FROM python:3.7-slim-buster AS base
EXPOSE 5000
WORKDIR /todo-app
RUN apt-get update
RUN apt-get install -y curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"
COPY ./poetry.toml ./pyproject.toml poetry.lock ./
RUN poetry install


FROM base AS production
COPY ./todo_app /todo-app/todo_app
CMD [ "poetry", "run", "gunicorn", "--bind", "0.0.0.0:5000", "todo_app.wsgi:app" ]

FROM base AS development
CMD [ "poetry", "run", "flask", "run", "--host", "0.0.0.0"]
