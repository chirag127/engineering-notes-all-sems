### Program for maintaining database by sending queries for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab

- A dynamic web page is a web page that can change its content or layout depending on the user's input, preferences, or environment.
- A dynamic web page can use server-side scripting to generate mutable content. Server-side scripting is the technique of using a programming language that runs on the web server to create web pages.
- Some of the common server-side languages are PHP, Perl, ASP, ASP.NET, JSP, and ColdFusion. These languages can use the Common Gateway Interface (CGI) to communicate with the web server and the database.
- A database is a collection of structured data that can be accessed, manipulated, and updated by the server-side language. A database can store information such as user profiles, product details, orders, etc.
- A query is a request for data or information from a database. A query can be written in a specific language such as SQL (Structured Query Language) or NoSQL (Not only SQL) depending on the type of database.
- To maintain a database by sending queries, the server-side language needs to perform the following steps:
  - Establish a connection with the database using the appropriate driver or library.
  - Create a query string that specifies the data or information to be retrieved, inserted, updated, or deleted from the database.
  - Execute the query string using the appropriate method or function of the driver or library.
  - Fetch the results of the query execution and store them in a variable or an array.
  - Close the connection with the database.
- The following are some examples of how to maintain a database by sending queries using different server-side languages:

  - PHP: PHP is a widely used open source scripting language that can be embedded in HTML. PHP can use various extensions or libraries to connect with different types of databases such as MySQL, PostgreSQL, SQLite, etc.
    - Example: The following code snippet shows how to connect to a MySQL database, create a query string to select all the records from a table named `notes`, execute the query, and display the results in a HTML table.

    ```php
    <?php
    // Create a connection with the database
    $conn = mysqli_connect("localhost", "username", "password", "database_name");

    // Check if the connection is successful
    if (!$conn) {
      die("Connection failed: " . mysqli_connect_error());
    }

    // Create a query string to select all the records from the notes table
    $sql = "SELECT * FROM notes";

    // Execute the query and store the result in a variable
    $result = mysqli_query($conn, $sql);

    // Check if the query returned any records
    if (mysqli_num_rows($result) > 0) {
      // Create a HTML table to display the results
      echo "<table border='1'>";
      echo "<tr><th>ID</th><th>Title</th><th>Content</th></tr>";

      // Loop through the result array and fetch each record
      while($row = mysqli_fetch_assoc($result)) {
        // Display each record in a table row
        echo "<tr><td>" . $row["id"] . "</td><td>" . $row["title"] . "</td><td>" . $row["content"] . "</td></tr>";
      }

      // Close the HTML table
      echo "</table>";
    } else {
      // Display a message if no records are found
      echo "No notes found";
    }

    // Close the connection with the database
    mysqli_close($conn);
    ?>
    ```

  - ASP: ASP (Active Server Pages) is a server-side scripting technology developed by Microsoft that can run on Windows servers. ASP can use various components or objects to connect with different types of databases such as Access, SQL Server, Oracle, etc.
    - Example: The following code snippet shows how to connect to an Access database, create a query string to select all the records from a table named `notes`, execute the query, and display the results in a HTML table.

    ```asp
    <% 
    ' Create a connection object
    Set conn = Server.CreateObject("ADODB.Connection")

    ' Specify the connection string to the database
    conn.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4