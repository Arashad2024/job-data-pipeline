FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY producer.py .
RUN pip install requests kafka-python
RUN pip install python-dotenv

# Environment variables for Adzuna API
ENV ADZUNA_APP_ID=your_app_id
ENV ADZUNA_APP_KEY=your_app_key
ENV KAFKA_BROKER=kafka:9092

CMD ["python", "producer.py"]
