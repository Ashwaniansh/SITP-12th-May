from flask import Flask, render_template, request
import pandas as pd
import joblib
import sqlite3

app = Flask(__name__)


df = pd.read_csv(
    r"D:\Data Science with AI & ML\SITP-12th-May\MACHINE LEARNING\PROJECT 1\DATA\Clean_laptop_price_prediction_data1.csv"
)


model = joblib.load("model_rfr.lb")

brand_list = sorted(df["brand"].unique())
processor_list = sorted(df["processor"].unique())
cpu_list = sorted(df["CPU"].unique())
ram_list = sorted(df["Ram"].unique())
ram_type_list = sorted(df["Ram_type"].unique())
rom_list = sorted(df["ROM"].unique())
rom_type_list = sorted(df["ROM_type"].unique())
gpu_list = sorted(df["GPU"].unique())
display_list = sorted(df["display_size"].unique())
os_list = sorted(df["OS"].unique())
warranty_list = sorted(df["warranty"].unique())


def dropdown():
    return {
        "brand_list": brand_list,
        "processor_list": processor_list,
        "cpu_list": cpu_list,
        "ram_list": ram_list,
        "ram_type_list": ram_type_list,
        "rom_list": rom_list,
        "rom_type_list": rom_type_list,
        "gpu_list": gpu_list,
        "display_list": display_list,
        "os_list": os_list,
        "warranty_list": warranty_list
    }

def init_db():

    conn = sqlite3.connect("laptop_predictions.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        brand INTEGER,
        processor INTEGER,
        cpu INTEGER,
        ram INTEGER,
        ram_type INTEGER,
        rom INTEGER,
        rom_type INTEGER,
        gpu INTEGER,
        display_size REAL,
        os INTEGER,
        warranty INTEGER,
        predicted_price REAL
    )
    """)

    conn.commit()
    conn.close()


init_db()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/project")
def project():
    return render_template(
        "project.html",
        **dropdown()
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/predict", methods=["POST"])
def predict():

    brand = int(request.form["brand"])
    processor = int(request.form["processor"])
    cpu = int(request.form["cpu"])
    ram = int(request.form["ram"])
    ram_type = int(request.form["ram_type"])
    rom = int(request.form["rom"])
    rom_type = int(request.form["rom_type"])
    gpu = int(request.form["gpu"])
    display_size = float(request.form["display_size"])
    os = int(request.form["os"])
    warranty = int(request.form["warranty"])

    input_data = pd.DataFrame(
        [[
            brand,
            processor,
            cpu,
            ram,
            ram_type,
            rom,
            rom_type,
            gpu,
            display_size,
            os,
            warranty
        ]],
        columns=[
            "brand",
            "processor",
            "CPU",
            "Ram",
            "Ram_type",
            "ROM",
            "ROM_type",
            "GPU",
            "display_size",
            "OS",
            "warranty"
        ]
    )

    prediction = round(
        float(model.predict(input_data)[0]),
        2
    )
    conn = sqlite3.connect("laptop_predictions.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO predictions (
            brand,
            processor,
            cpu,
            ram,
            ram_type,
            rom,
            rom_type,
            gpu,
            display_size,
            os,
            warranty,
            predicted_price
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        brand,
        processor,
        cpu,
        ram,
        ram_type,
        rom,
        rom_type,
        gpu,
        display_size,
        os,
        warranty,
        prediction
    ))

    conn.commit()
    conn.close()

    return render_template(
        "project.html",
        prediction=prediction,
        **dropdown()
    )

@app.route("/history")
def history():

    conn = sqlite3.connect("laptop_predictions.db")

    data = pd.read_sql_query(
        "SELECT * FROM predictions ORDER BY id DESC",
        conn
    )

    conn.close()

    if not data.empty:
        data["predicted_price"] = data["predicted_price"].round(2)

    return render_template(
        "history.html",
        tables=[
            data.to_html(
                index=False,
                classes="history-table",
                border=0
            )
        ]
    )

if __name__ == "__main__":
    app.run(debug=True)