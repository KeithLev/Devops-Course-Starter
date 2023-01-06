FROM python:3.7-slim-buster AS base
EXPOSE 5000
WORKDIR /todo-app
RUN apt-get update
RUN apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python - --version 1.1.15
ENV PATH="${PATH}:/root/.poetry/bin"
COPY ./poetry.toml ./pyproject.toml poetry.lock ./ 
RUN poetry config virtualenvs.create false --local && poetry install


FROM base AS production
COPY ./todo_app ./todo_app/
ENV PORT=5000
CMD poetry run gunicorn "todo_app.app:create_app()" --bind 0.0.0.0:$PORT

FROM base AS development
CMD [ "poetry", "run", "flask", "run", "--host", "0.0.0.0"]

FROM base AS test
COPY ./todo_app ./todo_app/
COPY ./test_to_do_app ./test_to_do_app/
CMD [ "poetry", "run", "pytest"]