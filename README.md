
# 🚀 Python Task Manager (Enterprise CLI Edition)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Platform](https://img.shields.io/badge/Platform-Ubuntu%2022.04-orange)
![Virtual Environment](https://img.shields.io/badge/Environment-venv-green)
![License](https://img.shields.io/badge/License-MIT-brightgreen)
![Project Status](https://img.shields.io/badge/Status-Active-success)

A modular, enterprise-grade Command-Line Task Management system built with Python 3.10 on Ubuntu 22.04.

---

# 📖 Executive Summary

The Python Task Manager is a structured CLI-based application designed with professional backend engineering principles:

- Clean modular architecture
- JSON-based persistence layer
- Virtual environment isolation
- Command-line argument parsing
- Error handling and validation
- Linux-first development workflow

---

# 🏗️ Architecture Overview

python-task-manager/
│
├── venv/                     # Virtual environment
├── src/
│   ├── __init__.py
│   ├── main.py               # CLI entry point
│   └── task_manager.py       # Business logic layer
│
├── tasks.json                # Data persistence layer
├── requirements.txt
└── README.md

---

# ⚙️ Installation & Setup

## Clone Repository

git clone https://github.com/MiSSkSambo/python-task-manager.git  
cd python-task-manager  

## Create Virtual Environment

python3 -m venv venv  
source venv/bin/activate  

---

# 🚀 Usage Guide

Add Task  
python src/main.py add "Learn Linux deeply"

List Tasks  
python src/main.py list

Complete Task  
python src/main.py complete 0

Delete Task  
python src/main.py delete 0

---

# 📸 Screenshots
## Account Created
<img width="1920" height="1020" alt="account created" src="https://github.com/user-attachments/assets/194ff1ef-2916-4dc0-8826-4517aea3aa75" />

---

## Project Structure
<img width="1920" height="1020" alt="project structure" src="https://github.com/user-attachments/assets/af8d50a6-0720-4060-9e62-88b6fe0fcaca" />

---

## CLI Execution Output
<img width="1920" height="1080" alt="output" src="https://github.com/user-attachments/assets/fa90b08b-50d1-4ef3-b6a9-b197c0c6ce43" />


---

# 🧪 Automated Testing

Planned integration with:

- pytest
- Coverage reports
- GitHub Actions CI

Run tests:

pytest

---

# 🤝 Contribution Guidelines

1. Fork repository  
2. Create feature branch  
3. Follow PEP8  
4. Write unit tests  
5. Submit pull request  

---

# 🚀 Roadmap

- SQLite integration
- FastAPI REST API
- Docker support
- Web frontend
- CI/CD

---

# 👤 Author

Katlego

---

# 📜 License

MIT License
