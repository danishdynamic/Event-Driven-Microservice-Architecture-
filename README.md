## StreamStore: Real-Time Order Tracking Engine

StreamStore is an event-driven microservices prototype built to demonstrate high-throughput data processing using Apache Kafka (KRaft mode). The system decouples order creation from order tracking, allowing for a scalable, fault-tolerant architecture.

### 🏗️ Architecture Overview
The project consists of three core components running in isolated Docker containers:

- Kafka Broker (KRaft Mode): The central event bus that manages message topics and persistence without the need for ZooKeeper.

- Order Producer (Microservice A): A Python-based service that simulates order placement by producing JSON-encoded events to the orders topic.

- Order Tracker (Microservice B): A consumer service that listens to the orders topic in real-time, processes payloads, and provides status updates.

### 🚀 Tech Stack

- Language: Python 3.12

- Message Broker: Apache Kafka 7.8.3 (Confluent Distribution)

- Orchestration: Docker & Docker Compose

- Libraries: confluent-kafka

### 🛠️ Getting Started

Prerequisites

- Docker Desktop installed and running.

- Python 3.12+ (for local development).

1. Clone the Repository

``` Bash
git clone https://github.com/your-username/StreamStore-Engine.git
cd StreamStore-Engine
```
2. Environment Setup
Create a virtual environment and install dependencies if you wish to run scripts locally:

``` Bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

3. Spin up the Infrastructure
Use Docker Compose to build the images and start the cluster:

``` Bash
docker-compose up --build -d
```
This command builds the custom Python images for the Producer and Tracker and starts the Kafka KRaft broker.

4. Monitor the Logs
To see the microservices interacting in real-time:

``` Bash
docker-compose logs -f
```
### 📡 Kafka Configuration Details

The system uses KRaft mode, which simplifies the architecture by removing the ZooKeeper dependency.

- Topic Name: orders

- Partitions: 1 (Scalable)

- Replication Factor: 1 (Optimized for local dev)

- Internal Network: Services communicate via the kafka:9092 listener.

📂 Project Structure

``` Bash
StreamStore/
├── .gitignore             # Prevents venv and cache uploads
├── Dockerfile             # Multi-service Python build recipe
├── docker-compose.yml     # Infrastructure and service orchestration
├── producer.py            # Order placement logic
├── tracker.py             # Status tracking logic
└── requirements.txt       # Project dependencies
```
### 🛡️ Key Features Included

- Graceful Shutdown: Consumers utilize finally blocks to close connections and commit offsets properly.

- Type Safety: Implements None checks and Walrus operators for robust message polling.

- Containerization: Uses python:3.12-slim to reduce image size and minimize security vulnerabilities.

- Decoupling: The Producer and Tracker are completely unaware of each other, communicating solely through event streams.

### 📈 Future Roadmap

- [ ] Add Redis for caching the "Last Known State" of orders.

- [ ] Implement Pydantic models for strict schema validation.

- [ ] Deploy to a local Kubernetes (Minikube) cluster using Helm charts.
