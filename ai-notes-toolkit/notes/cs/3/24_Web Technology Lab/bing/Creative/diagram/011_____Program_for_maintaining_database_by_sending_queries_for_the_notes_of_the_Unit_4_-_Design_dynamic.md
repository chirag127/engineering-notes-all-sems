### Program for maintaining database by sending queries for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab

- Server-side programming is the process of writing code that runs on the web server and generates dynamic web pages based on user requests.
- ASP, JSP and PHP are examples of server-side scripting languages that can interact with databases and perform operations over them.
- ASP stands for Active Server Pages, a server-side scripting language developed by Microsoft that uses VBScript or JScript as the default scripting languages.
- JSP stands for Java Server Pages, a server-side scripting language developed by Sun Microsystems that uses Java as the scripting language and has full access to Java APIs and databases.
- PHP stands for Hypertext Preprocessor, a server-side scripting language that can be embedded in HTML and supports multiple databases and web servers.
- A program for maintaining database by sending queries using server-side programming can be written in any of these languages, depending on the choice of the web server, the database and the scripting language.
- The basic steps for writing such a program are:

  - Establish a connection to the database using the appropriate driver or library for the chosen language and database.
  - Write SQL queries to perform the desired operations on the database, such as creating, updating, deleting or retrieving data.
  - Execute the queries using the appropriate methods or functions for the chosen language and database.
  - Fetch the results of the queries and display them on the web page using the appropriate syntax and tags for the chosen language and HTML.
  - Close the connection to the database when the program is finished.

- Here is an example of a program for maintaining database by sending queries using PHP and MySQL:

```php
<?php
// Connect to the database server
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "webtech";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Write a SQL query to create a table named students
$sql = "CREATE TABLE students (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(30) NOT NULL,
email VARCHAR(50),
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)";

// Execute the query and check for errors
if ($conn->query($sql) === TRUE) {
  echo "Table students created successfully";
} else {
  echo "Error creating table: " . $conn->error;
}

// Write a SQL query to insert some data into the table
$sql = "INSERT INTO students (name, email)
VALUES ('Alice', 'alice@example.com'),
       ('Bob', 'bob@example.com'),
       ('Charlie', 'charlie@example.com')";

// Execute the query and check for errors
if ($conn->query($sql) === TRUE) {
  echo "New records created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

// Write a SQL query to select all data from the table
$sql = "SELECT * FROM students";

// Execute the query and get the result set
$result = $conn->query($sql);

// Check if the result set is not empty
if ($result->num_rows > 0) {
  // Output the data of each row as an HTML table
  echo "<table border='1'>";
  echo "<tr><th>ID</th><th>Name</th><th>Email</th><th>Registration Date</th></tr>";
  while($row = $result->fetch_assoc()) {
    echo "<tr><td>" . $row["id"] . "</td><td>" . $row["name"] . "</td><td>" . $row["email"] . "</td><td>" . $row["reg_date"] . "</td></tr>";
  }
  echo "</table>";
} else {
  echo "0 results";
}

// Close the connection
$conn->close();
?>
```