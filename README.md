# 🛡️ End to End ML Pipeline for Phishing Website Detection

## 📌 Project Overview

A **Machine Learning–based Phishing Detection System** with an **End-to-End ML pipeline** and a **deployment-ready FastAPI service for real-time URL classification**.

The system automates the **end-to-end ML pipeline**, including:
- Data ingestion from MongoDB
- Data validation and drift detection
- Data transformation
- Model training and evaluation
- Prediction through a FastAPI web interface

It is built with **production-grade architecture**, following modular design, logging, exception handling, and CI/CD readiness.

---

## 🎯 Problem Statement

Phishing websites pose a serious cybersecurity threat by mimicking legitimate websites to steal sensitive information.  
This project aims to **classify website data as either legitimate or phishing**, helping organizations and users improve network security.

---

## 🧠 Solution Approach

1. **Dataset**
   - Phishing website dataset stored in MongoDB
   - Features extracted from URLs and website metadata

2. **Machine Learning Pipeline**
   - Data Ingestion
   - Data Validation (Schema & Drift Detection)
   - Data Transformation (Preprocessing & Imputation)
   - Model Training (Classification models)
   - Model Evaluation
   - Prediction & Output generation

3. **Web API**
   - FastAPI-based REST service
   - Upload URL and receive phishing predictions

---

## ⚙️ Tech Stack Used

### 🔹 Programming & Frameworks
- Python 3.13
- FastAPI
- Uvicorn

### 🔹 Machine Learning
- Scikit-learn
- NumPy
- Pandas
- Pickle

### 🔹 Database
- MongoDB Atlas
- PyMongo

### 🔹 DevOps & MLOps
- GitHub Actions
- Docker-ready architecture
- MLFlow and DAGsHub
- Data Drift Detection
- Logging & Exception Handling

### 🔹 Cloud Deployment
- Amazon S3 Bucket (Artifact and Model Storage)
- Amazon ECR (Docker Image Repository)
- Amazon EC2 Instance (Web App Deployment)

---

## 🗄 MongoDB Atlas Setup

1. Create a MongoDB Atlas account:  
   https://www.mongodb.com/cloud/atlas

2. Create a new cluster (Free Tier M0 works)

3. Create a database and collection:
   - Database name: `your_db_name`
   - Collection name: `your_collection_name`

4. Add your IP address to **Network Access**

5. Create a database user and note:
   - Username
   - Password

6. Set your Database name and Collection name as a constant for data ingestion:
   -  Go to networksecurity/constant/training_pipeline/__init__.py
   -  Replace DATA_INGESTION_COLLECTION_NAME value with your MongoDB Collection name
   -  Replace DATA_INGESTION_DATABASE_NAME value with your MongoDB Database name

---

## 🔐 Environment Variables

Create a `.env` file in the root directory and add:

```env
MONGO_DB_URL=mongodb+srv://<username>:<password>@cluster0.mongodb.net/<db_name>?retryWrites=true&w=majority
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## ▶️ Run the FastAPI Application
```bash
python app.py
```

## ▶️ Run the Training Pipeline Locally
```bash
python main.py
```
