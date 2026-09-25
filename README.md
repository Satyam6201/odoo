# Odoo 17 Custom Modules (Dockerized)

Welcome to the **Odoo Custom Modules** repository! This project contains fully functional custom Odoo 17 modules designed to demonstrate the core fundamentals of Odoo development, database relationships, business logic, and custom reporting.

Everything is containerized using Docker, meaning you can spin up the entire Postgres + Odoo environment with a single command!

---

## 🚀 Modules Included

### 1. Employee Management (`employee_management`)
A custom module to manage employees and their departments.
* **Department Management:** Create and manage departments.
* **Employee Profiles:** Store comprehensive employee data.
* **Relational Database Mapping:** Demonstrates Odoo's `Many2one` and `One2many` relations.
* **Smart Business Logic:** Computed fields for dynamic salaries and Python validations for strict data rules.
* **Custom UI/UX:** Clean form views, list/tree views, and custom search filters.
* **Role-Based Security:** Proper `ir.model.access.csv` implementation.

### 2. College Student Management System (`college_management`)
A custom module to manage student information, departments, and courses in a college.
* **Student Records:** Manage comprehensive student details.
* **Course and Department Management:** Organize courses within departments and map students accordingly.
* **Relational Database Mapping:** Practical usage of `Many2many` and other relationships for academic structures.
* **Security & Views:** Implements appropriate access controls and structured user interfaces.

### 3. Custom Invoice - Tally Style (`custom_invoice`)
A custom invoicing module that provides a customized PDF report format.
* **Tally-Style Invoices:** Generates PDF invoices mirroring the traditional Tally format.
* **Inheritance:** Extends the standard Odoo `account` module to add custom fields and report templates.
* **Custom QWeb Reports:** Showcases how to design and integrate custom report layouts using Odoo's QWeb engine.

---

## 📂 Project Structure

```text
.
├── docker-compose.yml              # Spins up Odoo 17 and PostgreSQL 15
├── .gitignore                      # Ignores Python caches and Docker volumes
├── .dockerignore                   # Optimizes Docker context
├── employee_management/            # Employee Management Module
├── college_management/             # College Management Module
└── custom_invoice/                 # Custom Invoice Module
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
*(This will download Odoo 17 and Postgres, link them together, and mount your custom modules directly into the container).*

### Step 2: Configure the Database
1. Open your web browser and navigate to `http://localhost:8069`.
2. On the database creation screen:
   * **Database Name:** `odoo_dev` (or whatever you prefer)
   * **Email / Password:** `admin` / `admin`
   * **Demo Data:** ✅ Check this box to generate fake data.
3. Click **Create Database**.

### Step 3: Install the Modules
1. Log into Odoo.
2. Go to **Settings**, scroll to the very bottom, and click **Activate the developer mode**.
3. Open the **Apps** menu (top left icon).
4. In the top navigation bar, click **Update Apps List** and confirm.
5. In the search bar, remove the default `Apps` filter, and type the name of the module you want to install (e.g., `Employee Management`, `College Student Management System`, or `Custom Invoice`).
6. Click **Activate** on the respective module card.

---

## 🧠 What You Will Learn from This Code

If you are exploring the code in these modules, here are the key Odoo concepts implemented:

### 1. The ORM (Object-Relational Mapping)
Instead of writing raw SQL, Odoo uses Python classes to create database tables. 

### 2. Relational Fields
Examples of `Many2one`, `One2many`, and `Many2many` relationships are extensively used across all three modules to link related records.

### 3. XML Views & QWeb Reports
Odoo's frontend is entirely driven by XML. You'll see how `<tree>` defines lists, `<form>` defines layouts, and `<template>` is used in QWeb for generating custom PDF reports.

### 4. Updating Code
* If you modify `.py` files: Run `docker compose restart web`.
* If you modify `.xml` files: Go to the Apps menu in Odoo, find the app, click the 3 dots, and click **Upgrade**.
