# 🛒 FastAPI E-Commerce Backend

A backend API built using **FastAPI**, featuring authentication, role-based access, cart management, and order processing.

---

## 🚀 Features

* 🔐 JWT Authentication (Register / Login)
* 👤 Role-Based Access Control (Admin/User)
* 📦 Product & Category Management
* 🛒 User-specific Cart System
* 🧾 Order & Checkout System
* 🗄️ SQLAlchemy ORM with SQLite/PostgreSQL
* ⚡ Dependency Injection (FastAPI)
* 🧱 Modular Project Structure
* 🐳 Docker Support

---

## 🧱 Tech Stack

* **Backend:** FastAPI
* **Database:** SQLite / PostgreSQL
* **ORM:** SQLAlchemy
* **Authentication:** JWT (python-jose)
* **Password Hashing:** Argon2 (passlib)
* **Containization:** Docker


## 🔐 Authentication Flow

1. User registers → `/users/register`
2. User logs in → `/users/login`
3. Receives JWT token
4. Use token in header:

```id="xkk32k"
Authorization: Bearer <token>
```

---

## 🛒 Cart Flow

* Add item → `/cart/add`
* View cart → `/cart`
* Remove item → `/cart/{id}`

---

## 🧾 Order Flow

* Checkout → `/orders/checkout`
* View user orders → `/orders/my-orders`

---

## ⚙️ Installation

### 1️⃣ Clone repository

```id="1m8hr4"
git clone <your-repo-url>
cd fastapi-ecommerce
```

---

### 2️⃣ Create virtual environment

```id="cw6rha"
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install dependencies

```id="uv8d3n"
pip install -r requirements.txt
```

---

### 4️⃣ Run server

```id="y11i3c"
uvicorn app.main:app --reload
```

---

### 5️⃣ Open API Docs

```id="l1rj1y"
http://127.0.0.1:8000/docs
```

###  🐳 Docker Setup
Build image
```
docker build -t fastapi-app .
```
Run container
```
docker run -p 8000:8000 fastapi-app
```

---

## 🔥 Key Concepts Used

* Dependency Injection (`Depends`)
* JWT Authentication & Authorization
* Role-Based Access Control (RBAC)
* ORM Relationships (One-to-Many)
* Modular Backend Architecture
* REST API Design

---

## 📌 Future Improvements

* 💳 Payment Integration
* 📦 Order Status Tracking
* 📧 Email Notifications
* 🔄 Refresh Tokens
* 🐳 Docker Support

---

## 👨‍💻 Author

**Narase Gowda**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
