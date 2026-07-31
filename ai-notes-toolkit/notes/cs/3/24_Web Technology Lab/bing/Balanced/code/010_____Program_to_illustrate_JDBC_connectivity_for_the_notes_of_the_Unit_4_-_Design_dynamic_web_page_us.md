### Program to illustrate JDBC connectivity for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab

JDBC stands for Java Database Connectivity, which is an API that allows Java programs to interact with various types of databases. JDBC provides a standard interface for connecting to different databases, executing queries, and retrieving results.

To illustrate JDBC connectivity, we will use a simple example of a web page that displays the details of students from a database. The web page will be written in JSP, which is a server-side technology that allows embedding Java code in HTML. The database will be MySQL, which is a popular open-source relational database management system.

The steps involved in creating the web page are:

1. Create a database and a table in MySQL. For this example, we will create a database named `webtech` and a table named `students` with the following schema:

| Column | Type | Description |
|--------|------|-------------|
| id | int | The primary key of the table |
| name | varchar(50) | The name of the student |
| course | varchar(20) | The course enrolled by the student |
| marks | int | The marks obtained by the student |

We can use the following SQL commands to create the database and the table:

```sql
CREATE DATABASE webtech;
USE webtech;
CREATE TABLE students (
  id int PRIMARY KEY,
  name varchar(50),
  course varchar(20),
  marks int
);
```

2. Insert some sample data into the table. We can use the following SQL commands to insert some sample data:

```sql
INSERT INTO students VALUES (1, 'Alice', 'B.Tech', 85);
INSERT INTO students VALUES (2, 'Bob', 'M.Tech', 90);
INSERT INTO students VALUES (3, 'Charlie', 'B.Sc', 75);
INSERT INTO students VALUES (4, 'David', 'M.Sc', 80);
```

3. Create a JSP page that connects to the database and displays the data from the table. We will name the JSP page as `students.jsp` and save it in the web server's directory. The JSP page will have the following code:

```jsp
<%@ page import="java.sql.*" %> <!-- Import the JDBC classes -->
<html>
<head>
  <title>Students Details</title>
</head>
<body>
  <h1>Students Details</h1>
  <table border="1">
    <tr>
      <th>ID</th>
      <th>Name</th>
      <th>Course</th>
      <th>Marks</th>
    </tr>
    <% // Start of Java code
      // Load the JDBC driver for MySQL
      Class.forName("com.mysql.jdbc.Driver");
      // Establish a connection to the database
      Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/webtech", "root", "root");
      // Create a statement object to execute queries
      Statement stmt = con.createStatement();
      // Execute a query to select all records from the students table
      ResultSet rs = stmt.executeQuery("SELECT * FROM students");
      // Loop through the result set and display the data in the table
      while (rs.next()) {
        // Get the data from the current row
        int id = rs.getInt("id");
        String name = rs.getString("name");
        String course = rs.getString("course");
        int marks = rs.getInt("marks");
        // Print the data in a table row
        out.println("<tr>");
        out.println("<td>" + id + "</td>");
        out.println("<td>" + name + "</td>");
        out.println("<td>" + course + "</td>");
        out.println("<td>" + marks + "</td>");
        out.println("</tr>");
      }
      // Close the result set, statement, and connection objects
      rs.close();
      stmt.close();
      con.close();
    %> // End of Java code
  </table>
</body>
</html>
```

4. Run the JSP page on the web browser. The web browser will send a request to the web server, which will execute the JSP page and send the HTML output to the browser. The browser will display the web page as shown below:

| ID | Name | Course | Marks |
|----|------|--------|-------|
| 1 | Alice | B.Tech | 85 |
| 2 | Bob | M.Tech | 90 |
| 3 | Charlie | B.Sc | 75 |
| 4 | David | M.Sc | 80 |

This is how we can illustrate JDBC connectivity for the notes of the