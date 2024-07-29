FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

EXPOSE 8080

CMD ["fastapi", "run", "app/main.py", "--port", "8080"]