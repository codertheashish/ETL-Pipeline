# 🚀 Python ETL Pipeline

A Python-based ETL (Extract, Transform, Load) pipeline that extracts employee data from a JSON file, cleans and validates the data, generates business KPIs, exports processed data to JSON, and loads it into a MySQL database.

---

## 📌 Features

- 📥 Extract employee data from JSON
- 🧹 Clean and standardize employee records
- ❌ Remove duplicate records
- 💰 Validate salary values
- 📧 Validate email addresses
- 📈 Calculate salary increments
- 📊 Generate employee KPIs
- 💾 Export cleaned data to JSON
- 🗄️ Load processed data into MySQL Database
- 📝 Logging support

---
## Clone the Repository

```bash
https://github.com/codertheashish/ETL-Pipeline.git
```

## 🛠️ Technologies Used

- Python 3
- MySQL
- JSON
- Regular Expressions (Regex)
- Logging
- Functional Programming (Map, Filter, Reduce)

---

## 📂 Project Structure

```
Python-ETL/
│
├── main.py
├── etl.py
├── extract.py
├── transform.py
├── load.py
├── database.py
├── config.py
├── logger.py
│
├── JSON/
│   └── employees.json
│
├── output/
│   ├── cleaned_employees.json
│   └── employee_kpi.json
│
└── README.md
```

---

## ⚙️ ETL Workflow

### 1️⃣ Extract
- Read employee records from a JSON file.

### 2️⃣ Transform
- Clean employee names
- Standardize departments
- Convert emails to lowercase
- Remove duplicate records
- Validate salaries
- Validate email addresses
- Calculate salary increment
- Generate KPIs

### 3️⃣ Load
- Save cleaned employee data
- Save KPI report
- Insert records into MySQL Database

---

## 📊 Generated KPI

The pipeline generates:

- Total Records
- Valid Records
- High Performers
- Total Salary Increment
- Highest Salary
- Lowest Salary

---

## 📁 Input

```
employees.json
```

---

## 📁 Output

```
cleaned_employees.json
employee_kpi.json
```

---

## ▶️ Run Project

```bash
python etl.py
```

or

```bash
python main.py
```

---

## 📸 Sample Output

### Cleaned Employee Data

- Standardized Names
- Valid Emails
- Salary Increment
- Updated Salary

### KPI Report

- Total Employees
- Valid Employees
- High Performers
- Salary Statistics

---

## 👨‍💻 Author

**Ashish Kumar Prajapati**

- GitHub :
[codertheashish](https://github.com/codertheashish)
- LinkedIn :
[codertheashish](https://www.linkedin.com/in/codertheashish/)
- Instagram :
[codertheashish](https://www.instagram.com/codertheashish/)
---

⭐ If you like this portfolio, don't forget to give it a star on GitHub.

<img width="601" height="437" alt="ETL Pipeline" src="https://github.com/user-attachments/assets/42e0995a-8e6e-486e-8903-beb060650931" />
