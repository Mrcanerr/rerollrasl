FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Создаём папку для базы данных
RUN mkdir -p data

CMD ["python", "bot.py"]
