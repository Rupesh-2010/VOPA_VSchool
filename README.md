
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

