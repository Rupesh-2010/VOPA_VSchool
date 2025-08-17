<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>V-School Assignment API Documentation</title>
  <style>
    body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; max-width: 900px; }
    h1, h2, h3 { color: #2c3e50; }
    pre { background: #f4f4f4; padding: 10px; border-radius: 4px; overflow-x: auto; }
    code { font-family: monospace; }
    ul { margin-bottom: 20px; }
  </style>
</head>
<body>
  <h1>V-School Assignment API</h1>
  <p>This Flask-based API enables an edtech platform (V-School) to manage lesson assignments between teachers and students. Teachers can assign lessons, track completion status, and students can view and mark their assigned lessons as completed.</p>

  <h2>Features</h2>
  <ul>
    <li>Teachers can assign existing lessons to multiple students with due dates and optional notes.</li>
    <li>Students can view their assigned, incomplete lessons.</li>
    <li>Students can mark their lessons as completed.</li>
    <li>Teachers can view all assignments they have made along with completion status.</li>
  </ul>

  <h2>API Endpoints</h2>
  <ul>
    <li><strong>POST /api/assignments</strong><br />Assign lessons to students (bulk assignment supported).</li>
    <li><strong>GET /api/assignments/student/&lt;student_id&gt;</strong><br />Fetch incomplete assignments for a specific student.</li>
    <li><strong>PUT /api/assignments/&lt;assignment_id&gt;/complete</strong><br />Mark an assignment as completed.</li>
    <li><strong>GET /api/assignments/teacher/&lt;teacher_id&gt;</strong><br />View all assignments created by a teacher, with completion info.</li>
  </ul>

  <h2>Request &amp; Response Example</h2>
  <h3>Assign lessons (POST /api/assignments)</h3>
  <p><strong>Request Body (JSON):</strong></p>
  <pre><code>{
  "lessonId": "lesson123",
  "studentIds": ["studentA", "studentB"],
  "teacherId": "teacherX",
  "dueDate": "2025-08-30T23:59:59Z",
  "note": "Complete this before the next class"
}</code></pre>

  <p><strong>Successful Response:</strong></p>
  <pre><code>{
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
}</code></pre>

  <h2>Getting Started</h2>
  <ol>
    <li>Install dependencies:<br /><code>pip install flask flask-pymongo</code></li>
    <li>Start MongoDB locally on default port 27017.</li>
    <li>Run the server:<br /><code>python app.py</code></li>
  </ol>

  <h2>Important Considerations</h2>
  <ul>
    <li><strong>Data validation:</strong> Ensure required fields are present and correctly formatted.</li>
    <li><strong>Authorization:</strong> Implement role-based access control to protect teacher/student actions.</li>
    <li><strong>Performance:</strong> Optimize queries and consider indexing based on assignment volume.</li>
    <li><strong>Database schema:</strong> Store assignment metadata with references to lessons, students, and teachers.</li>
  </ul>

  <h2>Testing</h2>
  <p>The included Postman collection (see screenshot example) shows how to test API endpoints with example requests and responses for easy verification.</p>
</body>
</html>

