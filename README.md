# 🧮 FastAPI BMI Calculator

A simple **FastAPI** application that calculates **Body Mass Index (BMI)** based on weight and height.  
The project is **Dockerized** and includes **GitHub Actions CI** for automated builds.

---

## 🚀 Features
- FastAPI-based REST API
- BMI calculation with category classification
- Docker support
- GitHub Actions CI (build validation)
- Swagger UI documentation

---

## 📁 Project Structure

fastapi-bmi/
├── app/
│   └── main.py
├── .github/
│   └── workflows/
│       └── docker-build.yml
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md

---

## 🛠️ Tech Stack
- **Python 3.11**
- **FastAPI**
- **Uvicorn**
- **Docker**
- **GitHub Actions**

---

## ▶️ Running Locally (Without Docker)

### 1️⃣ Create Virtual Environment
```bash
python3 -m venv env
source env/bin/activate

