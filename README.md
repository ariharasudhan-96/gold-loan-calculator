# Gold Loan Calculator (Python + Tkinter + MySQL)

A beginner-friendly Python project using Tkinter GUI and MySQL database.

---

##  Features
- Enter Customer Name, Phone, Gold Weight, Gold Rate, Tenure
- Calculates:
  - 75% Gold LTV
  - Interest (1% per month)
  - Total Amount
- Displays results instantly in GUI
- Automatically saves every loan entry to MySQL
- `view_history.py` prints complete loan history

---

##  Technologies Used
- Python
- Tkinter (GUI)
- MySQL Database

---

## 📂 Project Files
| File | Description |
|------|-------------|
| `gold_loan.py` | Main GUI program |
| `view_history.py` | View all saved loan entries |
| `README.md` | Project Documentation |

---

## Database Setup

Run these SQL commands in MySQL:

```sql
CREATE DATABASE gold_loan_db;

USE gold_loan_db;

CREATE TABLE loan_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20),
    gold_weight FLOAT,
    gold_rate FLOAT,
    tenure INT,
    loan_amount FLOAT,
    interest FLOAT,
    total_amount FLOAT
);
