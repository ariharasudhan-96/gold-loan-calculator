from tkinter import *
import mysql.connector

# Connect to MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",      
        password="Ari@999483", 
        database="gold_loan"
    )

# Calculate loan and save to MySQL

def calculate_loan():
    name = name_entry.get()
    phone = phone_entry.get()
    weight = float(weight_entry.get())
    rate = float(rate_entry.get())
    tenure = int(tenure_entry.get())

    loan_amount = weight * rate * 0.75
    interest = loan_amount * 0.01 * tenure
    total_amount = loan_amount + interest

    # Show result in GUI
    result = f"""
75% Gold LTV: ₹{loan_amount:.2f}
Interest (1%): ₹{interest:.2f}
Total Amount: ₹{total_amount:.2f}
"""
    result_label.config(text=result)

    # Save to MySQL
    conn = connect_db()
    cursor = conn.cursor()
    sql = "INSERT INTO loan_history (name, phone, gold_weight, gold_rate, tenure, loan_amount, interest, total_amount) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (name, phone, weight, rate, tenure, loan_amount, interest, total_amount)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()

# GUI
root = Tk()
root.title("Gold Loan Calculator")
root.geometry("450x400")

Label(root, text="Customer Name").pack()
name_entry = Entry(root)
name_entry.pack()

Label(root, text="Phone Number").pack()
phone_entry = Entry(root)
phone_entry.pack()

Label(root, text="Gold Weight (grams)").pack()
weight_entry = Entry(root)
weight_entry.pack()

Label(root, text="Gold Rate per gram").pack()
rate_entry = Entry(root)
rate_entry.pack()

Label(root, text="Tenure (months)").pack()
tenure_entry = Entry(root)
tenure_entry.pack()

Button(root, text="Calculate Loan", bg="green", fg ="white",command=calculate_loan).pack(pady=10)

result_label = Label(root, text="", justify=LEFT)
result_label.pack(pady=10)

root.mainloop()


