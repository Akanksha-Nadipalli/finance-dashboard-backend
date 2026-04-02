# Finance Data Processing and Access Control Backend

## 📌 Overview

This project implements a backend system for a finance dashboard that manages financial records and enforces role-based access control.

It is designed to demonstrate backend architecture, API design, data modeling, and business logic handling. The system supports multiple user roles and provides aggregated financial insights for dashboard usage.

The system is structured with clear separation of concerns between models, schemas, and API routes.

---

## 🔗 Live API Docs

Run the server locally and access interactive API documentation:
http://127.0.0.1:8000/docs

---

## 🛠️ Tech Stack

* FastAPI (API framework)
* SQLite (database)
* SQLAlchemy (ORM)
* Pydantic (data validation)

---

## 🚀 Features

### 1. User Management

* Create users
* Assign roles (viewer, analyst, admin)
* Update user details and roles
* Support for user status (active/inactive)

---

### 2. Role-Based Access Control

* Viewer → Access dashboard only
* Analyst → Access records and dashboard
* Admin → Full access (CRUD operations + user management)

Access control is implemented using dependency injection and role validation logic at the API level.

---

### 3. Financial Records Management

* Create, read, update, delete financial records
* Fields: amount, type (income/expense), category, date, notes
* Filtering support (type, category)
* Pagination support for scalable data retrieval

---

### 4. Dashboard & Analytics APIs

* Total income
* Total expenses
* Net balance
* Category-wise aggregation
* Recent transactions
* Trend analysis based on dates

These endpoints demonstrate backend aggregation and data processing beyond basic CRUD operations.

---

### 5. Validation & Error Handling

* Input validation using Pydantic
* Amount must be greater than 0
* Type restricted to "income" or "expense"
* Proper HTTP status codes:

  * 400 → Bad request (validation errors)
  * 403 → Access denied
  * 404 → Resource not found

---

### 6. Data Persistence

* SQLite database using SQLAlchemy ORM
* Lightweight and suitable for local development

---

## 📡 API Endpoints (Summary)

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

## ⚙️ Setup Instructions

1. Clone the repository:

```
git clone https://github.com/Akanksha-Nadipalli/finance-dashboard-backend
cd finance-dashboard-backend
```

2. Create virtual environment:

```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the server:

```
uvicorn app.main:app --reload
```

---

## 🧪 How to Test

1. Open Swagger UI:
   http://127.0.0.1:8000/docs

2. Create a user using POST /users

3. Create financial records using POST /records

4. Test role-based access:
   - Change user role using PUT /users/{id}
   - Try accessing restricted endpoints

5. View dashboard analytics using:
   - GET /dashboard
   - GET /dashboard/category
   - GET /dashboard/recent
  
6. (Optional) Test pagination:
   - GET /records?skip=0&limit=2
  
---     

## 🧠 Assumptions & Design Decisions

* Mock authentication is used (default user_id = 1)
* User active/inactive status is enforced during request handling
* Role-based access control implemented using dependency-based checks
* System simulates multi-user behavior without full authentication
* Designed to be extendable with JWT authentication and production-ready databases

---

## ✨ Additional Enhancements

* Pagination support for records
* Category-based aggregation
* Recent transaction tracking
* Trend analysis endpoints

---

## 📌 Conclusion

This project demonstrates a structured backend system with clear separation of concerns, role-based access control, and meaningful data processing logic.

It focuses on correctness, maintainability, and practical backend design aligned with real-world use cases.
