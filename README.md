# 🛍️ Ecommerce API

A fully–featured **Ecommerce REST API** built with **Django** and **Django REST Framework (DRF)**.  
It provides a secure backend for an online store including **user management**, **products**, **orders**, **payments**, and **addresses**, with full **JWT authentication** and **interactive API documentation via Swagger**.

---

## 🚀 Features

- **User Management**: Custom user model with email-based login and role-based permissions (Admin/Customer).
- **Product & Category Management**: Create, list, filter, and search products and categories.
- **Orders & Order Items**: Place orders, add items, calculate totals automatically.
- **Payments**: Record and track payment status for each order.
- **Addresses**: Manage multiple addresses with a unique default address per user.
- **JWT Authentication**: Secure authentication using JSON Web Tokens.
- **Interactive API Docs**: Built-in Swagger UI for testing and exploring endpoints.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|--------|
| **Django 4+** | Core backend framework |
| **Django REST Framework** | REST API implementation |
| **PostgreSQL** | Relational database |
| **Simple JWT** | JSON Web Token authentication |
| **drf-yasg (Swagger)** | Interactive API documentation |
| **Docker (Optional)** | Containerization for deployment |
| **Git & GitHub** | Version control and collaboration |

---

## 📂 Project Structure
```
ecommerce_api/
│
├── ecommerce_api/        # Project settings
├── products/                  # App containing all models, views & serializers
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Killian1UP/alx-project-nexus.git
cd ecommerce_app
```

### 2️⃣ Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables
Create a `.env` file in the project root:
```
SECRET_KEY=your_secret_key
DEBUG=True
```

### 5️⃣ Apply migrations
```bash
python manage.py migrate
```

### 6️⃣ Create a superuser
```bash
python manage.py createsuperuser
```

### 7️⃣ Run the development server
```bash
python manage.py runserver
```

---

## 🔐 Authentication (JWT)

Obtain an **access token** and **refresh token**:

`POST /token/`
```json
{
  "email": "your_email@example.com",
  "password": "your_password"
}
```

Use the access token in the `Authorization` header:
```
Authorization: Bearer <access_token>
```

Refresh token when needed:
`POST /token/refresh/`

---

## 📖 API Documentation

Swagger UI is available at:

```
https://ikaelelo.pythonanywhere.com/swagger/
```

### Using Swagger:
- Click **Authorize** and paste your JWT access token.
- Explore and test endpoints interactively.

---

## 🧪 Testing the API

### Option 1: Postman
- Import endpoints into Postman.
- Authenticate with your JWT token to access protected routes.

### Option 2: Curl
```bash
curl -H "Authorization: Bearer <access_token>" https://ikaelelo.pythonanywhere.com/api/users/
```

---

## 🌍 Deployment
- Configure **PostgreSQL** and environment variables for production.
- Serve static files using **WhiteNoise** or a cloud storage option.
- Optionally deploy with **Docker**, **Heroku**, or **PythonAnywhere**.

---

## 🤝 Contributing
Contributions are welcome! Please:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.

---

## 📧 Contact
**Author**: Ikaelelo Motlhako  
**Email**: ikaelelo.motlhako@gmail.com  

---

### ⭐ Demonstrations
This project demonstrates:
- Secure REST API development with Django & DRF.
- Token-based authentication using JWT.
- Professional API documentation and testing workflows.
- Deployment-ready architecture with PostgreSQL.

---
