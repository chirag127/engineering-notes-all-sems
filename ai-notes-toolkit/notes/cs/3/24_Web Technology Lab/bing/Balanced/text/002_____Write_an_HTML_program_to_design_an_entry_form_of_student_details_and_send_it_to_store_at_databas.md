### Write an HTML program to design an entry form of student details and send it to store at database server like SQL, Oracle or MS Access for the notes of the Unit 1 - Develop static web pages using HTML in the subject of Web Technology Lab

- To design an entry form of student details using HTML, you need to use the `<form>` element, which allows you to create various input fields, such as text boxes, radio buttons, checkboxes, dropdown lists, etc. 
- To send the form data to a database server, you need to specify the `action` attribute of the `<form>` element, which defines the URL of the server-side script that will process the form data. You also need to specify the `method` attribute, which defines how the form data will be transmitted. The most common methods are `GET` and `POST`. 
- To store the form data in a database server like SQL, Oracle or MS Access, you need to use a server-side scripting language, such as PHP, ASP.NET, Java, etc., that can connect to the database and execute SQL queries to insert, update, delete, or retrieve data. 

- Here is an example of an HTML program that creates a simple entry form of student details and sends it to a PHP script that stores the data in a MySQL database. You can modify the code according to your requirements and preferences.

```html
<html>
<head>
  <title>Student Entry Form</title>
</head>
<body>
  <h1>Student Entry Form</h1>
  <form action="student.php" method="POST">
    <p>First Name: <input type="text" name="fname" required></p>
    <p>Last Name: <input type="text" name="lname" required></p>
    <p>Email: <input type="email" name="email" required></p>
    <p>Phone: <input type="tel" name="phone" required></p>
    <p>Address: <input type="text" name="address" required></p>
    <p>Gender: <input type="radio" name="gender" value="Male" checked> Male <input type="radio" name="gender" value="Female"> Female</p>
    <p>Course: <select name="course" required>
      <option value="Web Technology">Web Technology</option>
      <option value="Database Management">Database Management</option>
      <option value="Software Engineering">Software Engineering</option>
      <option value="Artificial Intelligence">Artificial Intelligence</option>
    </select></p>
    <p>Date of Birth: <input type="date" name="dob" required></p>
    <p>Hobbies: <input type="checkbox" name="hobbies[]" value="Reading"> Reading <input type="checkbox" name="hobbies[]" value="Music"> Music <input type="checkbox" name="hobbies[]" value="Sports"> Sports</p>
    <p><input type="submit" value="Submit"> <input type="reset" value="Reset"></p>
  </form>
</body>
</html>
```

- Here is an example of a PHP script that receives the form data and stores it in a MySQL database. You need to create a database and a table with the appropriate columns and data types before running this script. You also need to change the database connection parameters according to your configuration.

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
$fname = $_POST["fname"];
$lname = $_POST["lname"];
$email = $_POST["email"];
$phone = $_POST["phone"];
$address = $_POST["address"];
$gender = $_POST["gender"];
$course = $_POST["course"];
$dob = $_POST["dob"];
$hobbies = $_POST["hobbies"];

// Convert the hobbies array to a comma-separated string
$hobbies = implode(",", $hobbies);

// Prepare and execute the SQL query to insert the data
$sql = "INSERT INTO student (fname, lname, email, phone, address, gender, course, dob, hobbies) VALUES ('$fname', '$lname', '$

```
