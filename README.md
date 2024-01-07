# DataEngineering

Realtime Data Streaming | End-to-End Data Engineering Project

This project shows building an end-to-end data engineering pipeline. It covers each stage from data ingestion to processing and finally to storage, utilizing a robust tech stack that includes Apache Airflow, Python, Apache Kafka, Apache Zookeeper, Apache Spark, and Cassandra. Everything is containerized using Docker for ease of deployment and scalability.


# Project Components:

DATA SOURCE: Using randomuser.me API to generate random user data for DATA PIPELINE.
Apache Airflow: Responsible for orchestrating the pipeline and storing fetched data in a PostgreSQL database.
Apache Kafka and Zookeeper: Used for streaming data from PostgreSQL to the processing engine.
Control Center and Schema Registry: Helps in monitoring and schema management of our Kafka streams.
Apache Spark: For data processing with its master and worker nodes.
Cassandra: Where the processed data will be stored.

# Steps
Setting up a data pipeline with Apache Airflow
Real-time data streaming with Apache Kafka
Distributed synchronization with Apache Zookeeper
Data processing techniques with Apache Spark
Data storage solutions with Cassandra and PostgreSQL
Containerizing your entire data engineering setup with Docker

Technologies: Apache Airflow, Python, Apache Kafka, Apache Zookeeper, Apache Spark, Cassandra, PostgreSQL, Docker, Getting Started

# Recommended steps to checkout the Project

1. Clone the repository:

git clone https://github.com/airscholar/e2e-data-engineering.git](https://github.com/varshahindupur09/Real-Time-Data-Processing-DE-Project.git

2. Run Docker Compose to start services:

docker-compose up

docker-compose down


# Architecture Diagram:

[https://github.com/varshahindupur09/Real-Time-Data-Processing-DE-Project/blob/main/architecture_diagram/arch_image.png]

