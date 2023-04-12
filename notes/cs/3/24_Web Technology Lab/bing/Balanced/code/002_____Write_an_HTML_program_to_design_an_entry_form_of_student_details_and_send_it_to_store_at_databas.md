Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a possible answer to your question:

### Write an HTML program to design an entry form of student details and send it to store at database server like SQL, Oracle or MS Access for the notes of the Unit 1 - Develop static web pages using HTML in the subject of Web Technology Lab

- To design an entry form of student details, you need to use HTML elements such as `<form>`, `<input>`, `<label>`, `<select>`, `<option>`, `<button>` etc. These elements allow you to create different types of input fields, labels, drop-down lists, buttons etc. that can collect the user's information.
- To send the form data to a database server, you need to specify the `action` and `method` attributes of the `<form>` element. The `action` attribute defines the URL of the server-side script that will process the form data, and the `method` attribute defines the HTTP method to use, such as `GET` or `POST`.
- To store the form data in a database server, you need to use a server-side scripting language such as PHP, ASP.NET, Python, etc. that can connect to the database server, execute SQL queries, and handle the form data. You also need to create a database table that can store the student details, with appropriate columns and data types.
- Here is an example of an HTML program that can design an entry form of student details and send it to store at a database server like SQL, Oracle or MS Access:

```html
<html>
<head>
  <title>Student Registration Form</title>
</head>
<body>
  <h1>Student Registration Form</h1>
  <form action="process.php" method="POST">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required><br>
    <label for="phone">Phone:</label>
    <input type="tel" id="phone" name="phone" required><br>
    <label for="address">Address:</label>
    <input type="text" id="address" name="address" required><br>
    <label for="hobbies">Hobbies:</label>
    <select id="hobbies" name="hobbies" multiple>
      <option value="reading">Reading</option>
      <option value="writing">Writing</option>
      <option value="coding">Coding</option>
      <option value="sports">Sports</option>
      <option value="music">Music</option>
    </select><br>
    <label for="course">Course:</label>
    <input type="radio" id="btech" name="course" value="B.Tech" checked>
    <label for="btech">B.Tech</label>
    <input type="radio" id="mtech" name="course" value="M.Tech">
    <label for="mtech">M.Tech</label>
    <input type="radio" id="phd" name="course" value="Ph.D">
    <label for="phd">Ph.D</label><br>
    <label for="gender">Gender:</label>
    <input type="radio" id="male" name="gender" value="male" checked>
    <label for="male">Male</label>
    <input type="radio" id="female" name="gender" value="female">
    <label for="female">Female</label>
    <input type="radio" id="other" name="gender" value="other">
    <label for="other">Other</label><br>
    <label for="dob">Date of Birth:</label>
    <input type="date" id="dob" name="dob" required><br>
    <button type="submit" name="submit">Submit</button>
  </form>
</body>
</html>
```
- Here is an example of a PHP script that can process the form data and store it in a MySQL database server:

```php
<?php
// Connect to the database server
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "student_db";

$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection

```
