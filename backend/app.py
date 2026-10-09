from flask import Flask, jsonify, request, send_from_directory
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(os.path.dirname(BASE_DIR), "frontend")
DATABASE_PATH = os.path.join(BASE_DIR, "students.db")

app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/students", methods=["GET"])
def get_students():
    connection = get_db_connection()

    students = connection.execute(
        "SELECT id, name, course FROM students"
    ).fetchall()

    connection.close()

    return jsonify([dict(student) for student in students])


@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json(silent=True)

    if not data or not data.get("name") or not data.get("course"):
        return jsonify({
            "error": "Name and course are required"
        }), 400

    name = data["name"].strip()
    course = data["course"].strip()

    if not name or not course:
        return jsonify({
            "error": "Name and course cannot be empty"
        }), 400

    connection = get_db_connection()

    cursor = connection.execute(
        "INSERT INTO students (name, course) VALUES (?, ?)",
        (name, course)
    )

    connection.commit()
    student_id = cursor.lastrowid
    connection.close()

    return jsonify({
        "id": student_id,
        "name": name,
        "course": course
    }), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)