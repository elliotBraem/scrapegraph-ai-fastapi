FROM python:3.10
FROM mcr.microsoft.com/playwright/python:v1.48.0-jammy

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install scrapegraphai[burr]
RUN pip install fastapi[standard]

COPY ./app /code/app

# Conditionally copy .env file only in development
RUN if [ "$ENVIRONMENT" = "development" ]; then \
        echo "Development environment - will copy .env file"; \
    else \
        echo "Production environment - skipping .env file"; \
    fi

COPY .env* /code/.env 2>/dev/null || true

EXPOSE 8000

CMD ["fastapi", "run", "app/main.py", "--port", "8000"]
