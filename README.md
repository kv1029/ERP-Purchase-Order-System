# ⚡ Nexus: Enterprise Purchase Order (PO) Management System

A modern, full-stack Purchase Order Management application built with a **FastAPI** backend and a **3D Glassmorphism Single-Page Application (SPA)** frontend. This project demonstrates secure OAuth 2.0 authentication, dynamic financial calculations, and Generative AI integration.

## 🌟 Key Features

### 🛡️ Security & Authentication
* **Google OAuth 2.0:** Secure login flow using Google Identity Services.
* **JWT Authorization:** Stateless backend security with JSON Web Tokens and strict expiration protocols.
* **Multi-Tenant Transactions:** Purchase Orders are securely tied to the authenticated user's email. Users cannot view, modify, or delete orders belonging to other accounts.

### 💻 Modern SPA Frontend (Vanilla JS + Tailwind)
* **Interactive 3D Login:** Features a custom cursor-tracking "spotlight" and 3D hologram tilt effects.
* **Glassmorphism UI:** Premium frosted-glass panels, animated mesh-gradient backgrounds, and custom modals.
* **Dynamic Form Handling:** Users can dynamically add/remove hardware allocation rows without page reloads.
* **Real-Time Financial Engine:** Instantly calculates subtotals, applies a strict 5% tax rate, and outputs the Grand Total.

### 🧠 Generative AI Integration
* **Neural Insight Tool:** Includes an AI "Magic Sparkles" button next to hardware selections.
* **Auto-Descriptions:** Instantly generates professional, context-aware marketing descriptions for selected products using simulated/live Gen-AI APIs.

### ⚙️ Backend Architecture (FastAPI + PostgreSQL)
* **Modular REST API:** Cleanly separated routing architecture for Products, Vendors, and POs.
* **Relational Database:** Designed with strict Primary/Foreign key constraints using SQLAlchemy ORM.
* **Full CRUD Capabilities:** Support for Creating POs, Reading dashboards, Updating delivery statuses (PATCH), and Cryptographically purging records (DELETE).

---

## ⚠️ Architectural Note: Master Data vs. Tenant Data
To simulate a real-world enterprise environment, this application implements a **Unified Master Data** approach alongside **Isolated Tenant Transactions**:
* **Shared Master Data:** The `Vendors` and `Products` databases are globally shared. *If User A adds a new Supplier or Hardware, User B will immediately be able to see and use it.* This mimics a company-wide unified inventory system.
* **Isolated Transactions:** The `Purchase Orders` themselves are strictly isolated. User A cannot see User B's purchase history or financial metrics. 

---

## 🛠️ Tech Stack
* **Frontend:** HTML5, CSS3, Vanilla JavaScript, Tailwind CSS, Google Identity Services.
* **Backend:** Python 3, FastAPI, Uvicorn, SQLAlchemy, python-dotenv, PyJWT.
* **Database:** PostgreSQL (or SQLite for local rapid prototyping).

---

## 🚀 Local Setup & Installation

### 1. Database Setup
1. Ensure your database is installed and running (e.g., PostgreSQL).
2. Create a new database (e.g., `nexus_po_db`).

### 2. Backend Environment
1. Navigate to the backend directory.
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate