### Program for maintaining database by sending queries for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab.

In the Unit 4 of the Web Technology Lab, you will learn about designing dynamic web pages using server-side programming languages such as ASP, JSP, and PHP. As a part of this unit, you will also learn about maintaining the database by sending queries. Here is a program that can help you maintain the database by sending queries for the notes.

#### Program for maintaining database by sending queries for the notes

1. Define the database connection: To maintain the database, you need to establish a connection to it. You can use the following code to define the database connection:

```php
<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "notes";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
?>
```

2. Insert notes into the database: To insert notes into the database, you can use the following code:

```php
<?php
$sql = "INSERT INTO notes (title, content)
VALUES ('Note Title', 'Note Content')";

if ($conn->query($sql) === TRUE) {
  echo "Note added successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
```

3. Select notes from the database: To select notes from the database, you can use the following code:

```php
<?php
$sql = "SELECT id, title, content FROM notes";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "id: " . $row["id"]. " - Title: " . $row["title"]. " - Content: " . $row["content"]. "<br>";
  }
} else {
  echo "0 results";
}

$conn->close();
?>
```

4. Update notes in the database: To update notes in the database, you can use the following code:

```php
<?php
$sql = "UPDATE notes SET content='New note content' WHERE id=1";

if ($conn->query($sql) === TRUE) {
  echo "Note updated successfully";
} else {
  echo "Error updating note: " . $conn->error;
}

$conn->close();
?>
```

5. Delete notes from the database: To delete notes from the database, you can use the following code:

```php
<?php
$sql = "DELETE FROM notes WHERE id=1";

if ($conn->query($sql) === TRUE) {
  echo "Note deleted successfully";
} else {
  echo "Error deleting note: " . $conn->error;
}

$conn->close();
?>
```

By using the above program, you can easily maintain the database by sending queries for the notes. Make sure to replace the database name, username, and password with your own values before using the code.