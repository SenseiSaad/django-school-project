FROM python:3.11-slim

RUN apt-get update && apt-get install -y libpq-dev gcc

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Pass dummy env vars so settings.py can compile for collectstatic
RUN SECRET_KEY="dummy" DB_NAME="dummy" DB_USER="dummy" DB_PASSWORD="dummy" DB_HOST="dummy" AWS_ACCESS_KEY_ID="dummy" AWS_SECRET_ACCESS_KEY="dummy" AWS_STORAGE_BUCKET_NAME="dummy" AWS_S3_REGION_NAME="dummy" python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && gunicorn portfolio_backend.wsgi:application --bind 0.0.0.0:8000 --workers 2"]
