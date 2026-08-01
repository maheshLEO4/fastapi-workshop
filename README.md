# FastAPI Workshop

Welcome to the **FastAPI Workshop**! This repository is designed as a hands-on learning project to help you understand the fundamentals of building REST APIs using **FastAPI**.

Instead of providing a fully completed application, this project contains guided exercises and TODO sections that you will implement throughout the workshop.

---

#  Learning Objectives

By the end of this workshop, you will learn how to:

* Build a FastAPI application
* Create API endpoints
* Read data from a JSON file
* Use Path Parameters
* Use Query Parameters
* Handle HTTP Exceptions
* Create request models using Pydantic
* Perform CRUD (Create, Read, Update, Delete) operations
* Explore and test APIs using Swagger UI

---

#  Technologies Used

* Python 3.10+
* FastAPI
* Uvicorn
* Pydantic
* JSON

---

#  Project Structure

```text
fastapi-workshop/
│
├── main.py             # FastAPI application
├── patients.json       # Sample patient dataset
├── pyproject.toml      # Project configuration
├── uv.lock             # Dependency lock file
├── .gitignore
└── README.md
```

---

#  Prerequisites

Before getting started, make sure you have:

* Python 3.10 or later
* Git
* VS Code 

---

# Clone the Repository

```bash
git clone https://github.com/AparnaBharani/fastapi-workshop.git
cd fastapi-workshop
```

---

# Create a Virtual Environment

## Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

---

## Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

#  Install Dependencies

## Option 1 (Recommended - using uv)

```bash
uv sync
```

## Option 2 (using pip)

```bash
pip install fastapi "uvicorn[standard]"
```

---

#  Run the Application

Using **uv**:

```bash
uv run uvicorn main:app --reload
```

Or using **uvicorn** directly:

```bash
uvicorn main:app --reload
```

If everything is working correctly, you should see output similar to:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

#  API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

These pages allow you to explore and test your API directly from the browser.

---

# 🧑 Workshop Roadmap

This workshop is divided into small sections. Each section introduces a new FastAPI concept.

*  Create a FastAPI application
*  Run a FastAPI server
*  Read data from a JSON file
*  View all patients
*  Path Parameters
*  HTTP Exceptions
*  Query Parameters
*  Pydantic Models
*  Create a Patient
*  Update a Patient
*  Delete a Patient

---

#  Sample Data

Patient records are stored in **patients.json**.

As you progress through the workshop, your API will read from and update this dataset.

---

#  Future Improvements

Possible enhancements include:

* Data validation
* Database integration (SQLite/PostgreSQL)
* Authentication
* Environment variables
* Docker support
* Automated testing
* Logging
* Deployment to a cloud platform

---

#  Contributing

Contributions, suggestions, and improvements are welcome.

If you discover an issue or have an idea for improving the workshop, feel free to open an issue or submit a pull request.

---
