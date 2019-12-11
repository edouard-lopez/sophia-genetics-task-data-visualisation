FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip3 install \
    pytest \
    requests \
    sqlalchemy \
    starlette

COPY ./app /app