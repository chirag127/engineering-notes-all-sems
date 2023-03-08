### Program for maintaining database by sending queries for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab.

In the subject of Web Technology Lab, one of the important topics is Designing dynamic web pages using server-side programming languages such as ASP, JSP, or PHP. In this unit, we will learn about maintaining databases by sending queries for notes using these programming languages.

#### What is a database?

A database is a collection of data that is organized to be easily accessed, managed and updated. It is an integral part of any web application that requires persistent storage of data. A database can be of various types such as relational, object-oriented, hierarchical, etc.

#### What is server-side programming?

Server-side programming is a type of web programming where the code is executed on the server rather than the client-side. This helps in providing dynamic content to the client-side and also in maintaining the security of the data.

#### What is ASP/JSP/PHP?

ASP (Active Server Pages), JSP (JavaServer Pages) and PHP (Hypertext Preprocessor) are server-side programming languages that help in developing dynamic web pages. These languages allow us to send queries to the database and retrieve data for display on the web page.

#### Program for maintaining database by sending queries

To maintain a database by sending queries, we need to follow these steps:

1. Connect to the database: To connect to the database, we need to provide the database name, username, and password. We can use the following code to establish a connection in PHP:

```php
<?php
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
echo "Connected successfully";
?>
```

2. Send queries: After establishing a connection, we can send queries to the database to retrieve data. We can use the following code in PHP to send a query:

```php
<?php
$sql = "SELECT * FROM MyGuests";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "id: " . $row["id"]. " - Name: " . $row["firstname"]. " " . $row["lastname"]. "<br>";
  }
} else {
  echo "0 results";
}
$conn->close();
?>
```

3. Display data: After retrieving data, we can display it on the web page using HTML and CSS.

#### Advantages of using server-side programming

1. Dynamic content: Server-side programming allows us to create dynamic content on the web page, which can change based on user input or database queries.

2. Security: Server-side programming provides better security as the code is executed on the server rather than the client-side.

3. Database connectivity: Server-side programming languages have built-in libraries and functions to connect to databases and retrieve data.

#### Disadvantages of using server-side programming

1. Slower page load times: Server-side programming requires a round trip to the server, which can result in slower page load times.

2. Server-side resources: Server-side programming requires resources such as CPU and memory on the server, which can affect the performance of the web application.

#### Examples and applications

1. E-commerce websites: E-commerce websites use server-side programming to connect to databases and retrieve product information, pricing, and availability.

2. Social networking websites: Social networking websites use server-side programming to create dynamic content, handle user authentication, and connect to databases.

In conclusion, maintaining databases by sending queries using server-side programming languages such as ASP, JSP, or PHP is an important topic in the subject of Web Technology Lab. By following the steps mentioned above, we can easily retrieve data from the database and display it on the web page.