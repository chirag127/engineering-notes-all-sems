### Program for maintaining database by sending queries for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab

- In this program, we will use PHP as the server-side programming language to create and query a MySQL database.
- The steps to create and query a database using PHP are:

  1. Establish a connection to MySQL server from your PHP script using either MySQLi or PDO extension. You need to provide the server name, username, password, and optionally the database name as parameters. For example:

  ```php
  // Using MySQLi Object-oriented
  $servername = "localhost";
  $username = "username";
  $password = "password";
  $dbname = "myDB";

  // Create connection
  $conn = new mysqli($servername, $username, $password, $dbname);

  // Check connection
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
  ```

  ```php
  // Using PDO
  $servername = "localhost";
  $username = "username";
  $password = "password";
  $dbname = "myDB";

  try {
    // Create connection
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  } catch(PDOException $e) {
    die("Connection failed: " . $e->getMessage());
  }
  ```

  2. Write a SQL query to create a database and store it in a string variable. The CREATE DATABASE statement is used to create a new database in MySQL. For example:

  ```php
  // SQL query to create a database named demo
  $sql = "CREATE DATABASE demo";
  ```

  3. Execute the query using either the mysqli_query() or the PDO::exec() method. If the query is successful, it will return TRUE, otherwise it will return FALSE or an error message. For example:

  ```php
  // Using MySQLi Object-oriented
  if ($conn->query($sql) === TRUE) {
    echo "Database created successfully";
  } else {
    echo "Error creating database: " . $conn->error;
  }
  ```

  ```php
  // Using PDO
  try {
    // Execute the query
    $conn->exec($sql);
    echo "Database created successfully";
  } catch(PDOException $e) {
    echo "Error creating database: " . $e->getMessage();
  }
  ```

  4. Write a SQL query to create a table and store it in a string variable. The CREATE TABLE statement is used to create a new table in a database. You need to specify the table name, the column names, the data types, and optionally the constraints for each column. For example:

  ```php
  // SQL query to create a table named students with four columns: id, name, email, and score
  $sql = "CREATE TABLE students (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(50),
    score INT(3)
  )";
  ```

  5. Execute the query using either the mysqli_query() or the PDO::exec() method. If the query is successful, it will return TRUE, otherwise it will return FALSE or an error message. For example:

  ```php
  // Using MySQLi Object-oriented
  if ($conn->query($sql) === TRUE) {
    echo "Table created successfully";
  } else {
    echo "Error creating table: " . $conn->error;
  }
  ```

  ```php
  // Using PDO
  try {
    // Execute the query
    $conn->exec($sql);
    echo "Table created successfully";
  } catch(PDOException $e) {
    echo "Error creating table: " . $e->getMessage();
  }
  ```

  6. Write a SQL query to insert data into the table and store it in a string variable. The INSERT INTO statement is used to insert new records into a table. You need to specify the table name, the column names, and the values for each column. For example:

  ```php
  // SQL query to insert a record into the students table
  $sql = "INSERT INTO students (

```
