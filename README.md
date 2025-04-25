[![Dynamic DevOps Roadmap](https://img.shields.io/badge/Dynamic_DevOps_Roadmap-559e11?style=for-the-badge&logo=Vercel&logoColor=white)](https://devopsroadmap.io/getting-started/)
[![Community](https://img.shields.io/badge/Join_Community-%23FF6719?style=for-the-badge&logo=substack&logoColor=white)](https://newsletter.devopsroadmap.io/subscribe)
[![Telegram Group](https://img.shields.io/badge/Telegram_Group-%232ca5e0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/DevOpsHive/985)
[![Fork on GitHub](https://img.shields.io/badge/Fork_On_GitHub-%2336465D?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork)

# HiveBox - DevOps End-to-End Hands-On Project
## 🐝 HiveBox Project – Phase 3: Building the RESTful API with FastAPI


<p align="center">
  <a href="https://devopsroadmap.io/projects/hivebox" style="display: block; padding: .5em 0; text-align: center;">
    <img alt="HiveBox - DevOps End-to-End Hands-On Project" border="0" width="90%" src="https://devopsroadmap.io/img/projects/hivebox-devops-end-to-end-project.png" />
  </a>
</p>

> [!CAUTION]
> **[Fork](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork)** this repo, and create PRs in your fork, **NOT** in this repo!

> [!TIP]
> If you are looking for the full roadmap, including this project, go back to the [getting started](https://devopsroadmap.io/getting-started) page.


## 📌 Project Overview

This is a lightweight backend API built with **FastAPI** that fetches environmental sensor data (temperature) using the [openSenseMap API](https://docs.opensensemap.org/). The project includes containerization, code linting, testing, and CI/CD automation.

---

## 🚀 Features

- **/version** – Returns the current version of the deployed app
- **/temperature** – Returns average temperature data from all senseBoxes (within the last 1 hour)
- **openSenseMap API integration**
- Fully containerized with **Docker**
- Automated **CI/CD** with GitHub Actions
- Code quality enforcement via **Pylint** and **Hadolint**
- Secure development practices with **OpenSSF Scorecard**

---

## 📦 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- Python 3.9-slim
- Docker
- GitHub Actions (CI/CD)
- openSenseMap API
- Pylint, Hadolint (Linting)
- Pytest (Unit Testing)

---

## 🧰 Setup Instructions

### 🔨 Prerequisites

- Python 3.9-slim
- Docker & Docker Compose
- [VS Code](https://code.visualstudio.com/) with extensions:
  - Pylint
  - Hadolint

---

### 📥 Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

### 🧪 Run Tests

```bash
pytest
```

---

### ▶️ Run the App (Dev)

```bash
uvicorn app.main:app --reload
```

---

## 🐳 Docker Usage

### 🏗️ Build the Docker Image

```bash
docker build -t hivebox-api .
```

### 🚀 Run the Container

```bash
docker run -d hivebox-api
```

---

## 🔁 API Endpoints

### `/version`

**Method**: `GET`  
**Response**:
```json
{
  "version": "0.1.0"
}
```

---

### `/temperature`

**Method**: `GET`  
**Response**:
```json
{
  "average_temperature": 13.61,
  "unit": "°C",
  "measurements_count": 3,
  "timestamp": "2025-04-24T20:40:08.237476+00:00"
}
```

**Note**: Only includes sensor data from the last **1 hour**.

---

## 🔧 Development Tools

- **Linting**:  
  - Python: `pylint`
  - Docker: `hadolint`

- **Git**:  
  - Follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
  - Pre-commit checks via GitHub Actions

---

## 🔄 Continuous Integration (GitHub Actions)

- Lint Python code and Dockerfile
- Build Docker image
- Run unit tests
- Verify `/version` endpoint response
- OpenSSF Scorecard integration

---

## 🔒 Security & Best Practices

- OpenSSF Scorecard GitHub Action integration
- Docker built with multi-stage and non-root user
- CI enforces quality and security standards

---

## 📄 License

MIT License. See `LICENSE` for details.

---

## 👥 Contributors

Maintained by the backend engineering team 🚀

---

## 📬 Feedback & Issues

Found a bug or have a feature request? [Open an issue](https://github.com/your-org/sensor-api/issues).

```

---