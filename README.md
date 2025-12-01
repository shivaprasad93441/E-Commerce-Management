# E-Commerce Management System

## 📌 Project Overview
The **E-Commerce Management System** is a simple Python + SQL based console project that allows users to browse products, add them to a cart, and place orders. The admin module allows product management and viewing orders.

This project is designed without Django/Flask to keep it beginner-friendly.

---

## 🛠️ Technologies Used
- Python
- SQLite Database
- HTML & CSS (Static Pages)
- Basic JavaScript

---

## 🚀 Features

### 👤 User Features
- View available products  
- Add products to cart  
- Place an order  
- View order summary  

### 🛠️ Admin Features
- Add new product  
- Delete existing product  
- View all orders  
- Update stock  

---

## 📁 Project Structure
Ecommerce_Project/
│── main.py
│── database.py
│── product_operations.py
│── order_operations.py
│── ecommerce.db
│
└── static/
│── index.html
│── style.css

---

## 🗄️ Database Design

### **products table**
| Column | Type | Description |
|--------|-------|-------------|
| id | INTEGER | Product ID |
| name | TEXT | Product Name |
| price | REAL | Product Price |
| stock | INTEGER | Available Stock |

### **orders table**
| Column | Type | Description |
|--------|-------|-------------|
| id | INTEGER | Order ID |
| product_id | INTEGER | Product Ordered |
| quantity | INTEGER | Quantity Ordered |
| total | REAL | Total Price |

---

## ▶️ How to Run the Project

### **1. Open Pycharm / VS Code**
Create a project folder and paste all files.

### **2. Install Python**
Required: Python 3.8+

### **3. Run the main file**
OR  
If using Pycharm, right-click → **Run main.py**

### **4. Database will auto-create**
`ecommerce.db` is automatically generated if not present.

---

## 📌 Future Improvements
- Add login system  
- Add cart persistence  
- Convert into full web app using Flask/Django  
- Add payment gateway  

---
---

## 👨‍💻 Author
Created by **Siva Prasad Thummuthukka**  
E-commerce Console Project using Python + SQL.

