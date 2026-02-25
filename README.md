# 🚀 Python Task Manager (Enterprise CLI Edition)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Build](https://img.shields.io/github/actions/workflow/status/MiSSkSambo/python-task-manager/ci.yml?branch=main)
![Platform](https://img.shields.io/badge/Platform-Ubuntu%2022.04-orange)
![License](https://img.shields.io/badge/License-MIT-brightgreen)
![Status](https://img.shields.io/badge/Project-Production%20Ready-success)

A modular, enterprise-grade CLI Task Management system built using Python 3.10.

---

# 📑 Table of Contents

- [Executive Summary](#-executive-summary)
- [Architecture Overview](#-architecture-overview)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [Screenshots](#-screenshots)
- [Testing & CI](#-testing--ci)
- [Contribution Guidelines](#-contribution-guidelines)
- [Roadmap](#-roadmap)
- [License](#-license)

---

# 📖 Executive Summary

This project demonstrates:

- Clean modular backend architecture  
- CLI command parsing  
- JSON-based persistence  
- Virtual environment isolation  
- Automated testing integration  
- Continuous Integration (CI) workflow  

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

# ⚙️ Installation

```bash
git clone https://github.com/MiSSkSambo/python-task-manager.git
cd python-task-manager
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

# 🚀 Usage Guide

```bash
python src/main.py add "Learn Linux deeply"
python src/main.py list
python src/main.py complete 0
python src/main.py delete 0
```

---

# 📸 Screenshots

## Account Created
<img width="1920" height="1020" src="https://github.com/user-attachments/assets/194ff1ef-2916-4dc0-8826-4517aea3aa75" />

## Project Structure
<img width="1920" height="1020" src="https://github.com/user-attachments/assets/af8d50a6-0720-4060-9e62-88b6fe0fcaca" />

## CLI Output
<img width="1920" height="1080" src="https://github.com/user-attachments/assets/fa90b08b-50d1-4ef3-b6a9-b197c0c6ce43" />

---

# 🧪 Testing & CI

Run tests locally:

```bash
pytest
```

CI Pipeline runs automatically on:

- Push to main
- Pull requests

---

# 🤝 Contribution Guidelines

See CONTRIBUTING.md for full workflow.

---

# 🚀 Roadmap

- SQLite database
- FastAPI backend
- Docker support
- REST API layer
- Web frontend

---
# 👤 Author

Katlego

---

# 📜 License

MIT License
