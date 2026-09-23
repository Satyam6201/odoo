# Odoo 17 Employee Management System (Dockerized)

Welcome to the **Odoo Employee Management** repository! This project is a fully functional custom Odoo 17 module designed to teach and demonstrate the core fundamentals of Odoo development, database relationships, and business logic.

Everything is containerized using Docker, meaning you can spin up the entire Postgres + Odoo environment with a single command!

---

## 🚀 Features

* **Department Management:** Create and manage departments (e.g., IT, HR, Sales).
* **Employee Profiles:** Store comprehensive employee data (Name, Email, Phone, Aadhar Card, Job Position).
* **Relational Database Mapping:** Demonstrates Odoo's `Many2one` and `One2many` relations connecting Employees to Departments.
* **Smart Business Logic:**
  * **Computed Fields:** Automatically calculates the `Annual Salary` dynamically using `@api.depends` whenever the base salary changes.
  * **Python Validations:** Enforces strict data rules using `@api.constrains` (e.g., preventing negative salaries and future joining dates).
* **Custom UI/UX:** Clean form views, list/tree views, and custom search filters (e.g., filtering by "Active" employees or grouping by "Job Position").
* **Role-Based Security:** Proper `ir.model.access.csv` implementation to grant CRUD permissions to the database.

---

## 📂 Project Structure

```text
.
├── docker-compose.yml              # Spins up Odoo 17 and PostgreSQL 15
├── .gitignore                      # Ignores Python caches and Docker volumes
├── .dockerignore                   # Optimizes Docker context
└── employee_management/            # The Custom Odoo Module
    ├── __manifest__.py             # Module configuration and view load order
    ├── __init__.py                 # Initializes the Python package
    ├── models/                     # Backend Database Models
    │   ├── department.py           # employee.department model
    │   └── employee.py             # employee.management model
    ├── views/                      # Frontend XML Views
    │   ├── department_views.xml    # UI for Departments
    │   └── employee_views.xml      # UI for Employees
    └── security/
        └── ir.model.access.csv     # Database access rights
```

---

## 🛠️ How to Run This Project (Locally)

Because this project uses Docker, you do not need to install Python or PostgreSQL on your computer. 

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

### Step 1: Start the Server
Open your terminal in the root directory of this project and run:
```bash
docker compose up -d
```
*(This will download Odoo 17 and Postgres, link them together, and mount your custom module directly into the container).*

### Step 2: Configure the Database
1. Open your web browser and navigate to `http://localhost:8069`.
2. On the database creation screen:
   * **Database Name:** `odoo_dev` (or whatever you prefer)
   * **Email / Password:** `admin` / `admin`
   * **Demo Data:** ✅ Check this box to generate fake data.
3. Click **Create Database**.

### Step 3: Install the Module
1. Log into Odoo.
2. Go to **Settings**, scroll to the very bottom, and click **Activate the developer mode**.
3. Open the **Apps** menu (top left icon).
4. In the top navigation bar, click **Update Apps List** and confirm.
5. In the search bar, remove the default `Apps` filter, and type **Employee Management**.
6. Click **Activate** on the Employee Management card.

---

## 🧠 What You Will Learn from This Code

If you are exploring the code in `employee_management`, here are the key Odoo concepts implemented:

### 1. The ORM (Object-Relational Mapping)
Instead of writing raw SQL, Odoo uses Python classes to create database tables. Look at `models/employee.py`:
```python
name = fields.Char(string='Name', required=True)
salary = fields.Float(string='Salary')
```

### 2. Relational Fields
Look at how Departments and Employees are linked:
* In `employee.py`: `department_id = fields.Many2one('employee.department')`
* In `department.py`: `employee_ids = fields.One2many('employee.management', 'department_id')`

### 3. XML Views
Odoo's frontend is entirely driven by XML. Open `views/employee_views.xml` to see how `<tree>` defines lists and `<form>` defines the layout of an individual record.

### 4. Updating Code
* If you modify `.py` files: Run `docker compose restart web`.
* If you modify `.xml` files: Go to the Apps menu in Odoo, find the app, click the 3 dots, and click **Upgrade**.
