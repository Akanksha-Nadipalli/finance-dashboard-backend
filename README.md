# Finance Data Processing and Access Control Backend

## 📌 Overview

This project is a backend system for a finance dashboard that manages financial records and enforces role-based access control.

It allows different users to interact with financial data based on their roles, and provides summary analytics for dashboard visualization.

---

## 🛠️ Tech Stack

* FastAPI
* SQLite
* SQLAlchemy
* Pydantic

---

## 🚀 Features

### 1. User Management

* Create users
* Assign roles (viewer, analyst, admin)
* Update user details and roles

### 2. Role-Based Access Control

* Viewer: Access only dashboard
* Analyst: View records and dashboard
* Admin: Full access (CRUD operations)

Access control is implemented using dependency-based role checks.

---

### 3. Financial Records

* Create, read, update, delete records
* Fields: amount, type, category, date, notes
* Filtering support (type, category)

---

### 4. Dashboard APIs

* Total income
* Total expenses
* Net balance
* Category-wise totals
* Recent transactions
* Trends based on date

---

### 5. Validation & Error Handling

* Input validation using Pydantic
* Amount must be greater than 0
* Type must be either "income" or "expense"
* Proper HTTP status codes (400, 403, 404)

---

### 6. Data Persistence

* SQLite database using SQLAlchemy ORM
* Database stored locally for simplicity

---

## 📡 API Endpoints (Sample)

### Users

* POST /users
* GET /users
* PUT /users/{id}

### Records

* POST /records
* GET /records
* PUT /records/{id}
* DELETE /records/{id}

### Dashboard

* GET /dashboard
* GET /dashboard/category
* GET /dashboard/recent
* GET /dashboard/trends

---

## 📖 API Documentation

Interactive API documentation is available via Swagger UI:

http://127.0.0.1:8000/docs

---

## ⚙️ Setup Instructions

1. Clone the repository:

```
git clone <your-repo-link>
cd finance-backend
```

2. Create virtual environment:

```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```
pip install fastapi uvicorn sqlalchemy pydantic email-validator
```

4. Run the server:

```
uvicorn app.main:app --reload
```

---

## 🧠 Assumptions & Design Decisions

* Mock authentication is used (default user_id = 1)
* Role-based access is enforced using dependency injection
* Database is local SQLite for simplicity
* System is designed to be easily extendable with authentication (JWT)

---

## ✨ Additional Enhancements

* Pagination support for records
* Category-based aggregation
* Recent transaction tracking
* Trend analysis

---

## 📌 Conclusion

This project demonstrates backend design, API structuring, role-based access control, and data processing for a finance dashboard system.

It focuses on clarity, maintainability, and logical organization of backend components.
