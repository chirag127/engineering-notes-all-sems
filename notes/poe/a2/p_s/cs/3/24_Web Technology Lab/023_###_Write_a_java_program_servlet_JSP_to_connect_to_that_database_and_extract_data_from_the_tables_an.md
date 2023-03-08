 Here is the content in markdown format:

### Write a java program/servlet/JSP to connect to that database and extract data from the tables and display them for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

1. Import the required packages - import java.sql.*; import javax.servlet.*; import javax.servlet.http.*;
2. Register the JDBC driver - Class.forName("com.mysql.jdbc.Driver");
3. Establish the connection - Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/dbname", "username", "password");
4. Create a Statement object - Statement stmt = con.createStatement();
5. Execute the SQL query - ResultSet rs = stmt.executeQuery("SELECT * FROM table_name");
6. Process the results - while(rs.next()) { //Display values from the table }
7. Close the connections - rs.close(); stmt.close(); con.close();

Advantages:
- Easy to integrate with web applications and display data on web pages.
- Wide driver support for connecting to different databases like MySQL, Oracle, SQL Server, etc.

Disadvantages:
- Large amount of code required for database connectivity and querying.
- Prone to SQL injection attacks if proper sanitization is not done.

Examples:
- Displaying a list of products from a table on a web page.
- Fetching user details from a table to display profile information.

Applications:
- Content management systems
- E-commerce websites
- Enterprise applications

[Detailed diagrams and code snippets can be included here if required]

The content covers the key points to learn and understand for connecting to a database and extracting data using JDBC to display on web pages. The points are written in a formal tone with headings and can be used as study material for learning and exams. Please let me know if you would like me to elaborate on any part or add more details.