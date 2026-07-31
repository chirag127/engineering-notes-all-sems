# Program for maintaining database by sending queries for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab

- Server-side programming is the process of creating dynamic web pages that interact with databases, files, and other servers using a programming language that runs on the web server.
- ASP, JSP, and PHP are examples of server-side programming languages that can be used to design dynamic web pages using server-side programming.
- ASP stands for Active Server Pages, a server-side scripting technology that allows developers to create dynamic web pages using HTML, CSS, JavaScript, and VBScript. ASP was created by Microsoft and runs on Windows servers.
- JSP stands for Java Server Pages, a server-side scripting technology that allows developers to create dynamic web pages using HTML, XML, or other types, combined with Java code. JSP was created by Sun Microsystems and runs on any server that supports Java.
- PHP stands for Hypertext Preprocessor, a server-side scripting language that allows developers to create dynamic web pages using HTML, CSS, JavaScript, and PHP code. PHP was created by Rasmus Lerdorf and runs on any server that supports PHP.
- To maintain a database by sending queries using server-side programming, the following steps are required:
  - Create a database and a table on the server using a database management system (DBMS) such as MySQL, Oracle, SQL Server, etc.
  - Establish a connection between the server-side script and the database using a database driver or an API such as JDBC, ODBC, PDO, etc.
  - Write SQL queries to perform operations on the database such as inserting, updating, deleting, or retrieving data.
  - Execute the queries using the server-side script and display the results on the web page using HTML, CSS, and JavaScript.
  - Close the connection to the database when the operation is completed.
- The following are some examples of server-side scripts that can be used to maintain a database by sending queries using ASP, JSP, and PHP:

## ASP Example

```asp
<%@ Language=VBScript %>
<%
'Create a connection object
Set conn = Server.CreateObject("ADODB.Connection")
'Open the connection using a connection string
conn.Open "Driver={SQL Server};Server=localhost;Database=webtech;Uid=sa;Pwd=1234;"
'Create a recordset object
Set rs = Server.CreateObject("ADODB.Recordset")
'Write a SQL query to select all records from the notes table
sql = "SELECT * FROM notes"
'Execute the query and store the result in the recordset object
rs.Open sql, conn
'Display the result in an HTML table
Response.Write "<table border='1'>"
Response.Write "<tr><th>Id</th><th>Title</th><th>Content</th></tr>"
Do While Not rs.EOF
  Response.Write "<tr>"
  Response.Write "<td>" & rs("id") & "</td>"
  Response.Write "<td>" & rs("title") & "</td>"
  Response.Write "<td>" & rs("content") & "</td>"
  Response.Write "</tr>"
  rs.MoveNext
Loop
Response.Write "</table>"
'Close the recordset and the connection objects
rs.Close
conn.Close
%>
```

## JSP Example

```jsp
<%@ page import="java.sql.*" %>
<%
//Create a connection object
Connection conn = null;
//Create a statement object
Statement stmt = null;
//Create a resultset object
ResultSet rs = null;
//Open the connection using a driver and a URL
Class.forName("com.mysql.jdbc.Driver");
conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/webtech", "root", "1234");
//Create a statement object from the connection object
stmt = conn.createStatement();
//Write a SQL query to select all records from the notes table
String sql = "SELECT * FROM notes";
//Execute the query and store the result in the resultset object
rs = stmt.executeQuery(sql);
//Display the result in an HTML table
out.println("<table border='1'>");
out.println("<tr><th>Id</th><th>Title</th><th>Content</th></tr>");
while(rs.next()){
  out.println("<tr>");
  out.println("<td>" + rs.getInt("id") + "</td>");
  out.println("<td>" + rs.getString("title") + "</td>");
  out.println("<td>" + rs.getString("content") + "</td>");
  out.println("</tr>");

```
