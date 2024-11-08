FROM python:3.10
FROM mcr.microsoft.com/playwright/python:v1.48.0-jammy

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install scrapegraphai[burr]
RUN pip install fastapi[standard]

COPY ./app /code/app

EXPOSE 8000

CMD ["fastapi", "run", "app/main.py", "--port", "8000"]
