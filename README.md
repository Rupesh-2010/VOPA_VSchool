V-School Assignment API
This Flask-based API enables an edtech platform (V-School) to manage lesson assignments between teachers and students. Teachers can assign lessons, track completion status, and students can view and mark their assigned lessons as completed.

Features
Teachers can assign existing lessons to multiple students with due dates and optional notes.

Students can view their assigned, incomplete lessons.

Students can mark their lessons as completed.

Teachers can view all assignments they have made along with completion status.

API Endpoints
POST /api/assignments
Assign lessons to students (bulk assignment supported).

GET /api/assignments/student/<student_id>
Fetch incomplete assignments for a specific student.

PUT /api/assignments/<assignment_id>/complete
Mark an assignment as completed.

GET /api/assignments/teacher/<teacher_id>
View all assignments created by a teacher, with completion info.

Request & Response Example
Assign lessons (POST /api/assignments)
Request Body (JSON):

json
{
  "lessonId": "lesson123",
  "studentIds": ["studentA", "studentB"],
  "teacherId": "teacherX",
  "dueDate": "2025-08-30T23:59:59Z",
  "note": "Complete this before the next class"
}
Successful Response:

json
{
  "assignments": [
    {
      "_id": "64de1234abcd5678ef901234",
      "lessonId": "lesson123",
      "studentId": "studentA",
      "teacherId": "teacherX",
      "status": "assigned",
      "assignedAt": "2025-08-17T09:30:00Z",
      "completedAt": null,
      "dueDate": "2025-08-30T23:59:59Z",
      "note": "Complete this before the next class"
    },
    ...
  ]
}
Getting Started
Install dependencies:
pip install flask flask-pymongo

Start MongoDB locally on default port 27017.

Run the server:
python app.py

Important Considerations
Data validation: Ensure required fields are present and correctly formatted.

Authorization: Implement role-based access control to protect teacher/student actions.

Performance: Optimize queries and consider indexing based on assignment volume.

Database schema: Store assignment metadata with references to lessons, students, and teachers.

Testing
The included Postman collection (see screenshot example) shows how to test API endpoints with example requests and responses for easy verification.
