FROM python:3.11-slim

RUN apt-get update && apt-get install -y sqlite3

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "bot.main"]

