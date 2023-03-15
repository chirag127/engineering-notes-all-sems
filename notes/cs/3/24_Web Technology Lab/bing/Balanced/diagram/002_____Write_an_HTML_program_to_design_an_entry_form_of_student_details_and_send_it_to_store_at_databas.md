Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a possible answer to your question:

### Write an HTML program to design an entry form of student details and send it to store at database server like SQL, Oracle or MS Access for the notes of the Unit 1 - Develop static web pages using HTML in the subject of Web Technology Lab

- To design an entry form of student details, you need to use HTML elements such as `<form>`, `<input>`, `<label>`, `<select>`, `<option>`, `<button>`, etc. You can also use CSS to style the form elements and layout  .
- To send the form data to a database server, you need to specify the `action` and `method` attributes of the `<form>` element. The `action` attribute defines the URL where the form data will be sent, and the `method` attribute defines the HTTP request method to use, such as `GET` or `POST`.
- To store the form data in a database server, you need to write a server-side script that can handle the form data and execute SQL queries to insert, update, delete, or retrieve data from the database. You can use any programming language that can communicate with the database server, such as PHP, ASP.NET, Python, etc .
- Here is an example of an HTML program that creates a simple entry form of student details and sends it to a PHP script that stores the data in a MySQL database:

```html
<html>
<head>
    <style>
        /* CSS code to style the form elements and layout */
        form {
            width: 400px;
            margin: 0 auto;
            border: 1px solid black;
            padding: 20px;
        }

        label {
            display: block;
            margin-bottom: 10px;
        }

        input, select {
            width: 100%;
            box-sizing: border-box;
        }

        button {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <form action="save_student.php" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Phone:</label>
        <input type="tel" id="phone" name="phone" required>

        <label for="course">Course:</label>
        <select id="course" name="course" required>
            <option value="">Select a course</option>
            <option value="Web Technology">Web Technology</option>
            <option value="Database Management">Database Management</option>
            <option value="Software Engineering">Software Engineering</option>
        </select>

        <label for="gender">Gender:</label>
        <input type="radio" id="male" name="gender" value="Male" required>
        <label for="male">Male</label>
        <input type="radio" id="female" name="gender" value="Female" required>
        <label for="female">Female</label>

        <label for="dob">Date of Birth:</label>
        <input type="date" id="dob" name="dob" required>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

- Here is an example of a PHP script that receives the form data and stores it in a MySQL database:

```php
<?php
// Connect to the database server
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "student_db";

$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Get the form data
$name = $_POST["name"];
$email = $_POST["email"];
$phone = $_POST["phone"];
$course = $_POST["course"];
$gender = $_POST["gender"];
$dob = $_POST["dob"];

// Prepare and execute the SQL query to insert the data
$sql = "INSERT INTO student (name, email, phone, course, gender, dob) VALUES (?, ?, ?, ?, ?, ?)";
$stmt = $conn