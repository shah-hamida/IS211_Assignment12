from flask import Flask, render_template, request, redirect, session
import sqlite3
app = Flask(__name__)
app.secret_key = "1234"

def get_db():
    return sqlite3.connect("hw13.db")

@app.route("/")
def home():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "password":
            session["logged_in"] = True
            return redirect("/dashboard")
        else:
            return render_template("login.html", error="Login Failed")
    return render_template("login.html")
@app.route("/dashboard")
def dashboard():
    if "logged_in" not in session:
        return redirect("/login")
    connection = get_db()
    students = connection.execute("SELECT * FROM students").fetchall()
    quizzes = connection.execute("SELECT * FROM quizzes").fetchall()
    connection.close()
    return render_template("dashboard.html", students=students, quizzes=quizzes)

@app.route("/student/add", methods=["GET", "POST"])
def add_student():
    if "logged_in" not in session:
        return redirect("/login")
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]

        connection = get_db()
        connection.execute(
            "INSERT INTO students (first_name, last_name) VALUES (?, ?)", (first_name, last_name))
        connection.commit()
        connection.close()
        return redirect("/dashboard")
    return render_template("add_student.html")
@app.route("/quiz/add", methods=["GET", "POST"])
def add_quiz():
    if "logged_in" not in session:
        return redirect("/login")
    if request.method == "POST":
        subject = request.form["subject"]
        number_questions = request.form["number_questions"]
        quiz_date = request.form["quiz_date"]
        connection = get_db()
        connection.execute(
            "INSERT INTO quizzes (subject, number_questions, quiz_date) VALUES (?, ?, ?)",(subject, number_questions, quiz_date))
        connection.commit()
        connection.close()
        return redirect("/dashboard")
    return render_template("add_quiz.html")

@app.route("/student/<int:id>")
def student_results(id):
    if "logged_in" not in session:
        return redirect("/login")
    connection = get_db()
    results = connection.execute(
        "SELECT quiz_id, score FROM results WHERE student_id = ?",(id,)).fetchall()
    connection.close()
    return render_template("student_results.html", results=results)

@app.route("/results/add", methods=["GET", "POST"])
def add_result():
    if "logged_in" not in session:
        return redirect("/login")
    connection = get_db()

    if request.method == "POST":
        student_id = request.form["student_id"]
        quiz_id = request.form["quiz_id"]
        score = request.form["score"]

        connection.execute(
            "INSERT INTO results (student_id, quiz_id, score) VALUES (?, ?, ?)",(student_id, quiz_id, score))

        connection.commit()
        connection.close()
        return redirect("/dashboard")
    students = connection.execute("SELECT * FROM students").fetchall()
    quizzes = connection.execute("SELECT * FROM quizzes").fetchall()
    connection.close()
    return render_template("add_result.html", students=students, quizzes=quizzes)



if __name__ == "__main__":
    app.run()



