from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/vschool"
mongo = PyMongo(app)
assignments = mongo.db.assignments


# 1) Teacher assigns lessons
@app.route("/api/assignments", methods=["POST"])
def assign_lesson():
    data = request.json
    lesson_id = data.get("lessonId")
    student_ids = data.get("studentIds")
    teacher_id = data.get("teacherId")
    due_date = data.get("dueDate")
    note = data.get("note")

    if not lesson_id or not student_ids or not teacher_id:
        return jsonify({"error": "lessonId, studentIds, teacherId required"}), 400

    created = []
    for student_id in student_ids:
        assignment = {
            "lessonId": lesson_id,
            "studentId": student_id,
            "teacherId": teacher_id,
            "status": "assigned",
            "assignedAt": datetime.utcnow(),
            "completedAt": None,
            "dueDate": due_date,
            "note": note
        }
        inserted = assignments.insert_one(assignment)
        assignment["_id"] = str(inserted.inserted_id)
        created.append(assignment)

    return jsonify({"assignments": created}), 201


# 2) Student views their incomplete assignments
@app.route("/api/assignments/student/<student_id>", methods=["GET"])
def get_student_assignments(student_id):
    result = list(assignments.find({"studentId": student_id, "status": "assigned"}))
    for r in result:
        r["_id"] = str(r["_id"])
    return jsonify(result)


# 3) Student marks assignment complete
@app.route("/api/assignments/<assignment_id>/complete", methods=["PUT"])
def mark_complete(assignment_id):
    result = assignments.update_one(
        {"_id": ObjectId(assignment_id)},
        {"$set": {"status": "completed", "completedAt": datetime.utcnow()}}
    )
    if result.modified_count == 1:
        return jsonify({"message": "Assignment marked as completed"}), 200
    else:
        return jsonify({"error": "Assignment not found"}), 404


# 4) Teacher views all assignments they assigned
@app.route("/api/assignments/teacher/<teacher_id>", methods=["GET"])
def get_teacher_assignments(teacher_id):
    result = list(assignments.find({"teacherId": teacher_id}))
    for r in result:
        r["_id"] = str(r["_id"])
    return jsonify(result)


# Home route
@app.route('/')
def home():
    return "Flask server is running 🚀"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
