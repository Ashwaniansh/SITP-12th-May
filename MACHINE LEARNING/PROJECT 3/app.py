from flask import Flask, request, render_template
import joblib
import sqlite3
import os

print("Current Folder =", os.getcwd())
print("App File =", __file__)

app = Flask(__name__)

model = joblib.load("model_rfr.lb")

def init_db():
    conn = sqlite3.connect('loan_history.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS loan_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        income INTEGER,
        credit_score INTEGER,
        loan_amount INTEGER,
        years_employed INTEGER,
        prediction TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/predict', methods=['POST'])
def predict():

    income = int(request.form['income'])
    credit_score = int(request.form['credit_score'])
    loan_amount = int(request.form['loan_amount'])
    years_employed = int(request.form['years_employed'])

    pred = model.predict([[
        income,
        credit_score,
        loan_amount,
        years_employed
    ]])
    print("================================")
    print("Income =", income)
    print("Credit Score =", credit_score)
    print("Loan Amount =", loan_amount)
    print("Years Employed =", years_employed)
    print("Raw Prediction =", pred)
    print("================================")


    if pred[0] == 1:
        result = "Loan Approved"
    else:
        result = "Loan Rejected"

    conn = sqlite3.connect('loan_history.db')
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO loan_history
    (income, credit_score, loan_amount,
     years_employed, prediction)
    VALUES (?, ?, ?, ?, ?)
    """,
    (
        income,
        credit_score,
        loan_amount,
        years_employed,
        result
    ))

    conn.commit()
    conn.close()

    return render_template(
        'project.html',
        prediction=result
    )

@app.route('/history')
def history():

    conn = sqlite3.connect('loan_history.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM loan_history
    ORDER BY id DESC
    """)

    historical_data = cursor.fetchall()

    conn.close()

    return render_template(
        'history.html',
        historical_data=historical_data
    )

if __name__ == "__main__":
    app.run(debug=True)