import os
import requests
import json
from kafka import KafkaProducer
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Adzuna API details
API_URL = "https://api.adzuna.com/v1/api/jobs"
APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")
COUNTRY = "gb"
QUERY = "data engineer"

# Kafka details
KAFKA_TOPIC = "jobs_data"
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")

def fetch_jobs():
    """Fetch job postings from Adzuna API."""
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "results_per_page": 20,
        "what": QUERY,
    }
    response = requests.get(f"{API_URL}/{COUNTRY}/search/1", params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print(f"Failed to fetch jobs: {response.status_code} {response.text}")
        return []

def produce_jobs_to_kafka():
    """Produce job postings to Kafka."""
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    while True:
        jobs = fetch_jobs()
        for job in jobs:
            producer.send(KAFKA_TOPIC, job)
            print(f"Produced job: {job['title']}")
        time.sleep(60)

if __name__ == "__main__":
    produce_jobs_to_kafka()
