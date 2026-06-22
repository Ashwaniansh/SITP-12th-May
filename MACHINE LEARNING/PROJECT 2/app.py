from flask import Flask, request, render_template
import joblib
import sqlite3
model = joblib.load(
    r"D:\Data Science with AI & ML\SITP-12th-May\MACHINE LEARNING\PROJECT 2\MODEL\model_rfr.lb"
)

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("bike_history.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        owner TEXT,
        brand TEXT,
        kms REAL,
        age INTEGER,
        power REAL,
        prediction REAL
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

@app.route('/project', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        brand_name = request.form['brand_name']
        owner = int(request.form['owner'])
        age = int(request.form['age'])
        power = int(request.form['power'])
        kms_driven = int(request.form['kms_driven'])
        brand_dict = {
            'TVS': 1,
            'Royal Enfield': 2,
            'Triumph': 3,
            'Yamaha': 4,
            'Honda': 5,
            'Hero': 6,
            'Bajaj': 7,
            'Suzuki': 8,
            'Benelli': 9,
            'KTM': 10,
            'Mahindra': 11,
            'Kawasaki': 12,
            'Ducati': 13,
            'Hyosung': 14,
            'Harley-Davidson': 15,
            'Jawa': 16,
            'BMW': 17,
            'Indian': 18,
            'Rajdoot': 19,
            'LML': 20,
            'Yezdi': 21,
            'MV': 22,
            'Ideal': 23
        }
        brand_encoded = brand_dict.get(brand_name)
        pred = model.predict([
            [brand_encoded, owner, age, power, kms_driven]
        ])
        prediction = round(float(pred[0]), 2)
        conn = sqlite3.connect("bike_history.db")
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO history
        (owner, brand, kms, age, power, prediction)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            str(owner),
            brand_name,
            kms_driven,
            age,
            power,
            prediction
        ))
        conn.commit()
        conn.close()
    return render_template(
        'project.html',
        prediction=prediction
    )
@app.route('/history')
def history():

    conn = sqlite3.connect("bike_history.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM history
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