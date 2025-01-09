# **Job Data Pipeline with Adzuna API**

This project implements a **containerized data pipeline** to fetch job data in near real-time from the Adzuna API. It streams the data to Apache Kafka, processes it with Apache NiFi, and stores the results in a PostgreSQL database. The data can be visualized using tools like Power BI or Tableau.

---

## **Key Features**
1. Fetches real-time job data for "Data Engineer" roles using the Adzuna API.
2. Streams data to Kafka for scalable message handling.
3. Processes and loads data into PostgreSQL using Apache NiFi.
4. Fully containerized with Docker Compose for seamless deployment.
5. Automated NiFi dataflow deployment with a REST API script.

---

## **Project Workflow**

1. **Adzuna Producer**:  
   Fetches job data from the Adzuna API and pushes it to a Kafka topic (`jobs_data`).  

2. **Apache Kafka**:  
   Acts as a message broker, ensuring reliable data streaming.  

3. **Apache NiFi**:  
   Consumes data from Kafka, processes the JSON data, and loads it into a PostgreSQL database.  

4. **PostgreSQL Database**:  
   Stores processed job data in a structured format for analysis and visualization.  

---

## **Project Structure**
```plaintext
job-data-pipeline/
│
├── adzuna-producer/         
│   ├── producer.py          # Main Python script for fetching job data
│   ├── requirements.txt     # Python dependencies
│   ├── Dockerfile           # Docker setup for the producer
│   └── .env                 # Local environment variables (ignored by Git)
│
├── nifi/                    
│   ├── Dockerfile           # Docker setup for Apache NiFi
│   ├── deploy_nifi_flow.sh  # Script for NiFi dataflow deployment
│   └── job_data_pipeline.json  # NiFi dataflow definition
│
├── postgres/                
│   ├── init.sql             # Initialization script for creating schema/tables
│
├── docker-compose.yml       # Orchestration for all services
├── .env                     # Global environment variables
├── .gitignore               # Files to ignore in the repository
└── README.md                # Documentation
```

---

## **Development Instructions**

### **1. Prerequisites**
Ensure you have the following installed:
- **Docker** and **Docker Compose**
- **Python 3.9+** (for local testing of the producer)
- **Adzuna API Account** (Sign up at [Adzuna](https://developer.adzuna.com) to get your `APP_ID` and `APP_KEY`).

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/job-data-pipeline.git
cd job-data-pipeline
```

### **2. Configure Environment Variables**
Create a `.env` file in the root directory and populate it with:
```plaintext
# Adzuna API credentials
ADZUNA_APP_ID=your_adzuna_app_id
ADZUNA_APP_KEY=your_adzuna_app_key

# Kafka configuration
KAFKA_BROKER=kafka:9092

# PostgreSQL credentials
POSTGRES_USER=jobs_user
POSTGRES_PASSWORD=jobs_pass
POSTGRES_DB=jobs_db
```

---

### **3. Build and Deploy the Pipeline**
Run the following command to build and start all services:
```bash
docker-compose up --build
```

### **4. Access Services**
- **Apache NiFi**:  
  Open the NiFi UI at [http://localhost:8080/nifi](http://localhost:8080/nifi).  
  The dataflow is deployed automatically.

- **PostgreSQL Database**:  
  Use any database client (e.g., pgAdmin, DBeaver, or CLI) to connect:
  - Host: `localhost`
  - Port: `5432`
  - Database: `jobs_db`
  - User: `jobs_user`
  - Password: `jobs_pass`

---

## **How It Works**

### **Step 1: Adzuna Producer**
- The `adzuna-producer` service fetches job postings from the Adzuna API for the title **"Data Engineer"**.
- Data is pushed to a Kafka topic named `jobs_data`.

### **Step 2: Apache Kafka**
- Kafka acts as a message broker, ensuring fault-tolerant, real-time data streaming.

### **Step 3: Apache NiFi**
- NiFi consumes data from the Kafka topic.
- Processes the JSON data to extract job details (e.g., title, company, location, salary).
- Inserts the processed data into a PostgreSQL database.

### **Step 4: PostgreSQL Database**
- Job data is stored in a structured table for further analysis or visualization.

---

## **Accessing the Data**

### **Connect with Power BI**
1. Open Power BI Desktop.
2. Go to **Get Data** > **PostgreSQL**.
3. Enter connection details:
   - **Server**: `localhost`
   - **Database**: `jobs_db`
   - **Username**: `jobs_user`
   - **Password**: `jobs_pass`
4. Import tables and create visualizations.

---

## **Deploy on Other Machines**

### **Steps for Deployment**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/job-data-pipeline.git
   cd job-data-pipeline
   ```

2. Set up environment variables in a `.env` file:
   ```plaintext
   ADZUNA_APP_ID=your_adzuna_app_id
   ADZUNA_APP_KEY=your_adzuna_app_key
   KAFKA_BROKER=kafka:9092
   POSTGRES_USER=jobs_user
   POSTGRES_PASSWORD=jobs_pass
   POSTGRES_DB=jobs_db
   ```

3. Build and start the services:
   ```bash
   docker-compose up --build
   ```

4. Confirm that all services are running:
   ```bash
   docker ps
   ```

---

## **Troubleshooting**

### **1. NiFi Dataflow Not Deployed**
- Check the NiFi container logs:
  ```bash
  docker logs <nifi-container-id>
  ```
- If the script fails, manually upload the `job_data_pipeline.json` using the NiFi Web UI.

### **2. Cannot Connect to PostgreSQL**
- Verify that the PostgreSQL container is running:
  ```bash
  docker ps
  ```
- Check the credentials in your `.env` file.

### **3. Producer Not Fetching Data**
- View logs for the `adzuna-producer` container:
  ```bash
  docker logs <producer-container-id>
  ```
- Ensure the Adzuna API credentials in the `.env` file are correct.

---

## **Future Enhancements**
- **Monitoring and Alerts**: Add Prometheus and Grafana to monitor pipeline performance.
- **Extend API Integration**: Include data for other job titles or regions.
- **Enhanced Error Handling**: Improve retries for API requests and Kafka delivery failures.
- **Data Quality Checks**: Integrate checks to ensure data consistency.

---

Let me know if you encounter any issues or need help setting this up! 😊

