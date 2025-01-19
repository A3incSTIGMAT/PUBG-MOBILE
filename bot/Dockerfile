FROM python:3.10-slim

WORKDIR /app
COPY .env /app/.env

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "bot/main.py"]

