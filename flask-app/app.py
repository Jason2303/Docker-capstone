import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        database=os.environ.get("DB_NAME", "employeedb"),
        user=os.environ.get("DB_USER", "admin"),
        password=os.environ.get("DB_PASSWORD", "secret"),
        cursor_factory=RealDictCursor
    )

@app.route("/")
def index():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees ORDER BY created_at DESC;")
    employees = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", employees=employees)

@app.route("/employee/<int:id>")
def employee(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees WHERE id = %s;", (id,))
    emp = cur.fetchone()
    cur.close()
    conn.close()
    if emp is None:
        return "Employee not found", 404
    return render_template("employee.html", emp=emp)

@app.route("/add", methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        name = request.form["name"]
        department = request.form["department"]
        role = request.form["role"]
        email = request.form["email"]
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO employees (name, department, role, email) VALUES (%s, %s, %s, %s);",
            (name, department, role, email)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for("index"))
    return render_template("add_employee.html")

@app.route("/delete/<int:id>", methods=["POST"])
def delete_employee(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM employees WHERE id = %s;", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
