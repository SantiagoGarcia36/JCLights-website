from flask import Flask, render_template, request, redirect
from datetime import datetime
import sqlite3

app = Flask(__name__)


def get_db_connection():

    conn = sqlite3.connect(
        "database/leads.db"
    )

    return conn


@app.route("/")
def home():

    success = request.args.get("success")

    return render_template(
        "jclights.html",
        success=success
    )


@app.route("/submit", methods=["POST"])
def submit():

    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
    """
    INSERT INTO Leads
    (Name, Phone, Email, CreatedAt)
    VALUES (?, ?, ?, ?)
    """,
    (
        name,
        phone,
        email,
        datetime.now().isoformat()
    )
)
        

    conn.commit()

    cursor.close()
    conn.close()

    first_name = name.split()[0]

    return redirect(
        f"/?success=Thanks {first_name}! We'll contact you soon."
    )


if __name__ == "__main__":
  app.run(debug=True)