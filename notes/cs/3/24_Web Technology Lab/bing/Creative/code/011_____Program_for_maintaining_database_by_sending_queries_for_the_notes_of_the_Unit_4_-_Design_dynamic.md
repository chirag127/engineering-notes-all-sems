### Program for maintaining database by sending queries for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab

- A dynamic web page is a web page that can change its content or layout depending on the user's input, preferences, or environment.
- A dynamic web page can use server-side scripting to generate mutable content. Server-side scripting is the technique of using a programming language that runs on the web server to create web pages.
- Some of the common server-side languages are PHP, ASP, ASP.NET, JSP, and ColdFusion. These languages can use the Common Gateway Interface (CGI) to communicate with the web server and produce dynamic web pages.
- To design a dynamic web page using server-side programming, the following steps are required:
  - Choose a server-side language and a web framework that suits your needs and preferences. A web framework is a collection of tools and libraries that simplify the development of web applications.
  - Set up your development environment, which may include installing the web server, the server-side language, the web framework, and the database system.
  - Create a database and populate it with some data that you want to display on your web page. You can use a database management system (DBMS) such as MySQL, PostgreSQL, or MongoDB to create and manage your database.
  - Write the server-side code that connects to the database, executes queries, and returns the results to the web page. You can use the syntax and features of your chosen server-side language and web framework to write the code.
  - Write the HTML code that defines the structure and layout of your web page. You can use HTML tags and attributes to create the elements of your web page.
  - Write the CSS code that defines the style and appearance of your web page. You can use CSS selectors, properties, and values to apply the style rules to your web page elements.
  - Write the JavaScript code that defines the behavior and interactivity of your web page. You can use JavaScript statements, variables, functions, and events to add dynamic features to your web page.
  - Test and debug your web page using a web browser and a web developer tool. You can use the web browser to view and interact with your web page, and the web developer tool to inspect and modify the HTML, CSS, and JavaScript code of your web page.
  - Deploy your web page to a web server and make it accessible to the public. You can use a web hosting service or a cloud platform to upload and host your web page files on the web server.

- Here is an example of a dynamic web page using PHP as the server-side language and MySQL as the database system:

```php
<?php
// connect to the database
$db = mysqli_connect("localhost", "root", "", "webtech");

// check connection
if (!$db) {
  die("Connection failed: " . mysqli_connect_error());
}

// get the query parameter from the URL
$q = $_GET["q"];

// execute the query and get the result
$result = mysqli_query($db, "SELECT * FROM notes WHERE unit = '$q'");

// check result
if (mysqli_num_rows($result) > 0) {
  // output the data of each row
  while($row = mysqli_fetch_assoc($result)) {
    echo "Topic: " . $row["topic"] . "<br>";
    echo "Content: " . $row["content"] . "<br>";
    echo "<hr>";
  }
} else {
  // no data found
  echo "No notes found for unit " . $q;
}

// close connection
mysqli_close($db);
?>
```

- This PHP code connects to the MySQL database named "webtech" and executes a query to select all the notes from the table named "notes" where the unit column matches the query parameter "q" from the URL. For example, if the URL is "http://localhost/notes.php?q=4", the query parameter "q" is "4" and the query is "SELECT * FROM notes WHERE unit = '4'". The code then outputs the topic and content of each note in the result, or a message if no notes are found. The code also closes the connection to the database at the end.

- Here is an example of the HTML code that displays the dynamic