# Employee Management Module

This is a beginner-friendly Odoo custom module designed to teach the fundamentals of Odoo module development.

## 1. Project Overview
This module creates a simple **Employee Management** application inside Odoo. It allows you to:
- Create and manage **Departments**.
- Create and manage **Employees**, assigning them to departments.
- Keep track of employee details, salaries, and active status.
- Easily filter and search through employee records.

### Technologies Used
- **Odoo:** The core business application framework.
- **Python:** For backend logic, models, computations, and validation.
- **PostgreSQL:** The database Odoo uses (handled automatically via the ORM).
- **XML:** For defining the UI (views, menus, and actions).
- **Odoo ORM:** The Object-Relational Mapping system that interacts with PostgreSQL securely and efficiently.

---

## 2. Module Structure & Important Files

### `__manifest__.py`
**What is this?** This is the entry point of the module.
**Why do we need it?** It tells Odoo that this folder is an Odoo addon. It contains metadata (name, version, author), dependencies (like `base`), and the list of data files (XML, CSV) to load and their order.

### `__init__.py` (Root and Models folder)
**What is this?** Python file that makes a directory behave like a Python package.
**Why do we need it?** Odoo needs to import the python files we create. The root `__init__.py` imports the `models` folder, and the `models/__init__.py` imports `department.py` and `employee.py`.

### `models/` (Python Models)
This folder holds our business logic and database schema definitions.

#### `employee.management` (models/employee.py)
This model represents an employee. It defines fields like Name, Email, Salary, and Joining Date.
#### `employee.department` (models/department.py)
This model represents a department. It holds a name, description, and an active toggle.

**Fields & Relationships:**
- **Char / Float / Date / Boolean:** Basic data types representing simple data in the database.
- **Many2one (`department_id` in Employee):** This links one employee to a single department. It creates a Foreign Key in the database.
- **One2many (`employee_ids` in Department):** This is a virtual relationship that looks up all employees whose `department_id` points to the current department.

**ORM Basics used in Odoo:**
- `self.env`: The environment that holds references to the database cursor, user, and context. (e.g., `self.env['employee.department'].search([])`)
- `search()`: Find records matching a condition.
- `create()` / `write()`: Add new records or update existing ones.
- `browse()`: Retrieve records by their ID.

**Computed Fields (`@api.depends`)**
We have an `annual_salary` field. The `@api.depends('salary')` decorator tells Odoo: *Whenever the `salary` field changes, trigger this function to recalculate the annual salary by multiplying it by 12*.

**Validation (`@api.constrains`)**
We use this to enforce business rules. For example, if a user enters a negative salary, the ORM catches it and raises a `ValidationError`, preventing bad data from saving to the database.

### `security/ir.model.access.csv`
**What is this?** The security access file.
**Why do we need it?** By default, Odoo blocks access to new models. We must grant **CRUD (Create, Read, Update, Delete)** permissions to user groups. This file gives basic users (1,1,1,1) full access to our new models so they can interact with the app.

### `views/` (XML Interface)
These files define how the application looks.

#### List/Tree View
Shows multiple records in a table format. Perfect for the main screen of the Employees or Departments.

#### Form View
Shows a single record with all its fields arranged neatly using `<group>` and `<notebook>` tags. Used for creating or editing.

#### Search View
Defines how users can search and filter the records (e.g., filtering by "Active Employees").

#### Actions and Menus
- **Action (`ir.actions.act_window`):** Tells Odoo *what to do* when a menu is clicked (e.g., "Open the employee.management model in tree and form views").
- **Menu (`menuitem`):** The physical buttons you see in the top navbar and left sidebar.

**The Flow:** Menu -> Action -> Model -> View

---

## 3. Installation Instructions

Follow these steps to install the module in your Odoo development environment:

1. **Locate your Odoo Addons Path:** Find where your custom Odoo addons are stored. This is typically configured in your `odoo.conf` file under the `addons_path` variable.
2. **Move the Module:** Copy the entire `employee_management` folder into your custom addons directory.
3. **Restart Odoo:** Restart your Odoo server so it recognizes the new directory.
   ```bash
   # Example command (depends on your setup)
   python odoo-bin -c odoo.conf
   ```
4. **Update Apps List:**
   - Log into Odoo as an Administrator.
   - Go to **Settings** and enable **Developer Mode** (scroll to the bottom of the page).
   - Navigate to the **Apps** menu.
   - Click **Update Apps List** in the top menu and confirm.
5. **Install:**
   - Search for "Employee Management" in the search bar.
   - Click the **Install** button.

### How to Upgrade After Code Changes
If you modify Python files (`models/`), you must restart the Odoo server.
If you modify XML or CSV files, you must restart the server AND upgrade the module.
- Go to the **Apps** menu.
- Find "Employee Management", click the three dots, and select **Upgrade**.
- Or use the command line: `python odoo-bin -c odoo.conf -u employee_management`

---
## Summary of Learning
Through this module, we've demonstrated how to create a complete database-backed application in Odoo from scratch, complete with data models, relational mapping, computed logic, UI design in XML, and fundamental role-based access control.
