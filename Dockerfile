FROM python:3.12-alpine as builder
RUN apk add --no-cache git
RUN pip install poetry==1.8.3
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache
WORKDIR /app
COPY ./pyproject.toml ./poetry.lock /app/
RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install
COPY . /app/
RUN poetry run mkdocs build

FROM joseluisq/static-web-server:2
COPY --from=builder /app/site /site
EXPOSE 80
CMD ["--root", "/site"]
