import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # your MySQL username
        password="Ari@999483", # your MySQL password
        database="gold_loan"
    )

def view_history():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM loan_history")
    rows = cursor.fetchall()

    print("\n----- LOAN HISTORY -----\n")
    for row in rows:
        print(row)

    conn.close()

view_history()
